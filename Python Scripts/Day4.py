# input , fstring  and Few math calculation
# First input
first_name = input("Provide your first name: ")
last_name = input("Provide your Last name: ")
#print(first_name,last_name)
# state_ment = "Hello Mr./Mss. " + first_name + " " + last_name


#print(state_ment)
# Fstring
#alternative_statement = f"Hello Mr./Mss. {first_name} {last_name}"
#print(alternative_statement)


# Let say

number1 = 105
number2 = 365

# addition
total = number1 + number2
print(total)
# subtraction
diff1 = number1 - number2
diff2 = number2 - number1
print(diff1)
print(diff2)

# multiplication

num1 = 50
num2 = 3
product_ = num1 * num2
print(product_)

# Division
dividend = 365
divisor = 5
quotient = dividend / divisor
print(quotient)
remainder  = dividend % divisor
print(remainder)

#Exponential
#finding the square of 35
square_of_35  = 35**2 # Read it as 35 to the power 2
print(square_of_35)
tenth_power_of_35 = 35 ** 10
print(tenth_power_of_35)


#Let compute Future value of $ 150000 invested today at 15% pa compounding rate.
# For a period of 7 year

"""
fv = pv * (1+r)**n
"""
present_value = 10000
rate = 15
n = 1

fv = present_value * (1+rate/100)**n
print(fv)




