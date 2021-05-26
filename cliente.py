# Carlos Alberto Dantas Filho - 96883
# Daniel Braz da Silva - 104495
# Gabriel Nunes Zwipp - 107813
# Lukas Gabriel Assis dos Santos - 105242
# Thiago Cunha de Melo - 108040

from socket import *
import sys, os
from time import sleep
# coding=UTF-8

host = gethostname()
port = 55551
cli = socket(AF_INET, SOCK_STREAM)
cli.connect((host, port))

    
opcao = input('1-Cadastrar\n2-Remover\n3-Consultar Clientes\n0-Sair\n')
cli.send(opcao.encode())


if(opcao == '0'):
    
    print("\nFinalizando o cliente...")
    
elif(opcao == '1'):
    
    # cli.send(opcao.encode())
    
    nome = input('Digite seu nome: ')
    cli.send(nome.encode())
    cpf = input("Digite seu CPF: ")
    cli.send(cpf.encode())
    endereco = input("Digite seu endereço: ")
    cli.send(endereco.encode())
    
    retorno = cli.recv(1024)
    
    print(retorno.decode('utf8'))
    
    
elif(opcao == '2'):
    
    # cli.send(opcao.encode())
    
    nome = input('Digite seu nome: ')
    cli.send(nome.encode())
    
    retorno = cli.recv(1024)
    
    print(retorno.decode('utf8'))
    
elif(opcao == '3'):
    
    # cli.send(opcao.encode())
    
    nome = input('Digite seu nome: ')
    cli.send(nome.encode())
    
    retorno_nome = cli.recv(1024)
    retorno_cpf = cli.recv(1024)
    retorno_ender = cli.recv(1024)
    
    print(retorno_nome.decode('utf8'))
    print(retorno_cpf.decode('utf8'))
    print(retorno_ender.decode('utf8'))
    
else:
    
    print('Opção Inválida') 
    sleep(3)
    os.system('clear')