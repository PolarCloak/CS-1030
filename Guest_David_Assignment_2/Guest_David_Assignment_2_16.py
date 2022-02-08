"""
CS10300-20766
ID#700714467
David Guest
Assignment #2.16
Due Date: 2/11/2022

Physics: acceleration, calculating average acceleration
"""


# converts change in velocity and time taken into average acceleration
def acceleration(start_velocity, end_velocity, time):
    acceleration_average = (end_velocity - start_velocity) / time
    return acceleration_average


# run my methods starting here
def main(args):
    start_velocity, end_velocity, time = eval(input("Enter v0, v1, and t: "))
    average_accel = acceleration(start_velocity, end_velocity, time)
    print("The average acceleration is {0}.".format(average_accel.__format__(".4f")))


main(0)
