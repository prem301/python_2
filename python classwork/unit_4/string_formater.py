# string_formater

city = "pune"
country = "india"

print("city",city,"country",country)
  
#string_formater : f- strings  method
print(f"i study in {city}")

# string_formater : format() method

print("i love  {str}".format(str = "python programming"))

# string_formater : % method
name = "prem prakash"
roll_number =  11

print("my name is %s and my roll number is %d" %(name,roll_number) )


# string_formater : template



from string import Template
str = Template('you are $name and your roll number is $num')
str1 = str.substitute(name = "prem prakash" , num = "eleven")
print(str1)

