weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))  # Added a missing colon ":" after "meters" for consistency in input prompts
bmi = weight / (height ** 2)  # Removed the extra closing parenthesis
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are overweight.")
else:
    print("You are obese.")
