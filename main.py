again = input("Welcome to badcalc, type Y or Yes to start, or N or No to exit(y/n) At any time you may exit\n")
while again == "Y" or "Yes" or "y" or "yes":
    import math

    #defines all the numbers inputs and the equations are for a later update
    first_number = input("First Number:")
    second_number = input("Second Number:")
    (multi_ply): input = "multiply"
    (sub_tract): input = "subtract"
    (div_ide): input = "divide"
    (add_ition): input = "addition"
    (square_root_1): input="1st number square root"
    (square_root_2): input="2nd number square root"
    (square_1):input = "First number squared"
    (square_2):input = "Second number squared"
    #does all the eqautions based on input
    (sumsquare1) = int(first_number) * int(first_number)
    square_1: print("The square of the first number is")
    print(sumsquare1)
    (sumsquare2) = int(second_number) * int(second_number)
    square_2: print("The square of the second number is")
    print(sumsquare2)
    (sumsqroot1) = math.sqrt(int(first_number))
    square_root_1: print ("The square root of the first number is")
    print(sumsqroot1)
    (sumsqroot2) = math.sqrt(int(second_number))
    square_root_2: print ("The square root of the second number is")
    print(sumsqroot2)
    (summ) = int(first_number) * int(second_number)
    multi_ply: print("The product is")
    print(summ)
    (sums) = int(first_number) - int(second_number)
    sub_tract: print("The difference is")
    print(sums)
    (sumd) = int(first_number) / int(second_number)
    div_ide: print("The quotient is")
    print(sumd)
    (suma) = int(first_number) + int(second_number)
    add_ition: print("The sum is")
    print(suma)
    again
else:
    def exit():
        exit()



