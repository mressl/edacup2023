# Clasificación EDACup 2023 

## Descripción

Para que tu equipo pueda participar en la EDACup 2023, es necesario que clasifiques en una prueba en la que deberás intentar marcar 100 goles en el menor tiempo posible. Para ello, ejecuta el simulador de juego y selecciona la opción "Clasificación". El software colocará automáticamente la pelota en una posición aleatoria y deberás marcar goles con un programa escrito en [lenguaje Python](https://www.python.org/) en el arco del equipo 1 con el robot `robot1.1`, mientras que el robot `robot2.1` intentará obstaculizarte. Ten en cuenta que sólo podrás controlar el robot `robot1.1`. Para saber dónde está la pelota, consulta el anexo del [reglamento de la competición](REGLAMENTO.md).

El tiempo total se calcula sumando el tiempo que tardas en completar los 100 intentos. El tiempo de cada intento se medirá desde que la pelota toca el suelo hasta que entre en el arco, según lo especificado en la regla 11 del [reglamento de la competición](REGLAMENTO.md). Si el robot no logra marcar un gol en menos de 10 segundos, se contabilizarán 10 segundos. Si el robot toca la pelota antes de que ésta toque el suelo, también se contabilizarán 10 segundos.

Sólo los ocho equipos con los tiempos más bajos se clasificarán. Las posiciones de pelota y robot obstaculizador en los 100 intentos serán las mismas para todos los equipos.

## Inscripción

Dentro de poco tiempo encontrarás aquí el enlace para la inscripción a la clasificación.

## Ayuda

Para obtener más información sobre la clasificación y hacer preguntas, te invitamos a unirte a nuestro [servidor de Discord](https://discord.gg/RAwJQxQyW2).

## Consejos

Para aumentar las posibilidades de éxito de tu equipo, te recomendamos seguir estos consejos:

* Utiliza alguna [biblioteca de vectores](https://pypi.org/search/?q=vector) para trabajar cómodamente con [vectores](https://es.wikipedia.org/wiki/Vector).
* Suscríbete sólo a los tópicos que necesitas.
* Evita enviar comandos inútiles.
* Envía los comandos desde la función callback de mensajes MQTT.
* Identifica los [cuellos de botella](https://es.wikipedia.org/wiki/Cuello_de_botella) de tu algoritmo y optimiza las partes que más tiempo consumen.
* Verifica que el simulador de juego funciona correctamente consultando los [FPS](https://es.wikipedia.org/wiki/Fotogramas_por_segundo) con la tecla `F`.
* Para iniciar el modo de clasificación directamente, llama al simulador de juego mediante la línea de comando con el argumento `-classification`.
* Si encuentras un error en el simulador, [repórtalo](https://github.com/mressl/edacup2023/issues). No lo aproveches para tu beneficio, ya que podrás quedar descalificado por conducta antideportiva.
