def bubble_sort(burst_list, _list):
    elements = len(burst_list)-1
    _sorted = False
    while not _sorted:
        _sorted = True
        for index in range(elements):
            if burst_list[index] > burst_list[index + 1]:
                burst_list[index], burst_list[index + 1] = burst_list[index + 1], burst_list[index]
                _list[index], _list[index + 1] = burst_list[index + 1], burst_list[index]
                _sorted = False
    return burst_list, _list