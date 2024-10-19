#string from user, sentence, how many words are there?
str = input("Enter what your full name is in a full sentence:")
words = 1
for i in range (len(str)):
    if(str[i] == " " ):
        words = words + 1
print("Total number of Words in this String are :", words)