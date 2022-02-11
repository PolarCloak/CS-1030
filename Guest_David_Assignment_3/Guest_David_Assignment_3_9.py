"""
CS10300-20766
ID#700714467
David Guest
Assignment #3.9
Due Date: 2/25/2022

Payroll
"""


# run my methods starting here
def main(args):
    name = input(f"Enter employee's name: ")
    hours = eval(input(f"Enter number of hours worked in a week: "))
    rate = eval(input(f"Enter hourly pay rate: "))
    federal_tax = eval(input(f"Enter federal tax withholding rate: "))
    state_tax = eval(input(f"Enter state tax withholding rate: "))
    gross_pay = hours * rate
    gross_federal = gross_pay * federal_tax
    gross_state = gross_pay * state_tax
    deductions = gross_state + gross_federal
    net_pay = gross_pay - deductions

    output_string = \
        f"Employee Name: {name}\n" \
        f"\n" \
        f"\n" \
        f"  Hours Worked: {hours:.0f}\n" \
        f"Pay Rate: ${rate:.2f}\n" \
        f"Gross Pay: ${gross_pay:.2f}\n" \
        f"Deductions:\n" \
        f"  Federal Withholding ({federal_tax:.1%}): ${gross_federal:.2f}\n" \
        f"  State Withholding ({state_tax:.1%}): ${gross_state:.2f}\n" \
        f"  Total Deduction: ${deductions:.2f}\n" \
        f"Net Pay: ${net_pay:.2f}\n"

    print(output_string)


main(0)
