year = 2026

first_name = input("First name: ")
last_name = input("Last name: ")
age = int(input("Age: "))
city = input("City: ")

full_name = first_name + " " + last_name
name_length = len(full_name)
birth_year = year - age

print("==============================")
print(f"  {full_name}, {age}")
print(f"  {city}")
print(f"  Name length: {name_length} characters")
print(f"  Born around: {birth_year}")
print("==============================")