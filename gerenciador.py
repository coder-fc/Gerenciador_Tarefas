def adicionar_tarefa(tarefas, nome_tarefa):

    # tarefas: nome da tarefa.
    # completada: indica se a tarefa foi completada.
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return


def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return


def atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome}")
    else:
        print("Tarefa não é valida")
    return


def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        if tarefas[indice_tarefa_ajustado]["completada"]:
            print("Tarefa já concluída anteriormente")
        else:
            tarefas[indice_tarefa_ajustado]["completada"] = True
            print(f"Tarefa {indice_tarefa} concluída")
    else:
        print("Tarefa não é valida")
    return


def deletar_tarefas_completadas(tarefas):

    for tarefa in tarefas:
        if tarefa["completada"]:
            tarefas.remove(tarefa)
    print("Tarefas concluídas deletas com sucesso")
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

    elif escolha == "2":
        ver_tarefas(tarefas)

    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input(
            "Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input(
            "Digite o número da tarefa que concluir: ")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break

print("Programa finalizado")
