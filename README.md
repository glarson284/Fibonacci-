Fibonacci-
==========

Euler Project - Problem 2

print "Fibonacci Sequence"
my_list = [x for x in range(1,11)]
fib_list = []
fib = 0
for x in my_list:
  if (my_list[index] % 3 == 0):
    fib = my_list[index-2] + my_list[index-1]
    fib_list.append(fib)
    print fib_list
    #add every third index to the list
  else: 
    fib_list.append(x)
    print fib_list
    
