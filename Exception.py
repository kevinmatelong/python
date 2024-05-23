while True:

    try:
        number : int(input("Please enter a number : "))
        break

    except ValueError:
        print("I said enter a number!!")

    except:
        print("AN unknown error occured")

print ("You entered the number succesfully!")


