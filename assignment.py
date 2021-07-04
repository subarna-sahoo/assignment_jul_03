def get_missing_range(lst, lower, upper):
    temp_missing_range_lst = []
    
    if lst[0]-lower == 1:
        temp_missing_range_lst.append(str(lower+1))
    elif lst[0]-lower > 1:
        temp_missing_range_lst.append(f"{lower+1}->{lst[0]-1}")

    temp_list = lst
   

    for idx, num in enumerate(temp_list):
        if idx < len(temp_list)-1:
            start_num = num
            next_num = temp_list[idx+1]
            # print(start_num, next_num)
            if next_num-start_num == 2:
                temp_missing_range_lst.append(str(start_num+1))
            elif next_num-start_num > 2:
                temp_missing_range_lst.append(f"{start_num+1}->{next_num-1}")
            else:
                pass

        
    if upper - lst[-1] == 1:
        temp_missing_range_lst.append(str(lst[-1]+1))
    elif upper - lst[-1] > 1:
        temp_missing_range_lst.append(f"{lst[-1]+1}->{upper}")

            
    return temp_missing_range_lst






if __name__ == '__main__':

    lst = [0,1,3,50,75]

    print(get_missing_range(lst, lower=0, upper=99))
