#Create a program using maths and f-Strings that tells us how many days, weeks,
# months we have left if we live until 90 years old.
age = int(input("how old are you? "))
rem_years = 90 -age
rem_month = rem_years *12
rem_weeks = rem_month *4
rem_days = rem_weeks *7
print(f"you have {rem_years} years and {rem_month} month and {rem_weeks} weeks and {rem_days} Days")