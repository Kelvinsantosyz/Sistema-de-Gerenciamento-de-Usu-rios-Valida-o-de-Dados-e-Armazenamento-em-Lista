def verificar_cpf_repetido(cpf):
    """Verifica se o CPF possui números repetidos."""
    if len(cpf) < 3:
        return False
    for i in range(len(cpf)-2):
        if cpf[i] == cpf[i+1] == cpf[i+2]:
            return True
        
def verificar_existencia_dados(nome, senha, cpf, usuarios):
    """Verifica se algum dos dados já foi cadastrado."""
    for usuario in usuarios:
        if usuario['nome'] == nome or usuario['senha'] == senha or usuario['cpf'] == cpf:
            return True
    return False

def validar_dados(nome, senha, cpf, usuarios):
    """Valida os dados do usuário."""
    if not nome.replace(' ','').isalpha() or len(nome) == 0:
        return False, "Nome inválido"
    
    if senha == nome or senha == senha[0] * len(senha):
        return False, "Senha inválida"
    
    cpf_numeros = ''.join(c for c in cpf if c.isdigit())
    if len(cpf_numeros) != 11:
        return False, "CPF inválido"
        
    if verificar_cpf_repetido(cpf_numeros):
        return False, "CPF inválido: contém números repetidos"
    
    if verificar_existencia_dados(nome, senha, cpf_numeros, usuarios):
        return False, "Dados já cadastrados"
    
    return True, ""

usuarios = []

def armazenar_dados(usuarios):
    """Armazena os dados dos usuários."""
    while True:
        print("Digite uma das opções: ")
        opcao_menu = input("[i]nserir  [s]air: [l]istar: ")
        
        if opcao_menu == "s":
            return "Você saiu do programa"
        
        if opcao_menu =='i':
            
            nome = input("Digite o seu nome: ")
            senha = input("Digite sua senha: ")
            cpf = input("Digite o seu CPF: ")
            
            try:
                valida, erro = validar_dados(nome, senha, cpf, usuarios)
                if valida:
                    if any(usuario['cpf'] == cpf for usuario in usuarios):
                        print("CPF já cadastrado")
                    else:
                        print("Dados válidos")
                        usuario = {
                            "nome": nome,
                            "senha": senha,
                            "cpf": cpf
                        }
                        usuarios.append(usuario)
                        print("Usuário cadastrado:")
                else:
                    print("Dados inválidos:", erro)
        
            except Exception:
                print("Ocorreu erro inesperado, tente novamente")
        
        if opcao_menu =='l':
            for usuario in usuarios:
                print("Lista de usuários:", usuario)

armazenar_dados(usuarios)
