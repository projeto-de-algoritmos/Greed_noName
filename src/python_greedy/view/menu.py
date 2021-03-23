from python_greedy.scripts.shortest_process import shortest_processing_first
from python_greedy.scripts.earliest_deadline_first import earliest_deadline_first
from python_greedy.scripts.smallest_slack import smallest_slack
from python_greedy.utils.print_result import print_result
from python_greedy.utils.clear import clear
import pygame
import time

def show_menu():
    print(40 * "*" , "ALGORITMOS" , 40 * "*")
    print("1. Shortest Process First")
    print("2. Earliest Deadline Fist")
    print("3. Smallest Slack")
    print("4. Sair")
    print(87 * "*")

def menu_choice():
    print(45 * "*" , "MENU" , 45 * "*")
    print("1. Comparacao dos algoritmos por meio de gráfico")
    print("2. Comparacao dos algoritmos por meio de arquivo csv")
    print("3. Disponibiliza individualmente o print de cada execucao")
    print("4. Sair")
    print(97 * "*")

# def back_menu():
#     keyEvent = pygame.key.get_pressed()
#     if keyEvent[pygame.K_KP_ENTER]:
#         clear()

def sub_menu(_list, costs, deadline):
    sorted_process_list, process_burst_list, waiting_time, execution_time, average_waiting_time, average_execution_time = shortest_processing_first(_list, costs, deadline)
    sorted_list_edf, sorted_deadline_list, waiting_time_edf, execution_time_edf, average_waiting_time_edf, average_execution_time_edf = shortest_processing_first(_list, costs, deadline)
    sorted_list_sms, sorted_diff, waiting_time_sms, execution_time_sms, average_waiting_time_sms, average_execution_time_sms = shortest_processing_first(_list, costs, deadline)

    while True:
        show_menu()
        choice = input("\nEscolha entre [1-4]: ")
        if choice == '1':
            print("Opcao 1 foi escolhida\n")
            print_result("Process",
            "Process size",
            "Waiting Time",
            "Execution time",
            len(_list),
            sorted_process_list,
            process_burst_list,
            waiting_time,
            execution_time,
            average_waiting_time,
            average_execution_time)

        elif choice == '2':
            print("Opcao 2 foi escolhida\n")
            print_result("Process",
            "DeadLine",
            "Waiting Time",
            "Execution time",
            len(_list),
            sorted_list_edf,
            sorted_deadline_list,
            waiting_time_edf,
            execution_time_edf,
            average_waiting_time_edf,
            average_execution_time_edf)

        elif choice == '3':
            print("Opcao 3 foi escolhida\n")
            print_result("Process",
            "Folga",
            "Waiting Time",
            "Execution time",
            len(_list),
            sorted_list_sms,
            sorted_diff,
            waiting_time_sms,
            execution_time_sms,
            average_waiting_time_sms,
            average_execution_time_sms)

        elif choice == '4':
            print("Opcao 4 foi escolhida\n Voltando ao menu principal")
            time.sleep(1)
            break
        else:
            input("Opcao incorreta! Tente novamente!")

