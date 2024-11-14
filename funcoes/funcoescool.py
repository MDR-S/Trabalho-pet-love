import os

usuarios = [['Adm', '1991', 'A']]
pets = []
clientes = []
atendimentos = []
servicos = []

def menu_principal():
   op = int(input('(1) Cadastro\n(2) Atendimento\n(3) Consultas ou Relatorio\\n(4) Logout\n(5) Sairn(\u2605 ) Digite: '))

def menu_cadastro():
    userop = int(input('\n(1) Funcionários (adm)\n(2) Clientes\n(3) Pets\n(4) Serviços (adm)\n(5) Voltar ao Menu Principal\n(\u2605 ) Digite: '))

def menu_usuarios():
    userop = int(input('\n(1) Cadastrar novo Funcionário\n(2) Fazer Login\n(3) Atualizar\n(4) Apagar\n(5) Consultar\n(6) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))

def menu_clientes():
    userop = int(input('\n(1) Cadastrar novo Cliente\n(2) Fazer Login\n(3) Atualizar\n(4) Apagar (adm)\n(5) Consultar\n(6) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))

def menu_pets():
    userop = int(input('\n(1) Cadastrar novo Pet\n(2) Atualizar\n(3) Apagar (adm)\n(4) Consultar\n(5) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))

def menu_servicos():
    userop = int(input('\n(1) Cadastrar novo Serviço (adm)\n(2) Atualizar (adm)\n(3) Apagar (adm)\n(4) Consultar (adm)\n(5) Voltar ao Menu Cadastro\n(\u2605 ) Digite: '))

def menu_atendimento():
    userop = int(input('\n(1) Iniciar\n(2) Agendar\n(3) Remarcar\n(4) Voltar ao Menu Principal\n(\u2605 ) Digite: '))

def menu_consultas():
    userop = int(input('\n(1) Consulta/Relatorio\n(2) Voltar\n\u2605 ) Digite: '))

def erase(): # vai limpar o terminal/cmd pra nn ficar feião kk
    if os.name == 'nt': #linux
        os.system('cls')
    elif os.name == 'posix': #windows
        os.system('clear')

def cadastro_usuarios():
    if len(usuarios) == 0:
        print("Cadastre um novo funcionário, pois não temos nenhum cadastrado.")
        nomeusuario = input("Nome do novo funcionário: ")
        senha = input("Digite a senha: ")
        usuarios.append([nomeusuario, senha, 'A'])  # Adiciona com permissão 'A' (Administrador)
        print("Funcionário cadastrado com sucesso!")
    else:
        nomeusuario = input("Digite o nome do novo funcionário: ")
        senha = input("Digite a senha: ")
        usuarios.append([nomeusuario, senha, 'A'])
        print("Funcionário cadastrado com sucesso!")

def login_usuario():
    while True:
        global usuario_logado, tipo
        nomeusuario = input("Digite o funcionário para login: ")
        senha = input("Digite a senha: ")
        
        for usuario in usuarios:
            if nomeusuario == usuario[0] and senha == usuario[1]:
                usuario_logado = usuario
                tipo = usuario[2]  # Define o tipo conforme o registro do usuário
                print("Funcionário autenticado.")
                return tipo
        # Se não houver correspondência, informa falha no login
        print("Funcionário ou senha inválido!")
        return None

def usuario_atualizar():
    while True:
        if len(usuarios) == 0:
            print("Não há funcionários cadastrados.")
            return
        while True:
            nomeusuario = input("Digite o nome do funcionário para atualizar: ")
            for i in range(len(usuarios)):
                if nomeusuario == usuarios[i][0]:
                    novasenha = input("Digite a nova senha: ")
                    usuarios[i][1] = novasenha 
                    print("Atualização realizada com sucesso!")
                    return True
                else:
                    print("Funcionário não encontrado.")
                    return False

def apagar_usuario():
    if len(usuarios) == 0:
        print("Não há funcionários cadastrados.")
        return 
    while True:
        nomeusuario = input("Digite o nome do funcionário para remove-lo: ")
        for i in range(len(usuarios)):
            if nomeusuario == usuarios[i][0]:
                del usuarios[i]
                print("Funcionário removido com sucesso!")
                return True

def consultar_usuarios():
    if len(usuarios) == 0:
        print("Sem funcionários cadastrados.")
        return
    print("Funcionários cadastrados: ")
    for i in usuarios:
        print(f"Nome: {i[0]}, Senha: {i[1]}, Tipo: {i[2]}")

def cadastrar_pet():
    nomepet = input("Digite o nome do pet: ")
    donocpf = input("Digite o CPF do dono: ")
    especiepet = input("Digite a espécie do pet: ")
    racapet = input("Digite a raça do pet: ")
    
    pets.append([nomepet, donocpf, especiepet, racapet])
    print("Pet cadastrado com sucesso!")

def atualizar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para atualizar: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            novonome = input("Digite o novo nome do pet: ")
            donocpf = input("Digite o novo CPF do dono: ")  
            pets[i] = [novonome, donocpf, pets[i][3], pets[i][4]]
            print("Pet atualizado com sucesso!")
            return
    print("Pet não encontrado.")

def apagar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    nomepet = input("Digite o nome do pet para remover: ")
    for i in range(len(pets)):
        if pets[i][0] == nomepet:
            del pets[i]
            print("Pet removido com sucesso!")
            return
    print("Pet não encontrado.")

def consultar_pet():
    if not pets:
        print("Não há pets cadastrados.")
        return
    else:
        pet = input("Digite o nome do pet para consultar: ")
    
        pet_encontrado = False  
        for pet in pets:  
            if pet == pets[0]:  
                print(f"Nome: {pet[0]}, Dono: {pet[1]}, Espécie: {pet[2]}, Raça: {pet[3]}")
                pet_encontrado = True
                break
        if not pet_encontrado:
            print("Pet não encontrado.")

def iniciar_atendimento():
    if not pets:
        print("Não há pets cadastrados para atendimento.")
        return
    nomepet = input("Digite o nome do pet para iniciar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            servico = input("Digite o serviço prestado: ")
            datatendimento = input("Digite a data do atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, servico, datatendimento])
            print("Atendimento iniciado com sucesso!")
            return
    print("Pet não encontrado.")

def agendar_atendimento():
    if not pets:
        print("Não há pets cadastrados para agendamento.")
        return
    nomepet = input("Digite o nome do pet para agendar o atendimento: ")
    for pet in pets:
        if pet[0] == nomepet:
            dono = pet[1]
            datagendada = input("Digite a data para agendar o atendimento (DD/MM/AAAA): ")
            atendimentos.append([nomepet, dono, "Agendado", datagendada])
            print("Atendimento agendado com sucesso!")
            return
    print("Pet não encontrado.")

def remarcar_atendimento():
    if not atendimentos:
        print("Não há atendimentos agendados.")
        return
    nomepet = input("Digite o nome do pet para remarcar o atendimento: ")
    for atendimento in atendimentos:
        if atendimento[0] == nomepet:
            novadata = input("Digite a nova data para o atendimento (DD/MM/AAAA): ")
            atendimento[3] = novadata
            print("Atendimento remarcado com sucesso!")
            return
    print("Pet não encontrado ou sem atendimentos agendados.")


def consulta_relatorio_1():
    if not atendimentos:
        print("Não há atendimentos registrados.")
        return
    print("Relatório de Todos os Atendimentos:")
    for atendimento in atendimentos:
        print(f"Pet: {atendimento[0]}, Dono: {atendimento[1]}, Serviço: {atendimento[2]}, Data: {atendimento[3]}")

def cadastrar_servico():
    nomeservico = input("Digite o tipo do serviço: ")
    precoservico = float(input("Digite o preço do serviço: "))
    
    servicos.append([nomeservico, precoservico])
    print("Serviço cadastrado com sucesso!")

def atualizar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para atualizar: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            novonome = input("Digite o novo tipo do serviço: ")
            novopreco = float(input("Digite o novo preço do serviço: "))
            servicos[i] = [novonome, novopreco]
            print("Serviço atualizado com sucesso!")
            return
    print("Serviço não encontrado.")

def apagar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    nomeservico = input("Digite o tipo do serviço para remover: ")
    for i in range(len(servicos)):
        if servicos[i][0] == nomeservico:
            del servicos[i]
            print("Serviço removido com sucesso!")
            return
    print("Serviço não encontrado.")

def consultar_servico():
    if not servicos:
        print("Não há serviços cadastrados.")
        return
    for servico in servicos:
        print(f"Tipo do serviço: {servico[0]}, Preço: R$ {servico[1]:.2f}")

def cadastro_clientes():
            
        if len(clientes) == 0:
            print("Não há clientes cadastrados. Cadastre um cliente.")
            
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))

            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")
    
        else:
            nomecliente = input("Digite o nome do novo cliente: ")
            senha = input("Digite a senha: ")
            cpf = int(input("Digite o CPF: "))
            for i in range (len(clientes)):
                if cpf == clientes[i][3]:
                    print("Clinte já registrado! Cadastre um novo!")
                    return False
            clientes.append([nomecliente, senha, 'C', cpf])
            print("Cliente cadastrado com sucesso!")

def login_clientes():
    global usuario_logado, tipo
    while True:
        nomecliente = input("Digite o cliente para login: ")
        senha = input("Digite a senha: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0] and senha == clientes[i][1]:
                usuario_logado = clientes
                tipo = 'C'
                print("Cliente autenticado.")
                return tipo
        else:
            print("Cliente ou senha inválido!")
            return None

def clientes_atualizar():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    while True:
        nomecliente = input("Digite o nome do cliente para atualizar: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                novasenha = input("Digite a nova senha: ")
                clientes[i][1] = novasenha

                print("Atualização realizada com sucesso!")
                return True

            else:
                print("Cliente não encontrado.")

def apagar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return 
    while True:
        nomecliente = input("Digite o nome do cliente para remove-lo: ")
        for i in range(len(clientes)):
            if nomecliente == clientes[i][0]:
                del clientes[i]
                print("Cliente removido com sucesso!")
                return True

def consultar_cliente():
    if len(clientes) == 0:
        print("Não há clientes cadastrados.")
        return
    else:
        senhacliente = input("Digite a senha do cliente para consultar: ")
    
        cliente_encontrado = False
        for cliente in clientes:  
            if senhacliente == cliente[1]:  
                print(f"Nome: {cliente[0]}, Senha: {cliente[1]}, Tipo: {cliente[2]}, CPF: {cliente[3]}")
                cliente_encontrado = True
                break
        if not cliente_encontrado:
            print("Cliente não encontrado.")


# oi professor :D