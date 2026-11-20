import random

print("Bem vindo ao Adivinhe o Número!!")

numeroaleatorio = random.randint(1,10)
print("Escolha Seu número entre 1 e 10, você tem direito a 3 tentativas! ")
numeroescolhido = int(input())
tentativas = 1

while numeroescolhido != numeroaleatorio and tentativas < 3:
    print("Você errou!, tente Novamente: ")
    tentativas += 1
    numeroescolhido = int(input())
    
if numeroescolhido == numeroaleatorio:
    print("Parabéns!!, você acertou!!! ")
    print("FIM DE JOGO")

else:
    print("Tentativas acabaram, Seu número Aleatório era: ", numeroaleatorio)
    print("FIM DE JOGO")   







    