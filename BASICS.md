# EDACup 2023

¡Bienvenido a la EDACup 2023!

Supongo que habrás visto el vídeo de la final de la EDACup 2022 y ahora quieres jugar con los robots. Manos a la obra.

Antes de comenzar, debes tener conocimientos mínimos de [Python](https://es.wikipedia.org/wiki/Python).

Para probar los robots, descarga el [simulador de juego de la EDACup 2023](Downloads) y los ejemplos que se encuentran en la carpeta [Ejemplos](Ejemplos). Ejecuta el simulador y selecciona “Sandbox”; luego ejecuta los ejemplos de Python que descargaste:

* EDAPark.py te permite controlar un robot de manera libre. Con la ventana de Python activa, utiliza las flechas del teclado o las teclas WASD para controlar la traslación, y Q y E para controlar la rotación. También te sugerimos que en el simulador aprietes las teclas 1 a 9 para probar las diferentes cámaras.
* EDADance.py te permite controlar un robot para que siga una trayectoria preestablecida de manera autónoma.

## Más cosas

* Lee las [especificaciones EDABot](SPECS.md) para aprender más acerca de los robots de la EDACup.
* El equipo 1 juega a la izquierda (coordenada X negativa) y el equipo 2, a la derecha (coordenada X positiva).
* Los robots del equipo 1 se identifican con el prefijo MQTT “robot1.[Y]”; los robots del equipo 2, con el prefijo MQTT “robot2.[Y]”. [Y] es el número de cada robot (1 a 6).
