# Básicos EDACup 2023

Supongo que habrás visto el vídeo de la final de la EDACup 2022 y ahora quieres jugar con los robots. Manos a la obra.

Antes de comenzar, debes tener conocimientos mínimos de [lenguaje Python](https://es.wikipedia.org/wiki/Python).

Para probar los robots de la EDACup 2023, deberás descargar el [simulador de juego](Downloads) y los [ejemplos](Ejemplos) correspondientes, y asegurarte de tener instalado [Python](https://www.anaconda.com/products/distribution) junto a las bibliotecas [paho-mqtt](https://pypi.org/project/paho-mqtt/) y [keyboard](https://pypi.org/project/keyboard/). Una vez que hayas instalado todo, ejecuta el simulador y selecciona la opción "Sandbox". Luego, ejecuta los ejemplos que descargaste:

* Con `EDAPark.py` puedes controlar un robot de manera libre utilizando las teclas `W`, `A`, `S` y `D` para la traslación, y `Q` y `E` para la rotación. Además, en el simulador puedes probar diferentes cámaras pulsando las teclas del `1` al `9`. Si el robot se cae o se le queman los motores, puedes restablecerlo presionando la tecla `R`.
* Con `EDADance.py` puedes mover un robot en una trayectoria preestablecida.

## Ayuda

Para obtener más información sobre los básicos y hacer preguntas, te invitamos a unirte a nuestro [servidor de Discord](https://discord.gg/RAwJQxQyW2).

## Más cosas

* Para conocer más acerca de los robots de la EDACup, revisa las [especificaciones EDABot 2023](SPECS.md).
* El equipo 1 juega en la parte izquierda del campo (coordenada `x` negativa), mientras que el equipo 2 juega en la parte derecha (coordenada `x` positiva).
* Los robots de cada equipo se identifican con los siguientes `robotId`: los del equipo 1 se llaman `robot1.[M]`, donde `[M]` corresponde al número de cada robot (del 1 al 6), mientras que los del equipo 2 se llaman `robot2.[M]`.
* Si deseas personalizar las camisetas de los equipos, puedes hacerlo editando los archivos `robot1.png` y `robot2.png` que se encuentran junto al simulador de juego. Estos archivos deben tener una resolución de 112x16. Los primeros 16x16 píxeles se utilizan para el logotipo del equipo, mientras que los sucesivos 16x16 píxeles se corresponden con las imágenes de cada robot.
* Para iniciar el sandbox directamente, llama al simulador de juego mediante la línea de comando con el argumento `-sandbox`.
