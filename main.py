import math as m;
import random as r
from tty import IFLAG;


def anykey():
    import sys
    import termios
    import tty
    # Exibe uma mensagem para o usuário
    print("Pressione qualquer tecla para continuar...")

    # Obtém o descritor de arquivo do stdin
    fd = sys.stdin.fileno()

    # Salva as configurações originais do terminal
    old_settings = termios.tcgetattr(fd)
    try:
        # Altera o modo do terminal para raw, permitindo a leitura de entrada de uma única tecla
        tty.setraw(sys.stdin.fileno())

        # Lê um único caractere do stdin
        sys.stdin.read(1)
    finally:
        # Restaura as configurações originais do terminal
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
def option():
  if conta_BLOCK==False:
    print('(1) CADASTRAR CONTA CORRENTE(já cadastrada)')
    print('(2) DEPOSITAR')
    print('(3) SACAR')
    print('(4) CONSULTAR SALDO')
    print('(5) CONSULTAR EXTRATO')
    print('(6) FINALIZAR')
  elif conta_BLOCK==True :
    print('(1) CADASTRAR CONTA CORRENTE(já cadastrada)')
    print('(2) DEPOSITAR')
    print('(3) SACAR(bloqueado)')
    print('(4) CONSULTAR SALDO(bloqueado)')
    print('(5) CONSULTAR EXTRATO(bloqueado)')
    print('(6) FINALIZAR')
def block_check():
  global conta_BLOCK
  if conta_BLOCK!= False :
    anykey()
    option()
    global opt
    opt=int(input('Digite a opção desejada: '))
def verificar_email(email):
    import re
        # Expressão regular para verificar o formato do email
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'

        # Verificar se o email corresponde ao padrão
    if re.match(padrao, email):
        return True
    else:
        return False
def verificar_senha():
  senha = input('Digite a senha: ')
  a=2
  while senha != senha1:
    if a > 0 :
      print('Senha incorreta!')
      senha = input('Digite a senha: ')
      a-=1      
    else :
      print('Senha incorreta! Conta bloqueada!')
      global conta_BLOCK
      conta_BLOCK = True
      anykey()
      option()
      global opt
      opt=int(input("Digete a opção desejada: "))
      break
      

print('(1) CADASTRAR CONTA CORRENTE')
print('(2) DEPOSITAR')
print('(3) SACAR')
print('(4) CONSULTAR SALDO')
print('(5) CONSULTAR EXTRATO')
print('(6) FINALIZAR')
opt = int(input('Digite a opção desejada: '))
depositos=[]
saques=[]
conta_BLOCK = False
while opt == 1:
  print('MACK BANK – CADASTRO DE CONTA')
  n_conta = m.floor(r.random()*10000)
  while 10000<n_conta and n_conta< 1000:
    n_conta = m.floor(r.random()*10000)
  print(f"O número da conta é: {n_conta}")
  nome = input('Digite o nome do cliente: ')
  while nome == "":
    print("Nome Inválido")
    nome = input('Digite o nome do cliente: ')
  telefone= input('Digite o telefone do cliente:')
  while telefone == "" :
    print("Telefone Inválido")
    telefone= input('Digite o telefone do cliente:')
  email = input('Digite o e-mail do cliente: ')
  while email == "":
    print("E-mail inválido")
    email = input('Digite o e-mail do cliente: ')
  while not verificar_email(email):
    print("O email é inválido.")
    email = input('Digite o e-mail do cliente: ')
    
  saldo = float(input('Digite o saldo inicial: '))
  while saldo < 1000:
    print("O saldo deve ser maior ou igual a R$1000,00")
    saldo = float(input('Digite o saldo novamente: '))
  limite = float(input('Digite o limite de crédito: '))
  while limite < 0 :
    print("Limite de crédito inválido")
    limite = float(input('Digite o limite de crédito novamente: '))
  senha1 = input("Digite a senha: ")
  senha2 = input("Digite novamente a senha: ")

  while senha1 != senha2:
    print("As senha não coincidem")
    senha1 = input("Digite a senha: ")
    senha2 = input("Digite novamente a senha: ")
  while len(senha1) <6 :
    print("A senha deve ter no mínimo 6 caracteres")
    senha1 = input("Digite a senha: ")
    senha2 = input("Digite novamente a senha: ")
  print('Conta cadastrada com sucesso! Precione qualquer tecla para continuar.')
  anykey()
  option()
  opt = int(input('Digite a opção desejada: '))
  while opt == 1:
    print("Você já é cadastrado, por favor selecione outra opção.")
    anykey()
    option()
    opt = int(input('Digite a opção desejada: '))
    
