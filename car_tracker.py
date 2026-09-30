import datetime
year = int (input ("Enter Car Year: "))
make = input ("Enter Car Make: ")
model = input ("Enter Car Model: ")
mileage = input ("Enter Car's Mileage: ")
age = datetime.datetime.now().year - year
print (f"Your Vehicle is a {year} {make} {model}.\nYour Mileage is: {mileage}.\nYour Vehicle is {age} years old.")