# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 17:31:15 2020

@author: Anu Soneye

Programming Drill 1.1.1 to 1.-.-
"""

class ComplexNumberMath():
    def product(compNum1, compNum2):
        realProductPart = ((compNum1.realNum * compNum2.realNum) - (compNum1.imaginaryNum * compNum2.imaginaryNum))
        imaginaryProductPart = ((compNum1.realNum * compNum2.imaginaryNum) + (compNum1.imaginaryNum * compNum2.realNum))
        return(ComplexNumber(realProductPart, imaginaryProductPart))
    def sum(compNum1, compNum2):
        realSumPart = (compNum1.realNum + compNum2.realNum)
        imaginarySumPart = (compNum1.imaginaryNum + compNum2.imaginaryNum)
        return(ComplexNumber(realSumPart, imaginarySumPart))

class ComplexNumber():
    def __init__(self, realNum, imaginaryNum):
        self.realNum = realNum
        self.imaginaryNum = imaginaryNum
    def print(self):
        print("{0} + {1}i".format(self.realNum, self.imaginaryNum))

num = ComplexNumber(3,1)
num2 = ComplexNumber(3,-1)

ComplexNumberMath.product(num, num2).print()
ComplexNumberMath.sum(num, num2).print()