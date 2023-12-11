import json
import random
import string

def gerar_id():
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(10))

def adicionar_usuario():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    idade = int(input("Digite a idade: "))
    curso = input("Digite o curso: ")
    instituicao = input("Digite a instituição: ")

    usuario = {
        'nome': nome,
        'sobrenome': sobrenome,
        'idade': idade,
        'curso': curso,
        'instituicao': instituicao,
        '_id': gerar_id()
    }

    # Carregar dados existentes ou inicializar se não existirem
    try:
        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        dados = {'quantidade': 0, 'usuarios': []}

    # Verificar se o ID já existe
    while any(u['_id'] == usuario['_id'] for u in dados['usuarios']):
        usuario['_id'] = gerar_id()

    # Adicionar o novo usuário
    dados['quantidade'] += 1
    dados['usuarios'].append(usuario)

    # Salvar os dados atualizados no arquivo
    with open('usuarios.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=2)

    print("Usuário adicionado com sucesso.")

# Chamar a função para adicionar um novo usuário
adicionar_usuario()