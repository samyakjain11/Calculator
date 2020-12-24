# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import matplotlib.pyplot as plt


def basicCalculatorMode():
    print("CALCULATIONS MODE")
    prob = ""
    while prob != "q":
        try:
            print("enter your problem")
            prob = input()
            print(eval(bytes([ord(p) for p in prob])))
        except:
            if prob != "q":
                print("invalid prompt")


def graphingCalculatorMode():
    print("GRAPHING MODE")
    eq, lowerRange, higherRange = "", 0, 0
    while eq != "q":
        try:
            # initializing equation that needs to be graphed
            print("enter equation to graph here")
            eq = input()
            if eq == "q":
                break

            # initializing lower range
            print("enter lower range")
            lowerRange = (input())
            if lowerRange == "q":
                break
            else:
                lowerRange = int(lowerRange)

            # intializing higher range
            print("enter higher range")
            higherRange = (input())
            if higherRange == "q":
                break
            else:
                higherRange = int(higherRange)

            # creating axes
            x = np.array(range(int(lowerRange), int(higherRange)))
            y = eval(bytes([ord(p) for p in eq]))

            # plotting points
            plt.plot(x, y)
            plt.show()



        except:
            print("invalid prompt")


def helpMode():
    print("""
             1. Do not put parenthesis while multiplying
             2. Put 'np." before using any of the numpy functions
             3. h (Help)
             4. q (Quit)
                    """)


def quitMode():
    print("thank you for using my calculator!")
    exit()


def main():
    mode = ""

    while mode != "q":
        print("""
        1. c (Normal Calculator)
        2. g (Graphing Calculator)
        3. h (Help)
        4. q (Quit)
        """)

        mode = input().lower()

        if mode == "c" or mode == "1":
            basicCalculatorMode()
        elif mode == "g" or mode == "2":
            graphingCalculatorMode()
        elif mode == "h" or mode == "3":
            helpMode()
        elif mode == "q" or mode == "4":
            quitMode()
        else:
            print("invalid input, please try again")


# def print_hi(name):
# Use a breakpoint in the code line below to debug your script.
# print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
