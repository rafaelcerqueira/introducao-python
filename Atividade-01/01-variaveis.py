#tipos de variáveis em Python:
""" Variáveis e Constantes:
- Variáveis: São espaços na memória que armazenam valores. Para iniciar uma variável, basta atribuir um nome, desde que não seja uma palavra reservada, e um valor. As variáveis são mutáveis, isto é, elas podem ter seus valores alterados.

- Constantes: As consantes também armazenam valores, porém não devem ter seus valores alterados. No entanto, o Python não tem uma palavra reservada para definir uma constante como em outras linguagens: o "const" (em JavaScript) ou "final" (em Java). Para isso, convencionou-se em criar o nome da variável em CAIXA ALTA.
"""

#Exemplo de variável:
name = 'Ash Ketchum'
age = 10

print(name, age) #Imprime: Ash Ketchum 10

#Exemplo de mutabilidade dos valores das variáveis:
name = 'Satoshi'

print(name, age) #Agora a variável "name" contém o valor "Satoshi"; Imprime: Satoshi 10

#--

#Exemplo de constante:
INITIALPOKEMON = "Bulbasaur"

print(INITIALPOKEMON); #Imprime: Bulbasaur

#--

#Boas práticas:

#O padrão de nomes compostos em variáveis é o snake_case:
pokemon_tipo_grama = "Bulbasaur"
pokemon_tipo_agua = "Squirtle"
pokemon_tipo_fogo = "Charmander"

#As variáveis devem ter nomes sugestivos:
melhor_pokemon_inicial = "Treecko"

#Nomes de constantes em CAIXA ALTA:
MELHOR_REGIAO = "Hoenn"

INICIAIS_HOENN = [
    "Treecko",
    "Torchic",
    "Mudkip"
]

INICIAIS_JOHTO = [
    "Totodile",
    "Cyndaquil",
    "Chicorita"
]

