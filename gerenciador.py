def adicionar_tarefa(tarefas, nome_tarefa):

    # tarefas: nome da tarefa.
    # completada: indica se a tarefa foi completada.
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return


tarefas = []

while True:
    print("\nMenu do Gerenciador de lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefas")
    print("4. Completar tarefa")
    print("5. Deletar tarefa")
    print("6. Sair")

    escolha = input("Digite a opção desejada: ")
    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "6":
        break

print("Programa finalizado")
