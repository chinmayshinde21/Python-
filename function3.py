def main():
    print("Enter first number")
    value1 = int(input())
    value2 = int(input("Enter second number\n"))

    ret = Addition(value1, value2)          # error: name 'Addition' is not defined
    print("Addition is", ret)

if __name__ == "__main__":
    main()