import json

def excluir_usuario_por_id(identificador):
    # Carregar dados do arquivo JSON
    try:
        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'usuarios.json' não encontrado.")
        return

    # Procurar o usuário pelo ID
    usuario_encontrado = None
    for indice, usuario in enumerate(dados.get('usuarios', [])):
        if usuario['_id'] == identificador:
            usuario_encontrado = usuario
            # Remover o usuário da lista
            dados['usuarios'].pop(indice)
            dados['quantidade'] -= 1
            break

    # Exibir o resultado
    if usuario_encontrado:
        # Salvar os dados atualizados no arquivo
        with open('usuarios.json', 'w') as arquivo:
            json.dump(dados, arquivo, indent=2)
        print(f"Usuário com ID {identificador} excluído com sucesso.")
    else:
        print("Usuário não encontrado para o ID:", identificador)

# Entrada do ID
id_a_excluir = input("Digite o ID do usuário a ser excluído: ")

# Chamar a função para excluir o usuário
excluir_usuario_por_id(id_a_excluir)
