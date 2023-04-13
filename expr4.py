# -*- coding: utf-8 -*-
import libtestes as t

correto = 0
incorreto = 0

for valor in range(10):
    A = t.checkMod(valor, 2)
    B = t.checkMod(valor, 3)
    C = t.checkMod(valor, 5)
    D = t.checkMod(valor, 7)

    testeOriginal     = not((A or B) and C) or not(D and (C or B))
    testeSimplificado =  True

    print(f'({valor})\nTeste Original: {testeOriginal} \nTeste Simplificado: {testeSimplificado}')

    if(testeOriginal == testeSimplificado):
        print("Correto")
        correto+=1
    else:
        print("Incorreto --- Quebrou")
        incorreto+=1

    print("\n")

print(f'Relatório: \nCorretos:{correto} \nIncorreto:{incorreto}\nAcerto:{100*correto/(correto+incorreto)}%')


