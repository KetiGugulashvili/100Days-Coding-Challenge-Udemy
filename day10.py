# execrise 1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return "Leap"
            else:
                return "Not Leap"
        else:
            return "Leap"
    else:
        return "Not Leap"


def days_in_month(year, month):
    """Enter year and number of month and get the days in month"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == "Not Leap":
        return month_days[month - 1]
    elif is_leap(year) == "Leap":
        month_days[1] = 29
        return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


# exercise 2
def calculator(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    else:
        return "Incorrect operator"


number1 = float(input("What's the first number? "))

while True:
    operator = input("+\n-\n*\n/\nPick an operator: ")
    next_number = float(input("What's the next number? "))
    result = calculator(number1, operator, next_number)
    print(f"{number1} {operator} {next_number} = {result}")

    if input(f"Type 'yes' to continue calculating with {result}, otherwise, type 'no'\n") == "yes":
        number1 = result
    else:
        break
        