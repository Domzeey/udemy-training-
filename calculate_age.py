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



# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, leap years have 366, with an extra day in February. The reason why we have leap years is really fascinating, this video does it more justice:
# This is how you work out whether if a particular year is a leap year.
# on every year that is evenly divisible by 4 
# **except** every year that is evenly divisible by 100 
# **unless** the year is also evenly divisible by 400
# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)




#soluion
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")



print("Welcome to the rollercoaster!")
height = int(input("what is your height in cm? "))
bill = 0

if height >= 120:
    print("you can ride the rollercoaster!")
    age = int(input("whta is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth ticket are $7.")
    else:
        bill = 12
        print("Adult ticket are $12.")
    
    wants_photo = input("Do you want a photo taken? Y OR N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")
       
else:
    print("sorry, you have to grow taller before you can ride.")

