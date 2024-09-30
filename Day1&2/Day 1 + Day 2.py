#rite a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
#Warning. Do not change the code on lines 1-3. Your program should work for different inputs. e.g. any two-digit number.

Mdigtnumb = input("Type 2 digit number ")
str_data = str(Mdigtnumb)
first_int= int(str_data[0])
second_int= int(str_data[1])
print(first_int+second_int)


