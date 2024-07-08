# Question :01
# for i in range(11):
#     print(i)
    
    
# Question :02
# i = 20
# while i >= 0:
#     print(i)
#     i = i-1

# Question :03
# for i in range(11):
#     if i %2 == 0:
#         print(i)

# Question :04
# num = int(input('Enter a Number'))
# for i in range(1 , num +1 ):
#     print(i)
    
    
# Question :05
# num = int(input('Enter a Number'))
# for i in range(1 , num +1 ):
#     if i % 2 != 0:
#         print(i)


# Question :06
# for i in range(5):
#     print('Happy Birthday') 


# Question :07
# num = int(input('Enter a number: '))
# for i in range(1, num + 1):
#     print(i * i, end=' ')


# Question :08
# num = int(input('Enter a number'))
# for i in range(1 , 11):
#     print(num , 'X' , i , '= ' , num*i)

# Question :09
# a = 3
# d = 4
# n = 8
# for i in range(n):
#     term = a + i * d
#     print(term, end=' ')
    
    
# Question :10
# a = 2
# r = 3
# n = 6
# for i in range(n):
#     term = a * (r ** i)
#     print(term, end=' ')

# Question :11
# num = int(input('Enter a number :'))
# sum = 0
# for i in range(num):
#     sum = sum + i
# print('Sum of the number is ' , sum)
    

# Question :12
# num = int(input('Enter a positive integer: '))
# if num > 0:
#     total_sum = 0.0
#     for i in range(1, num + 1):
#         total_sum += 1 / i
#     print(f'The sum of reciprocals from 1 to {num} is: {total_sum:.2f}')
# else:
#     print('Please enter a positive integer.')


# Question :13
# running_total = 0
# for i in range(5):
#     num = int(input('Enter a number: '))
#     running_total += num
# print(f'The final running total is: {running_total}')


# Question :14
# num = int(input('Enter a positive integer: '))
# if num < 0:
#     print('Factorial does not exist for negative numbers.')
# elif num == 0:
#     print('The factorial of 0 is 1.')
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     print(f'The factorial of {num} is {factorial}.')



# Question :15
# base = float(input('Enter the base number: '))
# exponent = int(input('Enter the exponent: '))
# result = 1
# if exponent > 0:
#     for _ in range(exponent):
#         result *= base
# elif exponent < 0:
#     for _ in range(-exponent):
#         result *= base
#     result = 1 / result
# print(f'{base} to the power of {exponent} is: {result}')

