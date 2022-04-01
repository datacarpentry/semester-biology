---
layout: exercise
topic: Making Choices
title: Unit Conversion Challenge
language: R
---
Las medidas de la cantidad de energía utilizada por los procesos biológicos son críticas para
comprender muchos aspectos de la biología, desde la fisiología celular hasta el ecosistema
ecología. Hay muchas unidades diferentes para el uso de la energía y su utilización varía según los métodos, las áreas de investigación y los grupos de laboratorio. Escriba la función:
`convert_energy_units(energy_value, input_unit, output_unit)` para convertir unidades
entre los siguientes valores de energía: julios (J), kilojulios (KJ), calorías (CAL),
y kilocalorías (KCAL; *esta es la unidad utilizada para etiquetar la cantidad de energía
contenidos en los alimentos*). Un kilojulio son 1000 julios, una caloría son 4.1868 julios, una kilocaloría es 4186.8 julios. Un ejemplo de una llamada a esta función se vería así:

```
energy_in_cal <- 200
energy_in_j <- convert_energy_units(energy_in_cal, "CAL", "J")
```

Haga que esta función sea más eficiente al vincular declaraciones `if else`. Si el
unidad de entrada o la unidad de salida no coinciden con los cinco tipos indicados anteriormente,  incluya la
función print con el mensaje- "Sorry, I don't know how to convert "  que incluya el nombre de la unidad
previsto. *En lugar de escribir una conversión individual entre cada una de las unidades de medida (lo que requeriría 12 declaraciones if) podría optar por
convertir todas las unidades de entrada a una escala común y luego convertir a partir de eso
escala común a las unidades de salida. Este enfoque es especialmente útil ya que
Es posible que deba agregar nuevas unidades más tarde y esto será mucho más fácil usando este método.*

Use su función para responder las siguientes preguntas:

1. ¿Qué cantidad de energía metabólica diaria utilizada por un ser humano (~2500 KCAL) en julios?
2. ¿Cuántas energía adicional utiliza una foca común comparada con un humano? La foca común utiliza ~52,500 KJ/día ([Nagy et al. 1999](http://www.annualreviews.org/doi/abs/10.1146/annurev.nutr.19.1.247)). Use la energía metabólica diaria de un humano diario mencionada en la parte 1.
3. ¿Cuántos ergios (ERG) hay en una kilocaloría? *Dado que no incluimos la conversión de erg, esto debería devolver nuestro mensaje 'no sé cómo convertir'*