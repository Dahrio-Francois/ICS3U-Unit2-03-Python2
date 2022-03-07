#!/usr/bin/env python3

# Created by: Dahrio Francois
# Created on: March 2022
# This program calculates the circumference of a circle
#   with user inputted radius


import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter the radius of the circle (mm): "))

    # process
    circumference = constants.TAU * radius

    # output
    print("")
    print("Circumference is {0} mm.".format(circumference))
    print("\nDone")


if __name__ == "__main__":
    main()
