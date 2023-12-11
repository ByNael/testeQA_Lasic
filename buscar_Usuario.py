import json

def buscar_usuario_por_id(identificador):
    # Carregar dados do arquivo JSON
    try:
        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'usuarios.json' não encontrado.")
        return

    # Procurar o usuário pelo ID
    usuario_encontrado = None
    for usuario in dados.get('usuarios', []):
        if usuario['_id'] == identificador:
            usuario_encontrado = usuario
            break

    # Exibir o resultado
    if usuario_encontrado:
        print(json.dumps(usuario_encontrado, indent=2))
    else:
        print("Usuário não encontrado para o ID:", identificador)

# Entrada do ID
id_procurado = input("Digite o ID do usuário: ")

# Chamar a função para buscar o usuário e exibir as informações
buscar_usuario_por_id(id_procurado)
