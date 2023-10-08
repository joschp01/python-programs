if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    # create a list from the array
    arr_list = [integers for integers in arr]
    # set the maximum number to the first number in the array
    max = arr_list[0]

    # block 1 finds the maximum value in the list

    # iterate through the list
    for i in arr_list:
        # if the iterable is greater than the first number
        # then assign iterable to max
        if max < i:
            max = i
    
    # block 2 finds the second highest number to max
    # when iterating through the list

    # set runner_up to 0
    runner_up = 0
    # iterate through the array list
    for j in arr_list:
        # if iterable is less than the max
        # then set runner_up as j
        if j < max:
            runner_up = j
    
    # block 3 pinpoints the value that is between
    # runner_up and max

    # set count to 0
    count = 0
    # iterate through the array list
    for k in arr_list:
        # if the iterable is between runner_up and k
        # then set runner_up to k, and increase count
        if k >= runner_up and k < max:
            runner_up = k
            count += 1

    # if runner_up did not change
    # then set maximum as the runner_up
    if count < 1:
        runner_up = max

    # print runner_up
    print(runner_up)