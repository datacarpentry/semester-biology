---
layout: exercise
topic: Making Choices
title: Load or Download File
language: R
---
Cuando los archivos de datos son de gran tamaño, puede ser útil descargar el archivo solo si no ha sido descargado. Una forma de hacer esto es verificar si el nombre del archivo existe en su directorio de trabajo. Si existe, cárguelo, si no, descárguelo. Puede usar la función `list.files()` para obtener una lista de archivos y directorios en el
directorio de trabajo y la función `download.file(url, filename)` para descargar
el archivo de una `url` a un `filename` específico.

1. Escriba una declaración condicional que verifique si `surveys.csv` existe en el
   directorio de trabajo, si no es así, descárguelo de
   <https://ndownloader.figshare.com/files/2292172> usando `download.file()`, y finalmente
   carga el archivo en un marco de datos y muestra las primeras filas usando `head()`
   función.

2. Haga una versión de esta declaración condicional que sea una función, donde el
   el nombre del archivo sea el primer argumento y el enlace para descargar el archivo
   sea el segundo argumento. La función debe devolver el marco de datos resultante.
   Agregue algo de documentación en la parte superior de la función que describa lo que hace.
   Llame a esta función utilizando "species.csv" como nombre de archivo y
   <https://ndownloader.figshare.com/files/3299483> como enlace. Imprima las primeras
   filas del marco de datos resultante usando `head()`.