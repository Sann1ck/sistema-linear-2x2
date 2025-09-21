"""
Sistema Linear 2x2 - Método de Cramer
Formato de entrada (2 linhas):
a b p
c d q
Representa:
ax + by = p
cx + dy = q
"""

#Leitura da Matriz
# Leitura (aceita números com parte decimal)
M = []
for i in range(2):
    while True:
        try:
            linha = input(f"Digite a, b, p da linha {i+1} (separados por espaços): ")
            partes = list(map(float, linha.strip().split()))
            if len(partes) != 3:
                print("Por favor insira 3 valores: a b p")
                continue
            M.append(partes)
            break
        except ValueError:
            print("Entrada inválida. Tente novamente.")

#Coeficientes
a, b, p = M[0]
c, d, q = M[1]

#Calculo das Determinantes
detA=(a*d)-(c*b)
detAx=(p*d)-(q*b)
detAy=(a*q)-(c*p)

#Se a Determinante da Matriz do Sistema for diferente de 0, então o problema tem somente uma Solução
if detA!=0:
    x=detAx/detA
    y=detAy/detA


    if (a*x)+(b*y)==p and (c*x)+(d*y)==q:
        print(f'\nSolução: x = {x} e y = {y}\nSistema Possível e Determinado (SPD)')

else:
    if detAx==0 and detAy==0:
        print(f'\nSolução: ( x , {p}-{a}x/{b} ) \nSistema Possível e Indeterminado (SPI)')

    elif detAx!=0 or detAy!=0:
        print(f'\nSolução: vazio \nSistema Impossível (SI)')
    

