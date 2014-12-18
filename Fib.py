Fibonacci-
Euler Project - Problem 2

print "Fibonacci Sequence" 
fib = [0,1] 
fib2 = [0,1] 
sum = 0 
if sum < 400: 
sum = fib[0] + fib[1] 
fib2.append(sum) 
fib[0] = sum 
sum = fib[0] + fib[1] 
fib2.append(sum) 
fib[1] = sum 
print fib2
