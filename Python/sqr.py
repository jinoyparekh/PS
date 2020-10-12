#This is simple program that returns sqr of all real# upto provided num -1

print("This program returns sqr of real# upto provided num -1")
num_l = [] #n_num stores the output in list
num = int(input("Please enter num: "))
assert num >= 0
try:
    for i in range(num):
        n_num = i ** 2
        num_l.append(n_num)
        print(n_num)
except AssertionError:
    print("Please enter valid REAL #")
 
