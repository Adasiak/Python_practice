list_of_par = [1, 2, 3, 3, 2, 1, 7, 8, 3]

set_of_list = set(list_of_par)

for i in set_of_list:
    j = list_of_par.count(i)
    if j < 2:
        print(i) 

