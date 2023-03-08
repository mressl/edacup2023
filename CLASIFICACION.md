# Clasificación EDACup 2023 

Versión 1

## Descripción

Para que tu equipo pueda participar en la EDACup 2023, es necesario que clasifique previamente en una prueba en la que deberá intentar marcar 100 goles en el menor tiempo posible.

Para ello, debes ejecutar el simulador de juego y seleccionar la opción "Clasificación". El software colocará automáticamente la pelota en una posición aleatoria y deberás marcar goles en el arco del equipo 1 con el robot `robot1.1`, mientras que el robot `robot2.1` intentará obstaculizarte. Sólo tendrás control sobre el robot `robot1.1`.

El tiempo total se calcula sumando el tiempo que tardas en completar los 100 intentos. El tiempo de cada intento se medirá desde que la pelota toca el suelo hasta que entre en el arco, tal como se especifica en la regla 11 del [reglamento de la competición](REGLAMENTO.md). Si el robot no logra marcar un gol en menos de 10 segundos, se contabilizarán 10 segundos. Si el robot toca la pelota antes de que ésta toque el suelo, se contabilizarán 10 segundos.

Los ocho equipos con los tiempos más bajos se clasificarán. Se utilizarán las mismas posiciones de pelota y robot obstaculizador en los 100 intentos para todos los equipos.

## Consejos

Para aumentar las posibilidades de éxito de tu equipo, te recomendamos seguir estos consejos:

* Utiliza alguna [biblioteca de vectores](https://pypi.org/search/?q=vector) para trabajar cómodamente con vectores de álgebra lineal.
* Suscríbete sólo a los tópicos que necesitas.
* No envíes comandos inútiles.
* Envía comandos desde la función callback de mensajes MQTT.
* Busca los [cuellos de botella](https://es.wikipedia.org/wiki/Cuello_de_botella) de tu algoritmo y optimiza aquello que más tiempo consume.
* Para iniciar el modo de clasificación directamente, llama al simulador de juego mediante la línea de comando con el argumento `-classification`.
