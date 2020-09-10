# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:31:15 2020

@author: Anu Soneye

Programming Drill 1.1.1 to 1.-.-
"""

import numpy as np
import math

#a = np.array({1,2,3})


class ComplexNumberMath():
    def product(compNum1, compNum2):
        realProductPart = ((compNum1.realNum * compNum2.realNum) - (compNum1.imaginaryNum * compNum2.imaginaryNum))
        imaginaryProductPart = ((compNum1.realNum * compNum2.imaginaryNum) + (compNum1.imaginaryNum * compNum2.realNum))
        return(ComplexNumber(realProductPart, imaginaryProductPart))
    def sum(compNum1, compNum2):
        realSumPart = (compNum1.realNum + compNum2.realNum)
        imaginarySumPart = (compNum1.imaginaryNum + compNum2.imaginaryNum)
        return(ComplexNumber(realSumPart, imaginarySumPart))
    def subtract(compNum1, compNum2):
        realSumPart = (compNum1.realNum - compNum2.realNum)
        imaginarySumPart = (compNum1.imaginaryNum - compNum2.imaginaryNum)
        return(ComplexNumber(realSumPart, imaginarySumPart))
    def divide(compNum1, compNum2):
        realQuotientPart = (((compNum1.realNum * compNum2.realNum) + (compNum1.imaginaryNum * compNum2.imaginaryNum)) / (compNum2.modulus()))
        imaginaryQuotientPart = (((compNum2.realNum * compNum1.imaginaryNum) - (compNum1.realNum * compNum2.imaginaryNum)) / (compNum2.modulus()))
        return(ComplexNumber(realQuotientPart, imaginaryQuotientPart))

class ComplexNumber():
    def __init__(self, realNum, imaginaryNum):
        self.realNum = realNum
        self.imaginaryNum = imaginaryNum
    def modulus(self, squared = False):
        insideSqrt = (self.realNum ** 2) + (self.imaginaryNum ** 2)
        if (squared):
            return(insideSqrt)
        else:      
            return(math.sqrt(insideSqrt))
    def print(self):
        print("{0} + {1}i".format(self.realNum, self.imaginaryNum))

'''
num = ComplexNumber(0,0)
num2 = ComplexNumber(1,0)

ComplexNumberMath.divide(num, num2).print()

'''

print("Create a Complex Number by entering both the imaginary and the real part")
realNum = float(input("Input the value of the real component: "))

imaginaryNum = float(input("Input the value of the imaginary component: "))

complexNum = ComplexNumber(realNum, imaginaryNum)
magnitude = complexNum.modulus(True)
thetaInRadians = math.atan(complexNum.imaginaryNum / complexNum.realNum)
thetaInDegrees = math.atan(1) * (180 / math.pi)

print("Your number was converted from its Cartesian Representation ({0}, {1}) to its Polar representation \n({2}, {3} in radians or {4} in degrees) ". format(complexNum.realNum, complexNum.imaginaryNum, magnitude, thetaInRadians, thetaInDegrees))



