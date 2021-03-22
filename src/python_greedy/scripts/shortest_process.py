import random
from python_greedy.utils.bubble_sort import bubble_sort

def shortest_processing_first(_list):
    process_burst_list = []
    sorted_process_burst_list = []
    sorted_list = []
    size_of_process = len(_list)
    waiting_time = []
    turn_around_time =[]
    average_waiting_time = 0
    average_turn_around_time = 0


    # o custo de cada processo será dado de forma randomica a fim de podermos ordernar
    for count in range(0, size_of_process):
        process_burst_list.append(random.randint(1, 20))
    # bubble sort
    # retorna a lista de processos e custos de processos
    # ordenado de acordo com o custo
    sorted_process_burst_list, sorted_list = bubble_sort(process_burst_list, _list)

    waiting_time.insert(0, 0)
    turn_around_time.insert(0, sorted_process_burst_list[0])

    for index in range(1,len(sorted_process_burst_list)):
        waiting_time.insert(index, waiting_time[index-1] + sorted_process_burst_list[index - 1])
        turn_around_time.insert(index, waiting_time[index] + sorted_process_burst_list[index])
        average_waiting_time += waiting_time[index]
        average_turn_around_time += turn_around_time[index]

    average_waiting_time = float(average_waiting_time)/size_of_process
    average_turn_around_time = float(average_turn_around_time)/size_of_process

    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for index in range(0, size_of_process):
        print(str(sorted_list[index]) + "\t\t" + str(sorted_process_burst_list[index]) + "\t\t" + str(waiting_time[index])+ "\t\t" + str(turn_around_time[index]))
        print("\n")

    print("Average Waiting time is: "+str(average_waiting_time))
    print("Average Turn Arount Time is: "+str(average_turn_around_time))