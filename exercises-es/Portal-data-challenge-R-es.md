---
layout: exercise
topic: dplyr
title: Portal Data Challenge
language: R
---

Desarrolle un pipeline para manipular los datos de la tabla `surveys` de Portal y produzca una tabla de datos solamente para las especies de Dipodomys (`DM`, `DO`, `DS`).
La identificación de la especie debe presentarse en minúsculas, no en mayúsculas.
La tabla debe contener información sobre la fecha, la identificación de la especie, el peso y la longitud del retropié (hindfoot).
Los datos no deben incluir valores nulos para en el peso o en la longitud del retropié.
La tabla debe ordenarse primero por especie (para que cada especie se agrupe) y luego por peso, con los pesos más altos en la parte superior.