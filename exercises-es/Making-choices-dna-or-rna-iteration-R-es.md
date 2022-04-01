---
layout: exercise
topic: Making Choices
title: DNA or RNA Iteration
language: R
---
Esta es una continuación de [DNA or RNA]({{ site.baseurl }}/exercises/Making-choices-dna-or-rna-R).
Escriba una función, `dna_or_rna(sequence)`, que determine si una secuencia
de pares de bases es ADN, ARN, o si no es posible saberlo dada la
secuencia dada. Ya que lo único lo que la función sabrá sobre el material es la
secuencia, la única forma de diferencias entre el ADN y el ARN es que
el ARN tiene la base uracilo (`"u"`) en lugar de la base timina (`"t"`). Haga que la función  devuelva una de las tres salidas: `"DNA"`, `"RNA"` o `"UNKNOWN"`.

1. Utilice la función y un bucle `for` (for loop) para imprimir el tipo de secuencia en la siguiente lista.
2. Use su función y `sapply` para imprimir el tipo de secuencia en la siguiente lista.

```
sequences = c("ttgaatgccttacaactgatcattacacaggcggcatgaagcaaaaatatactgtgaaccaatgcaggcg", "gauuauuccccacaaagggagugggauuaggagcugcaucauuuacaagagcagaauguuucaaaugcau", "gaaagcaagaaaaggcaggcgaggaagggaagaagggggggaaacc", "guuuccuacaguauuugaugagaaugagaguuuacuccuggaagauaauauuagaauguuuacaacugcaccugaucagguggauaaggaagaugaagacu", "gauaaggaagaugaagacuuucaggaaucuaauaaaaugcacuccaugaauggauucauguaugggaaucagccggguc")
```


*Opcional: para un desafío adicional, haga que su función funcione con letras mayusculas y minúsculas, o incluso cadenas con que incluyan ambas*
