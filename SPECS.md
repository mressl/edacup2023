# Especificaciones EDABot

![Campo de juego](Images/EDABot.jpg)

## Resumen

EDABot es un robot virtual móvil con tres grados de libertad de movimiento (dos de traslación, uno de rotación), orientado a deportes robóticos. Cuenta con cuatro ruedas omniwheel, un controlador de posición y orientación PID, un dribbler para cuidar la pelota, un kicker para disparar la pelota hacia adelante, un chipper para disparar la pelota a 45°, una pantalla LCD en la parte superior, y dos LEDs en los ojos.

| Ítem                            | Descripción                                         |
|---------------------------------|-----------------------------------------------------|
| Dimensiones                     | ↕140 mm, ⌀ 180 mm                                   |
| Peso                            | 2.6 kg                                              |
| Peso de cada rueda              | 70 g                                                |
| Centro de masa                  | 35 mm (respecto del piso)                           |
| Capacidad de la batería         | 28.8 Wh                                             |
| Motores de las ruedas           | maxon EC 45 flat ⌀ 42.8 mm, brushless, 70 Watt      |
| Gear ratio de las ruedas        | 1:1 (directo)                                       |
| Motor del dribbler              | maxon ECX SPEED 13 L ⌀ 13 mm, brushless, BLDC motor |
| Gear ratio del dribbler         | 1:1                                                 |
| Control de los motores          | Por tensión/por corriente                           |
| Corriente máxima de los motores | 10 A                                                |

## Ruedas

Las cuatro ruedas están a 90° entre sí, a ±45° respecto del frente, numeradas 1-4 según el siguiente esquema (vista superior):

![Ruedas del EDABot](Images/EDABot-Ruedas.png)

Una tensión o corriente positiva corresponde a un giro en el sentido de las manecillas del reloj (visto desde el frente de cada rueda).

Cuando controles los motores del EDABot, no superes la temperatura máxima que soportan. ¡De lo contrario pueden quemarse!

## Controlador de posición y orientación PID

El controlador de posición y orientación [PID](https://es.wikipedia.org/wiki/Controlador_PID) simplifica enormemente el manejo de los robots. Te recomendamos encarecidamente que lo uses, en lugar de controlar los motores por tensión o corriente.

Funciona de la siguiente manera: le dictas una posición y orientación (coordenadas X, Z y giro respecto del eje Y), y el robot tratará de alcanzar esta posición y orientación, independientemente de dónde se encuentre.

Internamente, los controladores PID (proporcional, integral y derivativo) funcionan de la siguiente manera:

![Controlador PID](Images/PID.png)

El controlador calcula continuamente el error entre la posición y orientación actual, y la posición y orientación del "setpoint": de la posición y orientación en la que quieres que el robot esté.

Cambiando los parámetros P, I y D puedes cambiar el comportamiento del controlador PID. En general hay una relación de compromiso entre la velocidad de respuesta (cuán rápido llega a destino) y las oscilaciones (cuánto oscila alrededor del setpoint cuando llegó).

Cuando uses el controlador PID, también debes cuidar que no se quemen los motores, controlando, o bien: cuán lejos colocas el "setpoint" respecto del valor actual, los parámetros del PID, y la temperatura de los motores.

## Dribbler

El dribbler es un cilindro girado por un motor que ayuda a controlar la pelota frente al robot. Una tensión o corriente positiva hace girar la pelota en la dirección del robot.

## Kicker y chipper

El kicker y el chipper consisten en solenoides activados por un brevísimo pulso de corriente. La duración de este pulso determina el nivel de potencia del disparo.

El disparo se realiza descargando un capacitor de alta tensión que debe cargarse previamente. El capacitor es compartido por el kicker y el chipper.

La tensión máxima de carga es de 300 V. El robot tiene un circuito de protección que limita la tensión del capacitor a 250 V.

## LEDs de los ojos

Cada LED es controlado por tres bytes en formato R8G8B8.

## Protocolo de comunicaciones

EDABot utiliza el protocolo MQTT para la comunicación de comandos y estados.

Para conectarte al servidorutiliza estos datos:

```
hostname: 127.0.0.1
port: 1883
clientId: controller
username: robot1 o robot2
password: robot1 o robot2
```

Cada robot se identifica con un identificador `robotId`, que se utiliza como primer nivel del topic MQTT.

Los topics de lectura tienen 3 niveles. Los topics de escritura tienen 4 niveles; el último nivel es “set” o “cmd”.

| Topic | Descripción | Payload | Acceso |
| - | - | - | - |
| [robotId]/motion/state | Posición 3D [m], velocidad 3D [m/s], rotación 3D (ángulos eulerianos) [°], velocidad angular 3D [°/s] | float[12] | Read |
| [robotId]/power/state | Consumo eléctrico total [W], nivel de batería [0 (vacío)-1 (lleno)], tensión capacitor del kicker [V] | float[3] | Read |
| [robotId]/motors/state | Para cada motor (1-4, y dribbler): tensión motor N [V], corriente motor N [A], RPM motor N [60/s], temperatura chassis motor N [°C] | float[20] | Read |
| [robotId]/motor[N]/voltage/set | Control por tensión motor N [V] | float | Write |
| [robotId]/motor[N]/current/set | Control por corriente motor N [A] | float | Write |
| [robotId]/pid/setpoint/set | Posición x, z [m] y rotación r [°] | float[3] |Write |
| [robotId]/pid/parameters/set | Parámetros P, I, D del controlador de posición y parámetros P, I, D del controlador de rotación (por defecto: 20, 0, 6, 0.1, 0, 0.005). | float[6] | Write |
| [robotId]/dribbler/voltage/set | Control por tensión dribbler [V] | float | Write |
| [robotId]/dribbler/current/set | Control por corriente dribbler [A] | float | Write |
| [robotId]/kicker/chargeVoltage/set | Tensión de carga del capacitor [V] | float | Write |
| [robotId]/kicker/kick/cmd | Dispara el kicker con potencia [0-1] | float | Write |
| [robotId]/kicker/chip/cmd | Dispara el chipper con potencia [0-1] | float | Write |
| [robotId]/display/eyes/set | Color RGB del ojo izquierdo y color RGB del ojo derecho | uint8_t[6] | Write |
