#----------------------practical no4.--------------------#

# print("leap year or nor: ")
# year = int(input("enter year: "))
# if year%4==0 and (year%100!=0 or year%400==0):
#     print("leap year: ")
# else:
#     print("not leap year")


#----------practical n03(c)----------------#

# marks = int(input("enter the marks of student: "))
# if marks>=90:
#     print(f"your grade is A: ")
# elif marks<90 and marks>80:
#     print(f"your grade is B: ")
# elif marks<79 and marks>70:
#     print(f"your grade is C: ")
# elif marks<69 and marks>60:
#     print("your grade is D: ")
# elif marks<59 and marks>50:
#     print("your grade is E: ")
# elif marks<50:
#     print("your grade is D: ")



# def calculate_average():
#     # Read the number of inputs from the user
#     n = int(input("Enter the number of values: "))

#     # Initialize sum variable
#     total_sum = 0

#     # Read n numbers from the user and calculate their sum
#     for i in range(n):
#         num = float(input(f"Enter number {i+1}: "))
#         total_sum += num

#     # Calculate average
#     average = total_sum / n

#     # Print the result
#     print(f"The average of the {n} numbers is: {average:.2f}")

# # Call the function
# calculate_average()

#---------->>>>>>>>> <<<<<<<<<<<<<<<<<<<----------------#
# for i in range(1, 6):
#     for j in range(1, i + 1):
#         print(j, end=' ')
#     print()


# k = 6
# for i in range(1,k+1):
#     print(' '*(k-i)+' *'*i)

    

#---------------------------->>>>>>>>>>>>>>> pettern
# n = int(input("enter the size: "))
# for i in range(1, n+1):     # first the loop starts with 1 and go till the end;
        # print(' ' * (n - i) + '* ' * i)  #in this statement first take space [(*)into] // n-i(-> [6-1]) then it print '*' into * i times (1) in the n is value witch we can get from the user


# Get the number of elements from the user
# n = int(input("Enter the number of elements: "))

# # Initialize a list to store the numbers
# numbers = []

# # Read the numbers from the user
# for i in range(n):
#     num = float(input(f"Enter element {i+1}: "))
#     numbers.append(num)

# # Calculate the average
# average = sum(numbers) / n

# # Print the result
# print(f"The average of the {n} numbers is: {average:.2f}")



# limit = 10000
# perfect_numbers = []

# for num in range(1, limit + 1):
#     sum_divisors = 0
#     for i in range(1, int(num ** 0.5) + 1):
#         if num % i == 0:
#             sum_divisors += i
#             if i != num // i:
#                 sum_divisors += num // i
#     if sum_divisors == 2 * num:
#         perfect_numbers.append(num)

# print("Perfect numbers up to", limit, ":", perfect_numbers)


#--->>>practical no 6 (list and itls operations)<<<<----#

# r_list = [13,32,434,76,32,5]
# print(f"adding elements in list: ")
# r_list.append("romit_17")
# print(f" printing the elements which  are present in list: {r_list}")
# r_list.remove(13)
# print(f" removeing an element from the list : {r_list}")
# print(f" this element having {r_list.count(32)} duplicate values: ")
# for item in range(0,6):
    # print(r_list[item])
# print(f"accesing element :{r_list[0:4]}")
# print("sorting of  list using .sort :")
# r_list.sort()
# print(f"after ssorting lisst: {r_list}")
# r_list.reverse()
# print(f"list after reverssing: {r_list}")
# r_list.index(32)

print("creating a tuple: ")
n = (45,"rohit_sharma",True,1.22)
print(type(n))
# for item in n:
    # print(item)
lis = list(n)
lis.remove(1.22)
# print(lis)
new_tuple = tuple(lis)
print(new_tuple)
