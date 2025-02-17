#Principaly use in order to not interrupt the program


while True:

    try:
        number = int(input("Enter a number: "))
        print(1 / number)

    except ZeroDivisionError:
        print("You can't divide by zero")

    except ValueError:
        print("Enter only number")

    except Exception:
        print("Something went wrong")

    finally:
        print("Do some cleanup here")