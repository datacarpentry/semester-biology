---
layout: exercise
topic: QAQC
title: Data entry validation in Excel
language: SQL
---
Cree una hoja de cálculo en Excel para la entrada de datos. Debe tener cinco columnas: Date, Site, Species, Mass, and Length.


Establezca los siguientes criterios de validación de datos para evitar que se ingresen datos no válidos:

1. La columna Date debe configurarse para que no convierta las fechas a otros formatos.
2. Utilice la validación de datos en Excel para que el Site solo pueda ser uno de los siguientes `A1`, `A2`, `B1`, `B2`. Configure un mensaje de error en este criterio de validación para proporcionar información sobre cuáles son los valores válidos.
3. Utilice la validación de datos de Excel para que Species solo puedan ser una de las siguientes `Dipodomys spectabilis`, `Dipodomys ordii`, `Dipodomys merriami`. Configure el mensaje de error en este criterio de validación para proporcionar información sobre cuáles son los valores válidos.
4. Utilice la validación de datos de Excel para que Mass solo pueda ser un decimal mayor o igual a cero pero menor o igual a 500. Establezca u  mensaje de error en este criterio de validación para proporcionar información sobre cuáles son los valores válidos.
5. Length debe ser un número entero entre 1 y 10. Configure el mensaje de error en este criterio de validación para proporcionar información sobre cuáles son los valores válidos.

Verifique que las reglas de validación y el formateo de datos estén funcionando, pero no incluya ningún dato ingresado en el archivo final.
 
Guarde este archivo como `data_entry_form.xlsx`.