import datetime

year = int (input ("Enter Car Year: "))
make = input ("Enter Car Make: ")
model = input ("Enter Car Model: ")
mileage = int (input ("Enter Car's Mileage: "))
age = datetime.datetime.now().year - year

maintenance = []

print (f"Your Vehicle is a {year} {make} {model}.\nYour Mileage is: {mileage}.\nYour Vehicle is {age} years old.")

for number in range(2):
    service = input ("Enter Maintenance Item: ")
    service_mileage = int (input ("Enter Mileage Performed: "))
    cost = float (input ("Enter Cost: "))
    maintenance.append ([service, service_mileage, cost])

print (f"Maintenance Records\n{20*"-"}")
for log in maintenance:
    print (f"\nService: {log[0]}\nMileage: {log[1]}\nCost: ${log[2]}")
