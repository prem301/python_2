#There is also a method called get() that will give the same result.
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
#Get the value of the "model" key:

x = car.get("model")
print(x)

y = car.keys()
print(y)

car.update({"year":2020})

print(car)