
# # for triangle in range(11, 1, 1)

# for Francis in range(1, 11, 1):
#     for two in range(10, Francis , -1):
#         print(' ', end = ' ')
#     for three in range(10, Francis, 1):
#         print('$', end = ' ')
#     for four in range(10, Francis, 1):    
#          print('$', end = ' ') #(10, 1, -1):
#     print()


#start - optional value / parameter -default 0 
#stop - required parameter / value
#step - otional value / parameter - default 1

# for i in range(1, 11, 1 ):
#     #for two in range(1, 11, 1):
#     #print(two, end =" ") #123456787910
#     for three in range(10, i, -1):
#         print(y )


# for John in range(1, 11, 1):
#     for one in range(1, John, 1):
#         print('#', end = ' ') #(10, 1, -1):
#     for two in range(John, 10, 1):
#         print('*', end='')
#     print()


for i in range(1, 11, 1):
    for x in range(1, i, 1):
        print('#', end=' ')
    for y in range(1, i, 1):
        print('*', end=' ')
    for z in range(i, 1, -1):
        print('#', end=' ')
    print()
