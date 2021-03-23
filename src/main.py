from python_greedy.utils._insert import random_insert
from python_greedy.view.menu import menu_choice
from python_greedy.scripts.shortest_process import shortest_processing_first
from python_greedy.utils.clear import clear
import time
import random
import pandas as pd
import subprocess
import os

def script_select(script, _list, sort_time, script_name):
    for i in range(1000,11000, 1000):
        start_timestamp = time.time()
        script(_list)
        end_timestamp = time.time()
        timestamp = end_timestamp - start_timestamp
        sort_time[script_name][i] = timestamp
        random_insert(_list, 100)

if __name__ == '__main__':
    execution = True
    minimizing_lateness_python = {'shortest_processing_first': {1000: 0, 2000: 0,
                  3000: 0, 4000: 0, 5000: 0, 6000: 0,
                  7000: 0, 8000: 0, 9000: 0, 10000: 0},
                  'earliest_deadline_first':{}, 'smallest_slack': {} }
    # minimizing_lateness_python['earliest_deadline_first'].update(minimizing_lateness_python['shortest_processing_first'])
    # minimizing_lateness_python['smallest_slack'].update(minimizing_lateness_python['shortest_processing_first'])
    size_of_process = 1000

    while execution:
        menu_choice()
        choice = input("Escolha entre [1-6]: ")
        if choice == '1':
            clear()
            print("Opcao 1 foi escolhida\n")
            list_process = random.sample(range(0, size_of_process * 2), size_of_process)
            script_select(shortest_processing_first, list_process, minimizing_lateness_python, 'shortest_processing_first')
            # script_select(earliest_deadline_first, list_process, minimizing_lateness_python, 'earliest_deadline_first')
            # seleciona_algoritmo(selection_sort, lista, minimizing_lateness_python, 'smallest_slack')
            # plot_grafico(minimizing_lateness_python, 'python')
            # clear()
        elif execution == '6':
            print("Opcao 6 foi escolhida\n Finalizando execução!")
            time.sleep(1)
            execution = False
        else:
            input("Opcao incorreta! Tente novamente!")