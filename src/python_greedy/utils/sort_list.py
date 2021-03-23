def sort_list(_list, burst_list):
    process_burst_list = [process for _,process in sorted(zip(burst_list,_list))]
    return process_burst_list