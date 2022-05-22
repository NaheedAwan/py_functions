# def max_num(n):
#     number = 0
#     for i in max_num:
#         if (max_num > number):
#             max_num=num
# print(max_num) 
# max_num  (2,8,6,4)

#  Python function called max_num()
def max_num(a,b,c):
  return max([a,b,c])

# print(max_num(1,2,3))
# print(max_num(100,50,1))
# print(max_num(15,30,2))


# Python function called mult_list()

def mult_list(num):
    # empty string
    if len(num) == 0:
        return 0
    number = num[0]
        # for more than one number
    if len(num) > 1:
        for i in num[1:]:
            number = number*i
    return number             
# print(mult_list([1,2,3]))
# print(mult_list([1,2,3,4]))

# Python function called rev_string()
# myString = "PythonForBeginners"
# reversedString = myString[:: -1]
# print("Original String is:", myString)
# print("Reversed String is:", reversedString)

def rev_string(my_str):
    return my_str[::-1]
print(rev_string("apple")) 
print("Original String is:", rev_string)   