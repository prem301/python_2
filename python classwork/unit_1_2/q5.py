x = int(input("enter the size of list to be created"))

my_list=[]

i=1
while i<x:
    m=int(input())
    my_list.append(m)
    i+=1

print(my_list)

print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(len(my_list))
