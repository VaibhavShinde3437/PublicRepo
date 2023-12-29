def main():
    while True:
        print("1. +")
        print("2. -")
        print("3 *")
        print("4. /")
        print("5. Done")
        try:
            n = int(input("Choose : "));
            if n == 5: break
            elif n > 4 : 
                print("Enter a valid choice")
            else:
                a = int(input("First no : "))
                b = int(input("Second no : "))

            match n :
                case 1 : print(addition(a,b));
                case 2 : print(subtract(a,b))
                case 3 : print(multiplication(a,b))
                case 4 : print(divide(a,b))
        except ValueError:
            print("Enter a Number")


def addition(a,b):
    return a + b


def subtract(a,b):
    return a - b

def divide(a,b):
    try:
        return a / b
    except ArithmeticError:
        print("Can't divide by zero")

def multiplication(a,b):
    return a * b


if __name__ == "__main__":
    main()