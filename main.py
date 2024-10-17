string = input("Enter any character:")

str = ("")
for i in string:
    str = i + str

print("Your origanal answer:", string)
print("Your origanal answer reversed:", str)