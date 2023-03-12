# Competición EDACup 2023

## Descripción

Antes de participar en la EDACup 2023, es esencial que leas cuidadosamente el [reglamento de la competición](REGLAMENTO.md) para que estés familiarizado con las normas y condiciones que rigen el evento.

Tu programa debe recibir un parámetro por línea de comando ([sys.argv](https://docs.python.org/es/3/library/sys.html)) que indique de qué lado debe jugar. Si el parámetro es `1`, tu programa jugará en el equipo 1 (a la izquierda); si es `2`, jugará en el equipo 2 (a la derecha).

## Ayuda

Te invitamos a unirte a nuestro [servidor de Discord](https://discord.gg/RAwJQxQyW2) para hacer preguntas y compartir tus inquietudes.

## Consejos

Para aumentar las posibilidades de éxito de tu equipo, sigue estos consejos:

* Suscríbete sólo a los tópicos que necesitas.
* No envíes comandos inútiles.
* Envía comandos desde la función callback de mensajes MQTT.
* Analiza los partidos de la RoboCup SSL, la competición que inspiró la EDACup. Puedes buscar en [YouTube]](https://www.youtube.com/results?search_query=robocup+ssl).
* Investiga artículos científicos sobre la RoboCup SSL. Puedes buscar en [Google Scholar](https://scholar.google.com/scholar?hl=es&as_sdt=0%2C5&q=robocup+ssl&btnG=).
* Utiliza la técnica de [selfplay](https://en-m-wikipedia-org.translate.goog/wiki/Self-play_(reinforcement_learning_technique)?_x_tr_sl=auto&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=wapp) para optimizar la respuesta de tu equipo.
* Para simular eventos de juego, utiliza el control remoto. Puedes utilizar las teclas `+` y `-` para añadir o quitar goles, faltas, y tarjetas amarillas y rojas. Para preparar un saque inicial, utiliza la tecla `Saque`; para un tiro libre, la tecla `Libre`; y para un tiro penal, la tecla `Penal`. Para detener o continuar el juego, puedes utilizar la tecla `Pausa` (dos barras verticales) o `Espacio` de tu teclado. Cuando la pelota no está en juego, las flechas del control remoto o de tu teclado te permiten mover un cursor que se superpone al campo de juego. Con la tecla `Pelota` puedes mover la pelota al cursor y con la tecla `Reset` puedes reiniciar el robot más cercano al cursor.
* Para iniciar el modo de competición directamente, llama al simulador de juego mediante la línea de comando con los siguientes argumentos: `-competition-t1` para comenzar en el primer tiempo, `-competition-t2` para comenzar en el segundo tiempo, `-competition-st1` para comenzar en el primer tiempo suplementario, `-competition-st2` para comenzar en el segundo tiempo suplementario, y `-competition-penalties` para comenzar con los penales.
* Puedes consultar los registros de juego en la carpeta `Logs`, junto al simulador de juego.
* Si encuentras un error en el simulador, [repórtalo](https://github.com/mressl/edacup2023/issues). No lo aproveches para tu beneficio, ya que podrás quedar descalificado por conducta antideportiva.
