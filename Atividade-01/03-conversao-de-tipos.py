"""
Conversão de tipos de dados:

    Inteiro: int()
    Texto: str()
    Decimal: float()
    Booleano: bool()
    Lista: list()
    Complexo: complex()
    Dicionário: dic()
    
"""
#Convertendo inteiro para decimal - int() e float():
nota = 4
print(nota) #Imprime: 4

nota_decimal = float(nota)
print(nota_decimal) #Imprime: 4.0

nota1, nota2, nota3 = 6, 8, 9
media = float((nota1 + nota2 + nota3) / 3)
print(media) #Imprime: 7.666667

#Convertendo decimal para inteiro - float() e int():
peso = 53.70
print(peso) #Imprime: 53.7

peso_inteiro = int(peso)
print(peso_inteiro) #Imprime: 53
