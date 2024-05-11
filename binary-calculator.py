A = ["A", "B", "C", "D"]  # the choose option
Bin = ["0", "1"]  # the base of the binary


def one_comp(onecomp):  # this function that convert binary number to one complement
    for i in range(len(onecomp)):  # use for loop and if condition to change the 0 to 1 and return the result
        if onecomp[i] == "0":
            onecomp[i] = "1"
        else:
            onecomp[i] = "0"
    return onecomp


def two_comp(twocomp):  # this function that convert binary number to two complement
    for i in range(len(twocomp) - 1, -1,
                   -1):  # use for loop to check the binary number from right used len()-1 and the step is -1 to move from right to left.
        if twocomp[
            i] == "1":  # used if condition that if it see first "1" print it and the next all number change it like the one complement.
            for j in range(i - 1, -1, -1):
                if twocomp[j] == "1":
                    twocomp[j] = "0"
                else:
                    twocomp[j] = "1"
            break
    return twocomp


def addition(lnum1):  # this function that make the addition operation
    while True:
        isbin = True
        num2 = input(
            "enter second number")  # take the second binary number from the user as an input to make the addition.
        lnum2 = []  # its the variable that do the make the check and addition
        for i in range(0, len(num2)):
            lnum2.append(num2[i])
            if lnum2[i] not in Bin:
                isbin = False  # its a check step because if the user enter an invalid number
                break
        if isbin:
            break
        else:
            print("Please enter a valid input")

    if len(lnum1) > len(lnum2):
        while len(lnum1) > len(lnum2):  # its a while loop that make the 2 binary numbers equal in length
            lnum2.insert(0, "0")
    else:
        while len(lnum2) > len(lnum1):  # its a while loop that make the 2 binary numbers equal in length
            lnum1.insert(0, "0")

    slnum = []  # its the main variable that used in addition
    if len(lnum1) > len(slnum):
        while len(lnum1) > len(
                slnum):  # the while loop makes slnum equal to the number that taken from the user and all the numbers in slnum = 0 to make the addition
            slnum.insert(0, "0")
    # in this part we will take the number from the right to the left and make addition is the sum = 0 or =1 it will print it
    # if sum equal 2 it will print zero and add 1 to the next number from right to left and if the sum = 3 it will print 1 and add
    # 1 to the next number from right to left
    for i in range(len(slnum) - 1, -1, -1):
        slnum[i] = str(int(lnum1[i]) + int(lnum2[i]))
    for i in range(len(slnum) - 1, -1, -1):
        if slnum[i] == "2":
            if i > 0:
                slnum[i] = "0"
                slnum[i - 1] = str(1 + int(slnum[i - 1]))
            else:
                slnum[i] = "0"
                slnum.insert(0, "1")
        if slnum[i] == "3":
            if i > 0:
                slnum[i] = "1"
                slnum[i - 1] = str(1 + int(slnum[i - 1]))
            else:
                slnum[i] = "1"
                slnum.insert(0, "1")
    return lnum2, slnum


def subtraction(lnum1):  # this function that make the addition operation and two complement to make the subtraction
    while True:
        isbin = True
        num2 = input("enter second number")  # take the second number from the user
        lnum2 = []  # its the main variable in the subtraction
        for i in range(0, len(num2)):
            lnum2.append(num2[i])
            if lnum2[i] not in Bin:  # its the check part if the binary number or not
                isbin = False
                break
        if isbin:
            break
        else:
            print("Please enter a valid input")
    lnum1.insert(0, "0")
    lnum2.insert(0, "0")
    if len(lnum1) > len(lnum2):  # its a while loop that make the 2 binary numbers equal in length
        while len(lnum1) > len(lnum2):
            lnum2.insert(0, "0")
    else:
        while len(lnum2) > len(lnum1):  # its a while loop that make the 2 binary numbers equal in length
            lnum1.insert(0, "0")
    lnum2 = two_comp(lnum2)
    # its the same part from the addition function
    slnum = []
    if len(lnum1) > len(slnum):
        while len(lnum1) > len(slnum):
            slnum.insert(0, "0")

    for i in range(len(slnum) - 1, -1, -1):
        slnum[i] = str(int(lnum1[i]) + int(lnum2[i]))
    for i in range(len(slnum) - 1, -1, -1):
        if slnum[i] == "2":
            if i > 0:
                slnum[i] = "0"
                slnum[i - 1] = str(1 + int(slnum[i - 1]))
            else:
                slnum[i] = "0"

        if slnum[i] == "3":
            if i > 0:
                slnum[i] = "1"
                slnum[i - 1] = str(1 + int(slnum[i - 1]))
            else:
                slnum[i] = "1"
    two_comp(lnum2)  # makes two complement before addition
    return lnum2, slnum  # it returns the second number and the final result


while True:  # we start the program from here
    print("**binary calculator**")
    cont = input("a) start program\n"
                 "b) exit\n")
    if cont.upper() == "B":
        print("Exiting program")
        break
    if cont.upper() not in A[:2]:
        print("Please enter a valid option")
        continue
    while True:
        isbin = True
        num1 = input("Please enter a binary number")
        lnum1 = []
        for i in range(0, len(num1)):
            lnum1.append(num1[i])
            if lnum1[i] not in Bin:
                isbin = False
                break
        if isbin:
            break
        else:
            print("Please enter a valid binary number")

    while True:
        operation = input("**please select the operation**"
                          "\na) Compute one's compliment\n"
                          "b) Compute two's compliment\n"
                          "c) Addition\n"
                          "d) Subtraction\n")
        if operation.upper() in A:
            break
        else:
            print("Please enter a valid option")

    if operation.upper() == "A":
        lnum1 = one_comp(lnum1)
        for i in range(len(lnum1)):
            print(lnum1[i], end="")
        print()

    if operation.upper() == "B":
        lnum1 = two_comp(lnum1)
        for i in range(len(lnum1)):
            print(lnum1[i], end="")
        print()

    if operation.upper() == "C":
        lnum2, slnum = addition(lnum1)
        for i in range(len(lnum1)):
            print(lnum1[i], end="")
        print(" + ", end="")
        for i in range(len(lnum2)):
            print(lnum2[i], end="")
        print(" = ", end="")
        for i in range(len(slnum)):
            print(slnum[i], end="")
        print()

    if operation.upper() == "D":
        lnum2, slnum = subtraction(lnum1)
        for i in range(1, len(lnum1)):
            print(lnum1[i], end="")
        print(" - ", end="")
        for i in range(1, len(lnum2)):
            print(lnum2[i], end="")
        print(" = ", end="")
        for i in range(1, len(slnum)):
            print(slnum[i], end="")
        print(end=" ")
        print("(result in two's complement)")
