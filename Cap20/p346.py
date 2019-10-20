# -*- coding: utf-8 -*-
"""
    Código fuente de ejemplos y ejercicios del libro
    "Curso de Programación Python"
    (C) Ediciones Anaya Multimedia 2019

    Autores: Arturo Montejo Ráez y Salud María Jiménez Zafra
"""

# NOTA: este código solo es válido en Unix, no en Windows

from subprocess import *
p1 = Popen(["cat", "elquijote.txt"], stdout=PIPE)
p2 = Popen(["tr", '" "', '"\n"'], stdin=p1.stdout, stdout=PIPE)
p3 = Popen(["sort"], stdin=p2.stdout, stdout=PIPE)
p4 = Popen(["uniq", "-c"], stdin=p3.stdout, stdout=PIPE)
p5 = Popen(["sort", "-rn"], stdin=p4.stdout, stdout=PIPE)
p6 = Popen(["head", "-n 10"], stdin=p5.stdout, stdout=PIPE)
p1.stdout.close()
output = p6.communicate()[0].decode('utf-8')
print(output)