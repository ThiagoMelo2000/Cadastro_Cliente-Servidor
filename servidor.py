# Carlos Alberto Dantas Filho - 96883
# Daniel Braz da Silva - 104495
# Gabriel Nunes Zwipp - 107813
# Lukas Gabriel Assis dos Santos - 105242
# Thiago Cunha de Melo - 108040

from socket import *
import sys, json
# coding=UTF-8

host = gethostname()
port = 55551

objeto = dict()
list_accounts = list()

print(f'HOST: {host} , PORT {port}')
serv = socket(AF_INET, SOCK_STREAM)
serv.bind((host, port))
serv.listen(5)

while 1:
    
    con, adr = serv.accept()
    print(f'conectado em {adr}')
        
    opcao = con.recv(1024)
    # nome = con.recv(1024)
    # cpf = con.recv(1024)
    # endereco = con.recv(1024)
            
    if(opcao == b''):
        
        pass
    
    elif(opcao == b'1'):
        #Adicionar
        nome = con.recv(1024)
        cpf = con.recv(1024)
        endereco = con.recv(1024)
        
        a = nome
        b = cpf
        c = endereco
        
        objeto = {
            'Nome': str(a),
            'CPF': str(b),
            'Endereco': str(c)
        }
        
        list_accounts.append(objeto)
            
        try:

            with open('arquivo.json') as arquivo:
                
                cadastro = json.loads(arquivo.read())
                
            cadastro.append(objeto)
            
            with open('arquivo.json', 'w') as arquivo:
                json.dump(cadastro, arquivo, indent=4)
                
        except FileNotFoundError:
            
            with open('arquivo.json', 'w', encoding='utf-8') as arquivo:
                
                json.dump(list_accounts, arquivo, indent=4)

        con.sendall(("Usuário Cadastrado").encode('utf-8'))
        
    elif(opcao == b'2'):

        #Remover
                    
        nome = con.recv(1024)
        
        a = str(nome)
        
        try:

            with open('arquivo.json') as arquivo:
                
                cadastro = json.loads(arquivo.read())
                
            for item in range(len(cadastro)):
                
                if(a == cadastro[item]['Nome']):
                    
                    cadastro.pop(item)
                    
                    with open('arquivo.json', 'w') as arquivo:
                        
                        json.dump(cadastro, arquivo, indent=4)
                        
                    con.sendall(("Usuário deletado").encode('utf-8'))
                    
                else:
                    pass
                
        except FileNotFoundError:
            
            con.sendall(("Nenhum usuário cadastrado").encode('utf-8'))
        
    elif(opcao == b'3'):

        #Consultar
        
        nome = con.recv(1024)
        
        a = str(nome)
        
        try:

            with open('arquivo.json') as arquivo:
                
                cadastro = json.loads(arquivo.read())
                
            for item in cadastro:
                
                if(a == item['Nome']):
                    
                    con.sendall(f' Nome: {item["Nome"]} '.encode('utf-8'))
                    con.sendall(f' CPF: {item["CPF"]} '.encode('utf-8'))
                    con.sendall(f' Endereço: {item["Endereco"]} '.encode('utf-8'))
                    
                else:
                    pass
                
        except FileNotFoundError:
            
            print('Nenhum usuário cadastrado')
            con.sendall(("Nenhum usuário cadastrado").encode('utf-8'))
        
    else:
        
        con.sendall(str("Opção inválida").encode('utf-8'))
