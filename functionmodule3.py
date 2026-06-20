from marvellous import Addition, subtraction


def main():
    print("Enter first number")
    value1 = int(input())
    value2 = int(input("Enter second number\n"))

    ret = Addition(value1, value2)
    print("Addition is", ret)
    ret = subtraction(value1, value2)
    print("Subtraction is", ret)

if __name__ == "__main__":
    main()