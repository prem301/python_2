s = "welcome to the world of python programming"

# counts each character except space 

char = 0
for i in range(0,len(s)):
    if(s[i] != ' '):
        char = char + 1 

print("the number of character in string are :" , char)

# counts each word 

word = 0
for i in range (0,len(s)):
    if (s[i] == ' '):
        word = word + 1

print("the number of word in string are : " , word + 1)