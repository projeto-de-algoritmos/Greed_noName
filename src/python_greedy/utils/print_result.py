def print_result(
    process_name,
    cost,
    waiting_time,
    execution_time,
    size_process,
    sorted_list,
    cost_list,
    waitin_time_list,
    execution_time_list,
    average_waiting_time,
    average_execution_time):

    print(f"{process_name}\t{cost}\t{waiting_time}\t{execution_time}")
    for index in range(0, size_process):
        print(
            str(sorted_list[index]) + "\t\t"
            + str(cost_list[index]) + "\t\t"
            + str(waitin_time_list[index])+ "\t\t"
            + str(execution_time_list[index]))
        print("\n")

    print("Average Waiting time is: "+str(average_waiting_time))
    print("Average Execution Time is: "+str(average_execution_time))