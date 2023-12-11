import json

def editar_usuario_por_id(identificador, novo_nome=None, novo_sobrenome=None):
    # Carregar dados do arquivo JSON
    try:
        with open('usuarios.json', 'r') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        print("Arquivo 'usuarios.json' não encontrado.")
        return

    # Procurar o usuário pelo ID
    for usuario in dados.get('usuarios', []):
        if usuario['_id'] == identificador:
            # editar o nome ou sobrenome se novos valores foram fornecidos
            if novo_nome is not None:
                usuario['nome'] = novo_nome
            if novo_sobrenome is not None:
                usuario['sobrenome'] = novo_sobrenome

            # Salvar os dados atualizados no arquivo
            with open('usuarios.json', 'w') as arquivo:
                json.dump(dados, arquivo, indent=2)

            print(f"As informações do usuário com ID {identificador} foram editadas com sucesso.")
            print(json.dumps(usuario, indent=2))
            return

    # Se o ID não for encontrado
    print("Usuário não encontrado para o ID:", identificador)

# Entrada do ID
id_a_editar = input("Digite o ID do usuário a ser editado: ")

# Entrada dos novos valores (pode ser vazio se não quiser editar)
novo_nome = input("Digite o novo nome (ou pressione Enter para manter o mesmo): ")
novo_sobrenome = input("Digite o novo sobrenome (ou pressione Enter para manter o mesmo): ")

# Chamar a função para editar o usuário
editar_usuario_por_id(id_a_editar, novo_nome, novo_sobrenome)
