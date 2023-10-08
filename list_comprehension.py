"""
# procedurally generate lists that contain all permutations of
    # 0 to x
    # 0 to y
    # 0 to z
    master_list = []
    for x_num in range(0, x):
        for y_num in range(0, y):
            for z_num in range(0, z):
                master_list.append([x_num, y_num, z_num])
    
    # use list comprehension to add the integers within each list
    
    # remove lists whose sum equate to n
    
    # add the remaining lists to a list
    
    # print the list
"""

x = 1
y = 2
z = 3
n = 4


# master_list = [0,0,0]
# for x_num in range(0, x):
#     for y_num in range(0, y):
#         for z_num in range(0, z):
#             master_list.append([x_num, y_num, z_num])


master_list = [[x_num,y_num,z_num] for x_num in range(x) for y_num in range(y) for z_num in range(z)]
master_list_filtered = [i for i in master_list if sum(i) != n]
print("this is master_list\n",master_list)
print("this is master_list_filtered\n",master_list_filtered)
# print(master_list)

# list comprehension format:
# <expression> for <iterable> in <target> [if <condition>]


print(master_list)