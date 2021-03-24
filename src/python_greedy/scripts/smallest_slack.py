import random
from python_greedy.utils.sort_list import sort_list

def smallest_slack(_list, costs, deadline):
    process_burst_list = costs
    sorted_process_burst_list = []
    deadline_list = deadline
    sorted_deadline_list = []
    size_of_process = len(_list)
    waiting_time = []
    turn_around_time =[]
    average_waiting_time = 0
    average_turn_around_time = 0
    sorted_diff = []
    sorted_list = _list

    sorted_process_burst_list = sort_list(sorted_list, process_burst_list)
    sorted_deadline_list = sort_list(sorted_process_burst_list, deadline_list)

    for i in range(0, size_of_process):
        sorted_diff.append(sorted_deadline_list[i] - sorted_process_burst_list[i])

    sorted_diff.sort(reverse=False)

    waiting_time.insert(0, 0)
    turn_around_time.insert(0, sorted_process_burst_list[0])

    for index in range(1,len(sorted_diff)):
        waiting_time.insert(index, waiting_time[index-1] + sorted_diff[index - 1])
        turn_around_time.insert(index, waiting_time[index] + sorted_diff[index])
        average_waiting_time += waiting_time[index]
        average_turn_around_time += turn_around_time[index]

    average_waiting_time = float(average_waiting_time)/size_of_process
    average_turn_around_time = float(average_turn_around_time)/size_of_process

    return sorted_list, sorted_diff, waiting_time, turn_around_time, average_waiting_time, average_turn_around_time
