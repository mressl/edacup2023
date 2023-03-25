#
# EDADance
# Controlador de robots EDABot
#
# (C) 2023 Marc S. Ressl
#
# Uso:
# * Ejecuta el simulador de juego EDACup 2023.
# * Inicia el modo "Sandbox".
# * Ejecuta este programa.
#
# Sugerencias:
# * Estudia paho-mqtt: https://pypi.org/project/paho-mqtt/#usage-and-api
# * Estudia struct para trabajar con payloads MQTT: https://docs.python.org/3/library/struct.html
#
# Tareas:
# * Cambia la trayectoria.
#

import math
import struct

import paho.mqtt.client as mqtt

# robotId del robot que controlamos
robot_id = 'robot1.1'

# Tiempo absoluto
time = 0

# Tiempo por mensaje
delta_time = 0.1    


# Actualiza los motores del robot
def update_robot(current_position_x, current_position_z):
    global robot_id, time

    # Trayectoria: curva de Lissajous
    # https://es.wikipedia.org/wiki/Curva_de_Lissajous
    omega_x = 0.5
    omega_z = 0.4

    setpoint_x = 2 * math.cos(omega_x * time + 1)
    setpoint_z = 2 * math.sin(omega_z * time + 1)

    # Limita la distancia máxima entre el "setpoint" y la posición actual
    delta_position_x = setpoint_x - current_position_x
    delta_position_z = setpoint_z - current_position_z
    delta_position_modulus = math.sqrt(delta_position_x * delta_position_x +\
        delta_position_z * delta_position_z)
    if delta_position_modulus > 1:
        setpoint_x = current_position_x + delta_position_x / delta_position_modulus
        setpoint_z = current_position_z + delta_position_z / delta_position_modulus

    # Envía el "setpoint" al PID
    payload = struct.pack('fff', setpoint_x, setpoint_z, 180)
    client.publish(robot_id + '/pid/setpoint/set', payload)

    # Actualiza el tiempo
    time += delta_time


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

        # Suscripción a "[robot_id]/motion/state"
        client.subscribe(robot_id + '/motion/state')

# Callback: mensaje del simulador de juego
def on_mqtt_message(client, userdata, msg):
    global robot_id

    if (msg.topic == (robot_id + '/motion/state')):
        motion_state = struct.unpack('ffffffffffff', msg.payload)

        current_position_x = motion_state[0]
        current_position_z = motion_state[2]

        update_robot(current_position_x, current_position_z)


# Programa principal
client = mqtt.Client()
client.username_pw_set('robot1', 'robot1')
client.on_connect = on_mqtt_connect
client.on_message = on_mqtt_message
client.connect('localhost', 1883, 60)
client.loop_forever()
