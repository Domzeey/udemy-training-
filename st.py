# print('hello' +' '+ 'angela')

# string
# print("Hello"[4])

# interger
# all whole numbers no matter wether they are positive or negetive are called interger
# numbers without decimal placeses - interger
# print(123 + 345 )

#float
# when numbers have decimal places it is called a float
# 3.14159


#boolean

# True
# false



# how to know the data type of your code

# num_char = len(input("whatis your name? "))
# # print("your name has " + num_char + "character")
# print(type(num_char))


# how to convert data type or casting

# num_char = len(input("whatis your name? "))
# new_num_char = str(num_char)
# print("your name has " + new_num_char + " character.")

# a = float(123)
# print(type(a))

# print(70 + float("100.5")) 

# print(str(70) + str(100))





age = input("What is your current age? ")
age_1 = int(age)
years_to_live = int(90)
num_of_days_in_a_year = int(365)
num_of_weeks_in_a_year = int(52)
num_of_months_in_a_year = int(12)

years_remaining_to_live = int(years_to_live - age_1)
days_remaining_to_live = int(num_of_days_in_a_year * years_remaining_to_live)
weeks_remaining_to_live = int(num_of_weeks_in_a_year * years_remaining_to_live)
month_remaining_to_live = int(num_of_months_in_a_year * years_remaining_to_live)

print(f"you have {days_remaining_to_live} days, {weeks_remaining_to_live} weeks, {month_remaining_to_live} months left.")






#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
# print('welcome to the tip calculator!')
# bill = float(input("what was the total bill? $"))
# tip = int(input("what percentage tip would you like to give 10, 12, or 15? "))
# people = int(input("how many people to split the bill? "))

# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
# final_amount = "{:.2f}".format(bill_per_person)
# print(f"Each person should pay: ${final_amount}")


