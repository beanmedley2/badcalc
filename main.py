# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('ethan')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import tkinter as tk
window=tk.Tk()
window.title("Ethan's Calculator")
window.geometry("1000x1000")
first_number = input("First Number:")
second_number = input("Second Number:")
(multi_ply): input = "multiply"
(sub_tract): input = "subtract"
(div_ide): input = "divide"
(add_ition): input = "addition"
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
window.mainloop()
