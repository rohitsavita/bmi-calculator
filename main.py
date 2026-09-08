print("BMI Calculator")

W = float(input("Enter your weight in kg: "))

H = float(input("Enter your height in cm: "))

H = H / 100

BMI = W / (H ** 2)

if BMI < 18.5:
    category = "Underweight Unhealthy "

elif BMI >= 18.5 and BMI < 25:
    category = "Healthy good "

elif BMI >= 25 and BMI < 30:
    category = "Overweight bad"
    
else:
    category = "Obesity danger"

print("Your BMI is:", round(BMI, 2))
print("Category:", category)