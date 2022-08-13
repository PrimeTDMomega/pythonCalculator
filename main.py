#for i in range(50):

#Values

while True:
    Question = input("Would you like to use our Simple Calculator Y/N :  ")
    if Question == "Y":
        print("Sure")

        first_number = input("What is your first number:")
        second_number = input("What is your second number:")
        function = input("What calculation would you like perormed:")

        first_number = int(first_number)
        second_number = int(second_number)

        if function == "+":
            print(first_number+second_number)

        if function == "-":
            print(first_number-second_number)

        if function == "*":
            print(first_number*second_number)

        if function == "/":
            print(first_number/second_number)    

    elif Question == "N":
        
        print("Ok")
        break