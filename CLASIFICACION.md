# EDACup 2023

Proceso de clasificación - rev. 1

## Descripción

Para poder participar en la competición EDACup 2023, es necesario que tu equipo se clasifique previamente. La prueba consiste en intentar marcar 100 goles en el menor tiempo posible.

Para clasificar, deberás ejecutar el simulador de juego y seleccionar la opción "Clasificación". El software colocará automáticamente la pelota en un lugar aleatorio y deberás marcar goles en el arco del equipo 1 con el robot llamado `robot1.1` en el menor tiempo posible.

El tiempo total que tu programa tarda se calcula de la siguiente manera:

- Tienes 100 oportunidades para marcar gol.
- El tiempo total se calcula como el tiempo que tardas en completar las 100 oportunidades.
- El tiempo de cada oportunidad se calcula desde el momento en que la pelota toca el suelo hasta que cruza la línea de gol, tal como se especifica en la regla 8 del [reglamento de la competición](REGLAMENTO.md).
- Si tu robot no consigue marcar gol en menos de 10 segundos:
  - Si has tocado la pelota, se te contabilizarán 10 segundos para ese intento.
  - Si no has tocado la pelota, se te contabilizarán 20 segundos para ese intento.

## Clasificación

Para clasificar, deberás entregar tu programa en el [sitio de clasificación de la competición](https://www.ieee.org) antes de 10 de abril de 2023.

Clasificarán los ocho equipos con los tiempos más bajos.
