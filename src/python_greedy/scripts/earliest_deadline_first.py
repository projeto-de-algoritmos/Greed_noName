import random
from python_greedy.utils.bubble_sort import bubble_sort

def earliest_deadline_first(_list):
    sorted_list = []
    deadline_list = []
    size_of_process = len(_list)
    waiting_time = []
    average_waiting_time = []
    sorted_deadline_list = []
    turn_around_time =[]
    average_turn_around_time = 0

    for i in range(0, size_of_process):
        sorted_deadline_list.append(random.randint(1,24))

    sorted_list = bubble_sort(sorted_list, _list)
    sorted_deadline_list = bubble_sort(sorted_deadline_list, _list)

    waiting_time.insert(0, 0)

    turn_around_time.insert(0, sorted_deadline_list[0])

    for index in range(1,len(sorted_deadline_list)):
        waiting_time.insert(index, waiting_time[index-1] + sorted_deadline_list[index - 1])
        turn_around_time.insert(index, waiting_time[index] + sorted_deadline_list[index])
        average_waiting_time += waiting_time[index]
        average_turn_around_time += turn_around_time[index]

    average_waiting_time = float(average_waiting_time)/size_of_process
    average_turn_around_time = float(average_turn_around_time)/size_of_process

    print("Process\t  Burst Time\t  Waiting Time\t  Turn Around Time")
    for index in range(0, size_of_process):
        print(str(sorted_list[index]) + "\t\t" + str(sorted_deadline_list[index]) + "\t\t" + str(waiting_time[index])+ "\t\t" + str(turn_around_time[index]))
        print("\n")

    print("Average Waiting time is: "+str(average_waiting_time))
    print("Average Turn Arount Time is: "+str(average_turn_around_time))