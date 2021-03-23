import random
from python_greedy.utils.sort_list import sort_list

def shortest_processing_first(_list, costs, deadline):
    process_burst_list = costs
    process_list = _list
    deadline_list = deadline
    sorted_process_burst_list = []
    size_of_process = len(_list)
    waiting_time = []
    execution_time =[]
    average_waiting_time = 0
    average_execution_time = 0

    # retorna a lista de processos e custos de processos
    # ordenado de acordo com o custo
    sorted_process_list = sort_list(process_list, process_burst_list)

    waiting_time.insert(0, 0)
    execution_time.insert(0, process_burst_list[0])

    for index in range(0,len(process_burst_list)):
        waiting_time.insert(index, waiting_time[index-1] + process_burst_list[index - 1])
        execution_time.insert(index, waiting_time[index] + process_burst_list[index])
        average_waiting_time += waiting_time[index]
        average_execution_time += execution_time[index]

    average_waiting_time = float(average_waiting_time)/size_of_process
    average_execution_time = float(average_execution_time)/size_of_process

    return sorted_process_list, process_burst_list, waiting_time, execution_time, average_waiting_time, average_execution_time