"""
CS10300-20766
ID#700714467
David Guest
Class Work
Due Date: N/A


"""
# static variables
LBS_TO_KGS = 0.453592
INCHES_TO_METERS = 0.0254

# prompt to enter: weight and height
lbs = eval(input(f"Enter weight in lbs: "))
feet, inches = eval(input(f"Enter a height in feet, inches: "))
totalInches = feet * 12 + inches

# convert
kgs = lbs * LBS_TO_KGS
meters = totalInches * INCHES_TO_METERS
bmi = kgs / (meters ** 2)

# getting category
status = ""
if bmi <= 18.5:
    status = "Underweight"
elif bmi <= 24.9:
    status = "Healthy"
elif bmi <= 29.9:
    status = "Overweight"
else:
    status = "Obese"

print(f"Your BMI is {bmi:.2f}. You are in the {status} category.")
