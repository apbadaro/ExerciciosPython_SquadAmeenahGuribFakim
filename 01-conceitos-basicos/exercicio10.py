nome =  input("Informe seu nome: ")
idade =  input("Informe sua idade: ")
carreira =  input('Você esta em transição de carreira? Informe "S" para sim e "N" para não: ')
profissao = input("Qual a sua profissão atual? ")
lugar = input("Você reside em qual Cidade/Estado? ")
mensagem = input("Deixe uma mensagem para as suas colegas de bootcamp: ")

if (carreira == "N"):
  print(f"Meu nome é {nome}, tenho {idade} anos. Atualmente não estou em transição de carreira e a minha profissão é {profissao}. Moro em {lugar}. Minha mensagem para as meninas do Bootcamp é: {mensagem}")
elif (carreira == "S"):
  print(f"Meu nome é {nome}, tenho {idade} anos. Atualmente estou em transição de carreira e a minha profissão é {profissao}. Moro em {lugar}. Minha mensagem para as meninas do Bootcamp é: {mensagem}")
else:
  print('Informe "S" ou "N" sobre sua carreira para que a mensagem seja printada corretamente')