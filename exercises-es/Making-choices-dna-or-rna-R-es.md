---
layout: exercise
topic: Making Choices
title: DNA or RNA
language: R
---

Escriba una función que determine si una secuencia de pares de bases es ADN, ARN o si
no es posible decir dada la secuencia proporcionada. El ARN tiene la base Uracilo
(`"u"`) en lugar de la base Timina (`"t"`), por lo que las secuencias con u son ARN,
las secuencias con t son ADN, y las secuencias sin ninguna son desconocidas.

Puede verificar si una cadena contiene un carácter (o una subcadena más larga) en R
usando `grepl(subcadena, cadena)`, entonces `grepl("u", secuencia)` verificará si el
cadena en la variable `secuencia` tiene la base `u`.

Nombre la función `dna_or_rna()`, la misma recibir `sequence` como argumento.
Haga que la función devuelva una de las tres salidas: `"DNA"`, `"RNA"` o `"UNKNOWN"`.
Llame a la función en cada una de las siguientes secuencias.


```
seq1 <- "ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg"
seq2 <- "gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau"
seq3 <- "gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc"
```

*Reto (**opcional**)*: Descubre cómo hacer que tu función funcione con ambos
letras mayúsculas y minúsculas, o incluso cadenas con mayúsculas mixtas.
