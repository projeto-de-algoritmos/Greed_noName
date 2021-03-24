from python_greedy.view.menu import menu_choice
from python_greedy.view.menu import sub_menu
from python_greedy.scripts.shortest_process import shortest_processing_first
from python_greedy.scripts.earliest_deadline_first import earliest_deadline_first
from python_greedy.scripts.smallest_slack import smallest_slack
from python_greedy.utils.plot_graph import plot_graph
from python_greedy.utils.get_csv import get_csv_data
from python_greedy.utils.clear import clear
from python_greedy.utils.generator import randomGenerator
import time
import random
import pandas as pd
import os

def script_select(script, _list, costs, deadline, sort_time, script_name):
    for i in range(1000,1000000, 1000):
        start_timestamp = time.time_ns()
        script(_list, costs, deadline)
        end_timestamp = time.time_ns()
        timestamp = end_timestamp - start_timestamp
        sort_time[script_name][i] = timestamp

if __name__ == '__main__':
    execution = True
    minimizing_lateness_python = {
        'shortest_processing_first': {},
        'earliest_deadline_first':{},
        'smallest_slack': {}
    }

    # minimizing_lateness_python['earliest_deadline_first'].update(minimizing_lateness_python['shortest_processing_first'])
    # minimizing_lateness_python['smallest_slack'].update(minimizing_lateness_python['shortest_processing_first'])
    size_of_process = 1000
    list_of_process = []
    list_of_costs = []
    list_of_deadline = []

    list_of_process = random.sample(range(0, size_of_process * 2), size_of_process)
    list_of_costs = randomGenerator(list_of_costs, size_of_process)
    list_of_deadline = randomGenerator(list_of_deadline, size_of_process)

    while execution:
        menu_choice()
        choice = input("Escolha entre [1-4]: ")
        if choice == '1':
            print("Opcao 1 foi escolhida\n")
            script_select(shortest_processing_first, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'shortest_processing_first')
            script_select(earliest_deadline_first, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'earliest_deadline_first')
            script_select(smallest_slack, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'smallest_slack')
            plot_graph('results_python.csv')
        elif choice == '2':
            clear()
            print("Opcao 2 foi escolhida\n")
            script_select(shortest_processing_first, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'shortest_processing_first')
            script_select(earliest_deadline_first, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'earliest_deadline_first')
            script_select(smallest_slack, list_of_process, list_of_costs, list_of_deadline, minimizing_lateness_python, 'smallest_slack')
            get_csv_data(minimizing_lateness_python, 'python')
            clear()
        elif choice == '3':
            print("Opcao 3 foi escolhida\n")
            clear()
            sub_menu(list_of_process, list_of_costs, list_of_deadline)
            clear()
        elif choice == '4':
            print("Opcao 4 foi escolhida\n Finalizando execucao!")
            time.sleep(1)
            execution = False
        else:
            input("Opcao incorreta! Tente novamente!")