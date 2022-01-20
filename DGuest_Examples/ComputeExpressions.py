"""
David Guest
ID#700714467

"""


def compute(num1, num2, num3, num4, num5):
    result = ((num1 + num2 * num3) / (num4 - num5))
    return result


def main(args):
    comp = compute(float(input(":")), float(input("plus :")), float(input("times :")), float(input("all divided by :")),
                   float(input("minus :")))
    print(comp)
    return 0


main(0)
