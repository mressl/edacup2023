# Reglamento de juego EDACup 2023

Versión 1

## Introducción

_EDACup_ es una competición robótica virtual organizada por el capítulo de estudiantes IEEE del Instituto Tecnológico de Buenos Aires.

## Regla 1: Campo de juego

![Campo de juego](Images/Campo-de-juego.png)

<figcaption align="center">El campo de juego</figcaption>

El _campo de juego_ es un rectángulo verde de 9 metros de largo por 6 metros de ancho, delimitado por líneas continuas blancas de 0.01 metros de ancho.

Las _líneas de banda_, que son las dos líneas de demarcación más largas, dividen el campo en dos mitades, mientras que las _líneas de meta_, que son las dos líneas de demarcación más cortas, se encuentran en los extremos del campo.

La _línea central_ une los puntos medios de las líneas de banda. El _punto central_ se encuentra en su punto medio, rodeado por una _circunferencia_ de 1 metro de diámetro.

Cada línea de meta tiene un _arco_, con dos paredes verticales, una pared posterior de 0.16 metros de alto y un techo. El espacio interior entre las paredes laterales mide 1 metro de ancho y 0.18 metros de profundidad, con un grosor de 0.02 metros que no invade la línea de meta.

Enfrente de cada arco hay un _área de defensa_ rectangular, con lados mayores de 2 metros paralelos a las líneas de meta y lados menores de 1 metro paralelos a las líneas de banda.

Cada arco tiene un _punto penal_ a 6 metros de distancia del centro de cada arco.

El _área técnica_ se extiende 1 metro fuera de las líneas de demarcación.

## Regla 2. Pelota

La _pelota_ utilizada en la competición es una pelota de golf estándar de color naranja, con un peso de 0.046 kg y un diámetro de 0.043 metros.

## Regla 3. Equipos

Cada _partido_ es disputado por dos _equipos_, cada uno de ellos compuesto por un máximo de seis EDABots.

Cada equipo debe designar un _representante_, quien será el encargado de comunicarse con el árbitro.

Todos los robots deben estar claramente identificados para que el árbitro pueda reconocerlos durante el partido. La identificación se realiza a través de la pantalla LCD de cada EDABot, la cual debe mostrar el logo del equipo y el número del robot. El número debe ser de al menos 8 píxeles de alto. El logo no debe contener imágenes de carácter político, religioso o personal.

