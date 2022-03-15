"""
CS10300-20766
ID#700714467
David Guest
Assignment #4.6
Due Date: 4/25/22

Health application: BMI
"""
# static variables
LBS_TO_KGS = 0.453592
INCHES_TO_METERS = 0.0254


# determine the category the BMI falls under
def getCategory(bmi):
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 24.9:
        return "Healthy"
    elif bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"


# run my methods starting here
def main(args):
    # prompt to enter: weight and height
    lbs = eval(input(f"Enter weight in lbs: "))
    feet, inches = eval(input(f"Enter a height in feet, inches: "))
    totalInches = feet * 12 + inches
    # convert
    kgs = lbs * LBS_TO_KGS
    meters = totalInches * INCHES_TO_METERS
    bmi = kgs / (meters ** 2)
    # output the BMI and category
    print(f"Your BMI is {bmi:.2f}.\nYou are in the {getCategory(bmi)} category.")


main(0)
