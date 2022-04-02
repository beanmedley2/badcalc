again = input("Welcome to badcalc, type Y or Yes to start\n")
while again == "Y" or "Yes" or "y" or "yes":
    import math
    how_many_numbers = int(input("How many numbers do you want to add? 2, 3 ,or 4 \n"))
    if how_many_numbers == 2:
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
        #does all the equations based on input
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
    elif how_many_numbers == 3:
        first_number = input("First Number:")
        second_number = input("Second Number:")
        third_number= input ("Third Number:")
        (multi_ply): input = "multiply"
        (sub_tract): input = "subtract"
        (div_ide): input = "divide"
        (add_ition): input = "addition"
        (square_root_1): input="1st number square root"
        (square_root_2): input="2nd number square root"
        (square_1):input = "First number squared"
        (square_2):input = "Second number squared"
        #does all the equations based on input
        (sumsquare1) = int(first_number) * int(first_number)
        square_1: print("The square of the first number is")
        print(sumsquare1)
        (sumsquare2) = int(second_number) * int(second_number)
        square_2: print("The square of the second number is")
        print(sumsquare2)
        (sumsquare3) = int(third_number) * int(third_number)
        square_3: print("The square of the third number is")
        print(sumsquare3)
        (sumsqroot1) = math.sqrt(int(first_number))
        square_root_1: print ("The square root of the first number is")
        print(sumsqroot1)
        (sumsqroot2) = math.sqrt(int(second_number))
        square_root_2: print ("The square root of the second number is")
        print(sumsqroot2)
        (sumsqroot3) = math.sqrt(int(third_number))
        square_root_3: print ("The square root of the third number is")
        print(sumsqroot3)
        (summ) = int(first_number) * int(second_number) * int(third_number)
        multi_ply: print("The product is")
        print(summ)
        (sums) = int(first_number) - int(second_number) - int(third_number)
        sub_tract: print("The difference is")
        print(sums)
        (sumd) = int(first_number) / int(second_number) / int(third_number)
        div_ide: print("The quotient is")
        print(sumd)
        (suma) = int(first_number) + int(second_number) + int(third_number)
        add_ition: print("The sum is")
        print(suma)
        again
    elif how_many_numbers == 4:
        first_number = input("First Number:")
        second_number = input("Second Number:")
        third_number= input ("Third Number:")
        fourth_number= input ("Fourth Number:")
        (multi_ply): input = "multiply"
        (sub_tract): input = "subtract"
        (div_ide): input = "divide"
        (add_ition): input = "addition"
        (square_root_1): input="1st number square root"
        (square_root_2): input="2nd number square root"
        (square_1):input = "First number squared"
        (square_2):input = "Second number squared"
        #does all the equations based on input
        (sumsquare1) = int(first_number) * int(first_number)
        square_1: print("The square of the first number is")
        print(sumsquare1)
        (sumsquare2) = int(second_number) * int(second_number)
        square_2: print("The square of the second number is")
        print(sumsquare2)
        (sumsquare3) = int(third_number) * int(third_number)
        square_3: print("The square of the third number is")
        print(sumsquare3)
        (sumsquare4) = int(fourth_number) * int(fourth_number)
        square_4: print("The square of the fourth number is")
        print(sumsquare4)
        (sumsqroot1) = math.sqrt(int(first_number))
        square_root_1: print ("The square root of the first number is")
        print(sumsqroot1)
        (sumsqroot2) = math.sqrt(int(second_number))
        square_root_2: print ("The square root of the second number is")
        print(sumsqroot2)
        (sumsqroot3) = math.sqrt(int(third_number))
        square_root_3: print ("The square root of the third number is")
        print(sumsqroot3)
        (sumsqroot4) = math.sqrt(int(fourth_number))
        square_root_4: print ("The square root of the fourth number is")
        print(sumsqroot4)
        (summ) = int(first_number) * int(second_number) * int(third_number) * int(fourth_number)
        multi_ply: print("The product is")
        print(summ)
        (sums) = int(first_number) - int(second_number) - int(third_number) - int(fourth_number)
        sub_tract: print("The difference is")
        print(sums)
        (sumd) = int(first_number) / int(second_number) / int(third_number) / int(fourth_number)
        div_ide: print("The quotient is")
        print(sumd)
        (suma) = int(first_number) + int(second_number) + int(third_number) + int(fourth_number)
        add_ition: print("The sum is")
        print(suma)
        again         
else:
    def exit():
        exit()


