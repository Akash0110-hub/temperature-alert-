# temperature_check.py

temp_c = float(input("Enter temperature in Celsius: "))

if temp_c > 30:
    print("It's hot!")
else:
    print("Temperature is normal.")

# temperature_check.py

temp_c = float(input("Enter temperature in Celsius: "))

# Celsius check
if temp_c > 30:
    print("It's hot!")
else:
    print("Temperature is normal.")

# Convert to Fahrenheit
temp_f = (temp_c * 9/5) + 32
print(f"Equivalent Fahrenheit: {temp_f:.2f}°F")