import random
tentativas = 4
numero_sorteado = random.randint(1, 15)
print(numero_sorteado)
def get_input():
    while True:
        try:
            print("Você tem:", tentativas, "tentativas!")
            numero = int(input("Digite um número: "))
        except ValueError as err:
            print("Valor inválido!")
            continue        
        
        if  1 <= numero <= 15:
            return numero
        
        print("Número inválido, tente um número no intervalo de 1 e 15.")

def check_numbers(numero, numero_sorteio):
    if numero == numero_sorteio:
        print("Parabéns você acertou!!!")
        return True
    
    elif numero > numero_sorteio:
        print("O número sorteado é menor!")
        return False
    elif numero < numero_sorteio:
        print("O número sorteado é maior!")
        return False

for i in range(3):
    tentativas -= 1
    numero_usuario = get_input()
    if check_numbers(numero_sorteio=numero_sorteado, numero=numero_usuario):
        break
    
else:
    print("Suas tentativas acabaram :(")

    

