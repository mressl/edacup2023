#
# EDAPark
# Controlador de robots EDABot
#
# (C) 2023 Marc S. Ressl
#
# Uso:
# * Ejecuta el simulador de juego EDACup 2023.
# * Inicia el modo "Sandbox".
# * Ejecuta este programa.
# * Aprieta las teclas WASD para moverte, QE para rotar.
#
# Sugerencias:
# * Estudia paho-mqtt: https://pypi.org/project/paho-mqtt/#usage-and-api
# * Estudia struct para trabajar con payloads MQTT: https://docs.python.org/3/library/struct.html
#
# Tareas:
# * Añade controles para el dribbler, el kicker y el chipper.
#

import struct

import paho.mqtt.client as mqtt
import keyboard

# robotId del robot que controlamos
robot_id = 'robot1.1'  

 # Estado de las teclas (0: no apretado, 1: apretado)
keys_state = {     
    'w': 0,
    'a': 0,
    's': 0,
    'd': 0,
    'q': 0,
    'e': 0,
}

# Indice de mensaje motion/state (para mostrar menos mensajes)
motion_state_message_index = 0  

# Indice de mensaje motors/state (para mostrar menos mensajes)
motors_state_message_index = 0  


# Actualiza los motores del robot
def update_robot():
    global robot_id, keys_state

    # Convierte el estado de las teclas en un vector de traslación 2D y una rotación
    translation_x = keys_state['d'] - keys_state['a']
    translation_z = keys_state['w'] - keys_state['s']
    rotation = keys_state['e'] - keys_state['q']

    # Constantes de traslación y rotación
    k_translation = 0.707 * 5
    k_rotation = 0.4

    # Convierte la traslación y rotación en tensiones de los motores
    # (rota el vector de traslación 45 grados y le suma la rotación)
    motor1 = k_translation * (-translation_x + translation_z) -\
        k_rotation * rotation
    motor2 = k_translation * (-translation_x - translation_z) -\
        k_rotation * rotation
    motor3 = k_translation * (translation_x - translation_z) -\
        k_rotation * rotation
    motor4 = k_translation * (translation_x + translation_z) -\
        k_rotation * rotation

    # Controla los motores por tensión
    payload = struct.pack('f', motor1)
    client.publish(robot_id + '/motor1/voltage/set', payload)
    payload = struct.pack('f', motor2)
    client.publish(robot_id + '/motor2/voltage/set', payload)
    payload = struct.pack('f', motor3)
    client.publish(robot_id + '/motor3/voltage/set', payload)
    payload = struct.pack('f', motor4)
    client.publish(robot_id + '/motor4/voltage/set', payload)


# Callback: conexión MQTT
def on_mqtt_connect(client, userdata, flags, rc):
    global robot_id

    if rc == 1:
        print('Conexión rechazada: versión de protocolo incorrecta.')
    elif rc == 2:
        print('Conexión rechazada: identificador de cliente no válido.')
    elif rc == 3:
        print('Conexión rechazada: servidor no disponible.')
    elif rc == 4:
        print('Conexión rechazada: nombre de usuario o contraseña incorrectos.')
    elif rc == 5:
        print('Conexión rechazada: no autorizada.')
    else:
        # Estamos conectados
        print('Conexión exitosa.')

        # Suscripción a "[robot_id]/motion/state" y "[robot_id]/motors/state"
        client.subscribe(robot_id + '/motion/state')
        client.subscribe(robot_id + '/motors/state')

# Callback: mensaje del simulador de juego
def on_mqtt_message(client, userdata, msg):
    global motion_state_message_index, motors_state_message_index

    if (msg.topic == (robot_id + '/motion/state')):
        motion_state_message_index += 1

        # Mostramos cada décimo mensaje (o sea, uno por segundo)
        if motion_state_message_index == 1:
            motion_state = struct.unpack('ffffffffffff', msg.payload)

            print('Posición del robot [m]: %.3f, %.3f, %.3f' %\
                (motion_state[0], motion_state[1], motion_state[2]))
            
            # Enciende los LEDs de los ojos
            payload = struct.pack('BBBBBB', 255, 0, 0, 255, 0, 0)
            client.publish(robot_id + '/display/eyes/set', payload)
        elif motion_state_message_index == 2:
            # Apaga los LEDS de los ojos
            payload = struct.pack('BBBBBB', 0, 0, 0, 0, 0, 0)
            client.publish(robot_id + '/display/eyes/set', payload)

        elif motion_state_message_index == 10:
            motion_state_message_index = 0

    elif (msg.topic == (robot_id + '/motors/state')):
        motors_state_message_index += 1

        # Mostramos cada décimo mensaje (o sea, uno por segundo)
        if motors_state_message_index == 1:
            motors_state = struct.unpack('ffffffffffffffffffff', msg.payload)

            print('Temperatura de los motores [°C]: %.1f, %.1f, %.1f, %.1f' %\
                (motors_state[3], motors_state[7], motors_state[11], motors_state[15]))

        elif motors_state_message_index == 10:
            motors_state_message_index = 0

# Callback: evento de teclado
def on_keyboard_event(event):
    if event.name in keys_state:
        # Tecla apretada o soltada?
        if event.event_type == keyboard.KEY_DOWN:
            key_state = 1
        else:
            key_state = 0

        # Actualiza el estado de la tecla
        keys_state[event.name] = key_state

        # Actualiza el robot
        update_robot()


# Código principal
keyboard.hook(on_keyboard_event)

client = mqtt.Client()
client.username_pw_set('robot1', 'robot1')
client.on_connect = on_mqtt_connect
client.on_message = on_mqtt_message
client.connect('localhost', 1883, 60)
client.loop_forever()