El software de control de los robots debe estar escrito en [lenguaje Python](https://www.python.org/), y requerir un máximo de 8 GB de memoria y un [núcleo de procesador](https://es.wikipedia.org/wiki/Procesador_multin%C3%BAcleo). Además, debe ser completamente autónomo y sólo puede acceder a la información de los propios robots, la posición/velocidad/orientación y aceleración angular de los demás robots y de la pelota, y los eventos proporcionados por el software de control del juego. El incumplimiento de esta regla se considerará conducta antideportiva.

El software de control de los robots recibe mensajes del software de simulación del juego para conocer el estado del juego (ver anexo).

Durante un partido no está permitido modificar el software de control de los robots. Se permiten ajustes y correcciones entre partidos.

## Regla 4. El árbitro

El _árbitro_ tomará sus decisiones según su criterio, de acuerdo con las reglas y el espíritu del juego. Las decisiones del árbitro se basarán en su opinión, quien tiene el poder discrecional de tomar las decisiones adecuadas dentro del marco de las reglas del juego.

Las decisiones del árbitro sobre hechos y acciones ocurridos durante el encuentro, incluyendo la validación de un gol o el resultado del partido, son irrevocables. Por lo tanto, se deben respetar en todo momento.

El árbitro será asistido por el árbitro automático del software de simulación del juego, pero tendrá el poder de revocar cualquier decisión del árbitro automático.

Los representantes de equipo son los únicos miembros de los equipos autorizados para hablar con el árbitro.

Las facultades y obligaciones del árbitro son:

- Hacer cumplir las reglas de juego.
- Dirigir el partido en colaboración con los otros miembros del equipo arbitral.
- Tomar nota de las incidencias del partido.
- Supervisar o dar la señal para la reanudación del partido.

El equipamiento del árbitro incluye:

- Un silbato.
- Tarjetas amarillas y rojas.

## Regla 5. El árbitro asistente

La función del _árbitro asistente_ es ayudar al árbitro a tomar decisiones precisas y justas.

Los miembros de los equipos no pueden hablar con el árbitro asistente.

Las facultades y obligaciones del árbitro asistente son:

- Detectar y señalar cualquier mala conducta o incidente que no haya sido visto por el árbitro.
- Discutir situaciones poco claras con el árbitro para ayudarlo a tomar la mejor decisión posible.

## Regla 6. El operador de juego

El _operador de juego_ actúa como intermediario entre el árbitro, el software de simulación del juego y el software de control de los robots de cada equipo.

Los miembros de los equipos no pueden hablar con el operador de juego.

Las facultades y obligaciones del operador de juego incluyen:

- Configurar el juego antes del inicio del partido.
- Introducir las órdenes del árbitro en el software de simulación del juego.
- Supervisar el registro de eventos del partido en busca de situaciones que requieran atención, y notificarlas al árbitro.

## Regla 7. Duración del partido

Cada partido tiene una duración de dos períodos de 300 segundos cada uno.

En caso de empate, se jugarán dos tiempos suplementarios de 150 segundos cada uno.

Si después de los tiempos suplementarios persiste el empate, se procederá a una serie de penales con cinco lanzamientos por equipo.

El cronómetro del partido se activa mientras los robots pueden interactuar con la pelota. No se contabiliza el tiempo antes de los saques iniciales, tiros libres, tiros penales o cuando el juego se encuentra detenido.

El partido termina automáticamente si un equipo marca 10 goles en cualquier momento del juego, incluso antes de que termine el tiempo reglamentario o en los tiempos suplementarios.

## Regla 8. Inicio del partido

El juego comienza con un _saque inicial_ al inicio de cada uno de los dos períodos del partido, de los tiempos suplementarios y después de marcar un gol.

Procedimiento:

- Antes de comenzar el partido, el árbitro lanza una moneda en presencia de los representantes de los equipos. El equipo ganador elige entre tener la mitad del campo para atacar en el primer tiempo o ejecutar el saque inicial.

En el saque inicial:

- El árbitro da la orden de saque inicial.
- La pelota se coloca en el punto central y se emite el mensaje `preKickOff`.
- Todos los robots, excepto el que realiza el saque, deben estar en su propia mitad del campo de juego.
- Los robots del equipo adversario deben estar fuera del círculo central hasta que la pelota entre en juego.
- Se emite el mensaje `kickOff`.
- Es posible marcar un gol directo desde el saque inicial.

## Regla 9. Reanudación del juego

Cuando el juego se interrumpe por una causa que no favorece a ningún equipo, como una causa externa o porque ambos equipos cometieron una falta, la pelota se coloca en la posición donde se produjo el último contacto válido con un robot, y se emite el mensaje `continue`. En ese momento, ambos equipos pueden acercarse a la pelota y manipularla para continuar el juego.

## Regla 10. Pelota en juego

La pelota se considera en juego cuando se cumplen las siguientes condiciones:

- Se ha emitido el mensaje `kickOff`, `freeKick` o `penaltyKick`, y la pelota ha recorrido al menos 0.05 metros o han pasado 10 segundos desde la emisión del mensaje.
- Se ha emitido el mensaje `continue`.

La pelota se encuentra fuera de juego cuando:

- Se ha emitido el mensaje `preKickOff`, `preFreeKick`, `prePenaltyKick` o `pause`. En este caso, los robots tienen 2 segundos para reducir su velocidad a menos de 1.5 metros por segundo y alejarse de la pelota a una distancia mínima de 0.5 metros.

## Regla 11. Goles

Se considera gol válido cuando la pelota cruza completamente la línea de meta entre las paredes y debajo del techo, siempre que:

- El equipo no exceda el número de robots permitidos en el momento en que la pelota entra al arco.
- La altura de la pelota no exceda los 0.15 m después del último contacto con un robot del equipo.
- El equipo no cometa ninguna falta desde el último contacto con un robot del equipo.

En el momento en que se produce un gol, se emite el mensaje `pause`.

## Regla 12. Faltas

Los miembros de los equipos deben mostrar respeto hacia todos los implicados en el juego. Se considera conducta antideportiva el insultar o molestar al equipo adversario, al árbitro, al árbitro asistente o al operador de juego, o no obedecer las órdenes del árbitro. La conducta antideportiva puede ser penalizada con una tarjeta amarilla, una tarjeta roja, un forfait o la descalificación del equipo.

Si la pelota está en juego y el juego no progresa durante 10 segundos, el árbitro detendrá el juego y lo reanudará a continuación con el mensaje `continue`.

Cada equipo tiene su propio contador de faltas, que aumenta en uno por cada falta cometida. Cada tercera falta lleva consigo la presentación de una tarjeta amarilla.

Las siguientes faltas detienen el juego, que se reanuda con un tiro libre para el equipo adversario:

- __Doble toque inicial__. El primer robot que toca la pelota después de un saque inicial o tiro libre no puede tocarla una segunda vez antes de que otro robot la toque o se detenga el juego.
- __Cruzar las líneas de banda__. Un robot hace que la pelota se salga por una de las líneas de banda.
- __Cruzar la línea de meta propia__. Cuando un robot mueve la pelota más allá de la línea de meta de su propio equipo, la pelota se colocará a 0.2 metros de la línea de banda más cercana y a 0.2 metros de la línea de meta.
- __Cruzar la línea de meta del adversario__.  Si un robot mueve la pelota más allá de la línea de meta del equipo adversario, la pelota se colocará a 0.2 metros de la línea de banda más cercana y a 1 metro de la línea de meta.
- __Empujar__. Un robot empuja a un robot adversario cuando ambos tienen contacto con la pelota o entre sí, y el robot ejerce una fuerza sobre el robot adversario, moviendo el punto entre ambos robots hacia el robot adversario.
- __Rodear la pelota__. Impedir que el equipo adversario acceda a la pelota.
- __Robot en el área de defensa del equipo adversario__. Cuando la pelota no está en juego, y en los tiros libres antes de que la pelota vuelva a estar en juego, ningún robot debe tocar o estar en el área de defensa adversaria. Hay un período de gracia de 2 segundos para que los robots abandonen el área de defensa del equipo adversario.
- __Múltiples defensores__. Sólo se permite que haya un robot parcial o totalmente dentro del área de defensa propia. Infringir esta regla puede considerarse conducta antideportiva. Si dos robots de un mismo equipo están parcial o totalmente dentro del área de defensa propia y uno de ellos toca la pelota, el juego se detiene y se concede un tiro penal al equipo adversario.
- __Dribbling excesivo__. Los robots no pueden empujar la pelota con el dribbler por más de 1 metro, medido linealmente desde el lugar en que comenzó el contacto con la pelota. Un robot deja de usar el dribbler cuando se puede observar un espacio entre la pelota y el robot.

Las siguientes faltas no detienen el juego:

- __Tocar la pelota en el área de defensa del adversario__. La pelota no debe ser tocada cuando un robot se encuentra parcial o totalmente en el área de defensa del equipo adversario.
- __Velocidad de la pelota__. La velocidad de la pelota no debe exceder los 6.5 metros por segundo en el espacio tridimensional.
- __Choque__. Las velocidades de ambos robots son proyectadas sobre la recta que los une. Si el módulo de la diferencia entre las velocidades proyectadas supera 1.5 metros por segundo, el equipo del robot más rápido será sancionado con una falta.

Las siguientes faltas pueden ocurrir cuando la pelota no está en juego:

- __Robot demasiado cerca de la pelota__. Cuando el juego está detenido, todos los robots deben estar a más de 0.5 m de la pelota.
- __Adversario demasiado cerca de la pelota__. Antes del saque inicial o tiro libre, los robots adversarios deben permanecer a más de 0.5 m de la pelota; los robots del equipo propio pueden acercarse más. En los tiros penales, todos los robots, salvo el defensor y el atacante, deben permanecer al menos 1 m detrás de la pelota.
- __Exceso de velocidad__. Cuando la pelota no está en juego, los robots no deben moverse a más de 1.5 metros por segundo.

En todas las faltas, se considera un período de gracia de 2 segundos para la próxima falta del mismo tipo.

Si un equipo comete una falta y se presenta una _tarjeta amarilla_, se emite el mensaje `removeRobot` y el equipo en falta dispone de 10 segundos para retirar un robot a su posición inicial en el área técnica, lo cual disminuye el número de robots permitidos en el campo de juego por uno. La tarjeta amarilla expira después de 120 segundos de tiempo de juego, y en cuanto se da la próxima oportunidad, se emite el mensaje `addRobot` que autoriza al equipo a añadir un robot al campo de juego. Si la tarjeta amarilla se presenta por conducta antideportiva, el árbitro tiene la potestad de detener el partido; en este caso, el juego continúa con un tiro libre.

Una _tarjeta roja_ es similar a una tarjeta amarilla, pero no expira. Si un equipo recibe dos tarjetas amarillas aún no expiradas, la tercera tarjeta amarilla se convierte en roja. Si un equipo se queda sin robots por tarjetas amarillas o rojas, el partido termina en _forfait_, y el resultado final es de 10-0 a favor del equipo que todavía tiene robots en el campo de juego.

## Regla 13. Tiros libres

Un tiro libre se concede al equipo adversario del robot que cometió la infracción. Excepto en los casos de cruces de línea de meta o de banda, el tiro libre se ejecuta en el lugar en el que se produjo la falta. Si ese lugar está a una distancia menor de 0.2 m de las líneas de demarcación o a menos de 1 m de las áreas de defensa, la pelota se coloca en la posición válida más cercana.

En un tiro libre:

- El árbitro ordena el tiro libre.
- La pelota se coloca en su posición correspondiente y se emite el mensaje `preFreeKick`.
- Todos los robots del equipo que cometió la falta deben estar a más de 0.5 m de la pelota.
- Se emite el mensaje `freeKick`.
- Es posible anotar un gol directamente desde un tiro libre.

## Regla 14. Tiro penales

El procedimiento para los tiros penales es el siguiente:

- El árbitro ordena el tiro penal.
- La pelota se coloca en el punto penal correspondiente al arco del equipo defensor y se emite el mensaje `prePenaltyKick`.
- Un robot defensor se mueve a la línea de meta para defender su arco.
- Un robot atacante puede acercarse a la pelota sin tocarla, mientras que todos los demás robots deben permanecer al menos a 1 m de distancia detrás de la pelota.
- Se emite el mensaje `penaltyKick`.
- El robot atacante debe mover la pelota en dirección al arco.
- Si la pelota sigue en juego después de 10 s, el juego se detiene.

Se concede un gol si se cumple la regla 11 o si el equipo defensor comete una falta.

## Anexo

Lista de mensajes MQTT del software de simulación del juego:

| Tópico | Descripción | Payload |
| - | - | - |
| `ball/motion/state` | Posición 3D [m], velocidad 3D [m/s], rotación 3D (ángulos eulerianos) [°], velocidad angular 3D [°/s] | `float32 * 12` |
| `edacup/preKickOff` | Indica que el equipo (`1` o `2`) debe preparar un saque inicial. | `uint8` |
| `edacup/kickOff` | Indica que el equipo (`1` o `2`) debe realizar el saque inicial. | `uint8` |
| `edacup/preFreeKick` | Indica que el equipo (`1` o `2`) debe preparar un tiro libre. | `uint8` |
| `edacup/freeKick` | Indica que el equipo (`1` o `2`) debe realizar el tiro libre. | `uint8` |
| `edacup/prePenaltyKick` | Indica que el equipo (`1` o `2`) debe preparar un tiro penal. | `uint8` |
| `edacup/penaltyKick` | Indica que el equipo (`1` o `2`) debe realizar el tiro penal. | `uint8` |
| `edacup/pause` | Indica que el juego se detuvo. | - |
| `edacup/continue` | Indica que el juego se reanuda. | - |
| `edacup/removeRobot` | Indica que el  equipo (`1` o `2`) debe retirar un robot. | `uint8` |
| `edacup/addRobot` | Indica que el equipo (`1` o `2`) puede incorporar un robot. | `uint8` |
