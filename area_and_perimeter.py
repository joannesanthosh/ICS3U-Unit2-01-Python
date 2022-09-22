#!/usr/bin/env python3

# Created by: Joanne Santhosh
# Created on: Sept 2022
# This is the Area and Perimeter program for circles

import math


def main():
    # This function calculates the area and perimeter

    print("If a circle has a radius of 15 mm: ")
    print("")
    print("The area is {}mm².".format(math.pi * 15 ** 2))
    print("The perimeter is {}mm.".format(2 * math.pi * 15))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
