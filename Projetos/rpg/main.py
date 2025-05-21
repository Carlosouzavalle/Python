# nome_usuario = input("Digite seu nome: ")
# print("Bem vindo ao mundo de Rolelia " + nome_usuario)
# print(""" 
#       Breve historia do game
      
#       Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
#       Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, 
#       when an unknown printer took a galley of type and scrambled it to make a type specimen book. 
#       It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. 
#       It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, 
#       and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
#       """)


# sistema de criação de classe
classes_jogaveis = ['Guerreiro', 'Arqueiro', 'Mago', 'Healer']

for i, classe in enumerate(classes_jogaveis, start=1):
    print(f"{i}: {classe}")

escolha = int(input("Digite o número da classe (1 a 4): "))

if 1 <= escolha <= 4:
    print("Você escolheu:", classes_jogaveis[escolha - 1])
else:
    print("Escolha inválida.")