while 1<opt <6:

  
  if opt == 2 :
    print('MACK BANK – DEPÓSITO')
    numero_conta= int(input('Digite o número da conta: '))
    if numero_conta == n_conta:
      print(nome)
      valor = float(input('Digite o valor do depósito: '))
      while valor <= 0:
        print('Valor inválido, o valor deve ser maior que zero!')
        valor = float(input('Digite o valor do depósito: '))
        
      saldo = saldo + valor
      depositos+=[valor]
      
      print(f"O novo saldo é: {saldo:.2f}")
      print('Depósito realizado com sucesso! Precione qualquer tecla para continuar.')
      anykey()
      option()
      opt = int(input('Digite a opção desejada: '))
    else:
      print('Conta não encontrada!')
      anykey()
      

  if conta_BLOCK== False:
    if opt ==3 :
      block_check()
      print('MACK BANK – SAQUE')
      numero_conta= int(input('Digite o número da conta: '))
      if numero_conta == n_conta:
        print(nome)
        verificar_senha()
        if conta_BLOCK==False:
          valor = float(input('Digite o valor do saque: '))
          while valor <=0:
            print('Valor inválido!')
            valor = float(input('Digite o valor do saque: '))
          if valor > saldo:
            print('Saldo insuficiente!')
            sn= input("Você deseja continuar utilizar seu limite de crédito? (s/n)")
            if sn == "s" :
              print("Você está usando seu limite de crédito!")
              valor = float(input('Digite o valor do saque novamente: '))       
              if limite> valor :
                limite-=valor
                print(f"Você tem {limite:.2f} de crédito disponível!" )
                print('Saque realizado com sucesso! Precione qualquer tecla para continuar.')
                anykey()
              else :
                print("Limite de crédito insuficiente!")
                anykey()
                  
            else: 
              anykey()
          saldo = saldo - valor
          saques+=[valor]
          print(f"O novo saldo é: {saldo:.2f}")
          print('Saque realizado com sucesso! Precione qualquer tecla para continuar.')
          anykey()
          option()
          opt = int(input('Digite a opção desejada: '))
    
        elif numero_conta != n_conta:
          print('Conta não encontrada!')
          anykey()
    elif opt == 4:
      block_check()
      print('MACK BANK – CONSULTA DE SALDO')
      numero_conta= int(input('Digite o número da conta: '))
      if numero_conta == n_conta:
        print(nome)
        verificar_senha()
        if conta_BLOCK==False:
          print(f"O saldo atual é: {saldo:.2f}")
          print('Consulta realizada com sucesso! Precione qualquer tecla para continuar.')
          anykey()
          option()
          opt = int(input('Digite a opção desejada: '))
      elif numero_conta != n_conta:
        print('Conta não encontrada!')
        
        anykey()
    
    elif opt==5:
      block_check()
      print('MACK BANK – CONSULTA DE EXTRATO')
      numero_conta= int(input('Digite o número da conta: '))
      if numero_conta == n_conta:
        print(nome)
        verificar_senha()
        if conta_BLOCK ==False:
          print(f"O limite de crédito disponível é: {limite:.2f}")
          print("ÚLTIMAS OPERAÇÕES")
          print("DEPÓSITOS")
          for i in depositos:
            print(f"DEPÓSITO : R${i:.2f} ")
          print("SAQUES")
          for i in saques:
            print(f"SAQUE : R${i:.2f} ")
          if saldo < 0 :
            print("Atenção seu saldo está negativo!")
          print(f"O saldo atual é: {saldo:.2f}")
          print('Consulta realizada com sucesso! Precione qualquer tecla para continuar.')
          anykey()
          option()
          opt = int(input('Digite a opção desejada: '))
      elif numero_conta != n_conta:
        print('Conta não encontrada!')
        anykey()
  else:
    print("Opção indisponível! Conta Bloqueada.")
    anykey()
    option()
    opt=int(input("Digite a opção desejada: "))
  
if opt == 6:
  print('MACK BANK – FINALIZADO')
  print("Este programa foi desenvolvido por: \nTiago de Andrade Reiz \n RA: 10443354")
    
  
    