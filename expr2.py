# -*- coding: utf-8 -*-
import libtestes as t

correto = 0
incorreto = 0

for valor in range(10):
    A = t.checkMod(valor, 2)
    B = t.checkMod(valor, 3)
    C = t.checkMod(valor, 5)

    testeOriginal     = (A or B or C) and (not A or not B or C)
    testeSimplificado =  True

    print(f'({valor})\nTeste Original: {testeOriginal} \nTeste Simplificado: {testeSimplificado}')

    if(testeOriginal == testeSimplificado):
        print("Correto")
        correto+=1
    else:
        print("Incorreto --- Quebrou")
        incorreto+=1

    print("\n")

print(f'Relatorio: \nCorretos:{correto} \nIncorreto:{incorreto}\nAcerto:{100*correto/(correto+incorreto)}%')


