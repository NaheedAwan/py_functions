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
# print(rev_string("apple")) 

# Python function called num_within()
def num_within(x,a,b):
  return x in range(a,b+1)
     
# print(num_within(3,2,4))     
# print(num_within(3,1,3))     
# print(num_within(10,2,5))

# Python function called pascal()

triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)         
