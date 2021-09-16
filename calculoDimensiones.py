'''
    Copyright (C) 2021 Luis Trejo

    This file is part of fixedfixedBeamCalc.
    fixedfixedBeamCalc is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    fixedfixedBeamCalc is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with fixedfixedBeamCalc.  If not, see <https://www.gnu.org/licenses/>.'''

import numpy as np
import math
from decimal import *

class FixFixBeams:
    def __init__(self,grosor=0,minStress=0, maxStress=0,E=0, numPoints=0) -> None:
        self.grosor=grosor
        self.minStress=minStress
        self.maxStress=maxStress
        self.numPoints=numPoints
        self.E = Decimal(E)

    def setGrosor(self,grosor):
        self.grosor=Decimal(grosor)

    def setMinStress(self,minStress):
        self.minStress=minStress

    def setMaxStress(self,maxStress):
        self.maxStress=maxStress

    def setE(self,E):
        self.E=Decimal(E)

    def setNumPoints(self,numPoints):
        self.numPoints=numPoints

    def len_resStress(self,resStress): 
        length = (((self.E*Decimal(math.pi)**Decimal(2))/(Decimal(3)*resStress))**(Decimal(0.5)))*self.grosor
        return length

    def getArrayStresses(self) -> list:
        arrayStresses= np.asarray([ point for point in np.linspace(self.maxStress,self.minStress,self.numPoints,dtype=np.integer)])
        return arrayStresses
    
    def getArrayLengths(self) -> list:
        Stresses = self.getArrayStresses()
        arrayLengths = np.asarray([self.len_resStress(resStress=Stress) for Stress in Stresses ])
        return arrayLengths

if __name__ == '__main__':
    obj = FixFixBeams(450E-9,5E6,50E6,134E9,8)
    arregloStresses=obj.getArrayStresses()
    arreglo = obj.getArrayLengths()
    print(arregloStresses)
    print(arreglo)