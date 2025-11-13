import os
import json


with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
     tarefas = json.load(arquivo)


barra = f'|{60*'-'}|'

def mostrar_tarefas():
    print(barra)
    for i in range(len(tarefas['tarefas'])):
            print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} - Data: {tarefas['datas'][i]}')

def adicionar_tarefa():
    print(barra)
    tarefa = input('| Nome da tarefa: ')
    data = input('| Data: ')
    tarefas['tarefas'].append(tarefa)
    tarefas['datas'].append(data)

    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
         json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)
    
def remover_tarefa():
    print(barra)
    for i in range(len(tarefas['tarefas'])):
            print(f'| {i+1} - Tarefa: {tarefas['tarefas'][i]} - Data: {tarefas['datas'][i]}')

    id_tarefa = int(input('| Dígite o número da tarefa que deseja remover: '))
    if id_tarefa > 0:
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas['datas'].pop(id_tarefa-1)
        print(f'| Tarefa {tarefa} removida com sucesso!')
    else:
         print('| Índice inválido!')

    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
         json.dump(tarefas, arquivo, indent=4, ensure_ascii=False) 

def menu():
    while True:
        os.system('cls')
        print(barra)
        print('| GERENCIADOR DE TAREFAS')
        print(barra)
        print('| 1- Mostrar tarefas')
        print('| 2- Adicionar tarefas')
        print('| 3- Remover tarefa')
        print('| 4- Sair')
        print(barra)
        try:
            opc = int(input('| Dígite o número da opção desejada: '))
            if opc == 1:
                os.system('cls')
                mostrar_tarefas()
                input('| Aperte ENTER para continuar...')
            elif opc == 2:
                os.system('cls')
                adicionar_tarefa()
                input('| Aperte ENTER para continuar...')
            elif opc == 3:
                os.system('cls')
                remover_tarefa()
                input('| Aperte ENTER para continuar...')
            elif opc == 4:
                print('| Saindo...')
                break
            else:
                print('| Opção inválida!')
                input('| Aperte ENTER para continuar...')
        except:
             print('| Erro! Dígite um número válido!')
             input('| Aperte ENTER para continuar...')

menu()
