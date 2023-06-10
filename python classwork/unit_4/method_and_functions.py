str = "premprakash"
str2= "somu"
print("length of string is :", len(str))
print("in upper case : " , str.upper())  # upper case means capital latter 
print("in lower case : " , str.lower())  # lower case means small latter 
print("is lower case :" , str.islower())  # it will check that ki kya mera string small latter se bana hua hai 
print("is upper case :" , str.isupper())  # it will check letter of string is capital or not 


string = "             python program   "
print("before removing white space :",string)
print("aftr removing white space :", string.strip())   # strip()

str5 = "1226541"
print("is digit : ", str5.isdigit())        # isdigit()
print("is digit :",str.isdigit())       #  isdigit()

print("is alpha : ", str5.isalpha())     # isalpha()
print("is alpha :",str.isalpha())        # isalpha()

str6 = "   "
str7 = " / "
print("is space :", str6.isspace())     # isspace()
print("is space :", str7.isspace())     # isspace()

 
 # isalnum --> determine that python string consists of alphanumeric characters or not 
str8 = "prem@"
str9 = "prem"
str10 = "prem4567"
print("is alphanumeric:",str8.isalnum())    # isalnum
print("is alphnumeric: ", str9.isalnum())    # isalnum
print("is alphanumeric:",str10.isalnum())   # isalnum
print(str5.isalnum())                       # isalnum

a = "Haidar Nagar"
b = "haidar nagar" 
print("is title cased :",a.istitle())     # istitle
print("is title cased :",b.istitle())     # istitle
print("after titled",b.title())         
 
c = "mynameis"
ok = "HOME"
print("before swapcase :",c)
print("after swapcase:",c.swapcase())
print(ok.swapcase())
print("before capitalized :",c)
print("after capitalized:", c.capitalize())


str = "python programming"
str11 = "python"
str12 = "programming "
print("is starting with:",str.startswith("python"))
print("is starting with:",str.startswith(str11))
print("is starting with:",str.startswith(str12))