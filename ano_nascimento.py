#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if ano >= 1922 and ano <= 2021:
                return ano
            else:
                print("Ano inválido. Por favor, digite um ano entre 1922 e 2021.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

nome = input("Digite seu nome completo: ")
ano_nascimento = obter_ano_nascimento() 
ano_atual = 2024
idade = ano_atual - ano_nascimento

print(f"{nome}, você completou ou completará {idade} anos em {ano_atual}.")