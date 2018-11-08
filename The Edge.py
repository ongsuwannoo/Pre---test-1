""" The Edge """
def main():
    """ input number 1-5 """
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    num4 = float(input())
    num5 = float(input())
    numall = num1 + num2 + num3 + num4 + num5
    nummax = max(num1, num2, num3, num4, num5)
    nummin = min(num1, num2, num3, num4, num5)
    print("Total: %.2f THB\nMaximum: %.2f THB\nMinimum: %.2f THB\nAverage: %.2f THB"%\
        (numall, nummax, nummin, numall / 5))
main()
