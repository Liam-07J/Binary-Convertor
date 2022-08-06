def binaryConvertor(number):
    print("Converting " + number + " to decimal")
    # check that the only characters are 0 and 1
    for char in number:
        if char != "0" and char != "1":
            return "Invalid input"
    # convert number to an array for easier manipulation
    number = list(number)
    number.reverse()

    # find place value of the digits
    answer = 0
    for x in range(len(number)):
        answer += int(number[x]) * 2 ** x
    return answer

def decimalConvertor(number):
    print("Converting " + number + " to binary")
    number = int(number)
    binary = ""
    currentPlaceValue = 65536
    while True:
        if currentPlaceValue ==0.5:
            break
        if number >= currentPlaceValue:
            number = number - currentPlaceValue
            currentPlaceValue = currentPlaceValue / 2
            binary += "1"
        elif number < currentPlaceValue:  # Can number fit into the current place value?
            # half current place value
            currentPlaceValue = currentPlaceValue / 2
            binary += "0"
    return binary

BinaryOrDecimal = input("Do you have a decimal or a binary number? ")
number = input("What is your " + BinaryOrDecimal + " number?")
if BinaryOrDecimal == "binary":
    print(binaryConvertor(number))
elif BinaryOrDecimal == "decimal":
    print(decimalConvertor(number))
else:
    print("Invalid input,must choice between a binary or decimal number, please re-run program")