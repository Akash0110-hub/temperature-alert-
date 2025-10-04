# Simple Interest Calculator

# Input values
P = float(input("Enter the Principal amount: "))
R = float(input("Enter the Rate of Interest: "))
T = float(input("Enter the Time (in years): "))

#calculate the interset
SI = (P*T*R)/100

# Display result
print("The Simple Interest is:", SI)
