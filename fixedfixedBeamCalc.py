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

import decimal
import sys
from PyQt5 import uic
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QApplication, QFileDialog
from PyQt5.QtWidgets import QMessageBox
import pygame
from calculoDimensiones import FixFixBeams
from decimal import *
import pandas as pd

class app_gui(QMainWindow):

    def __init__(self,calcFixFix):
        super().__init__()
        uic.loadUi('FixedFixed.ui',self)
        self.Tbl_longitudes.setColumnWidth(0,80)
        self.Tbl_longitudes.setColumnWidth(1,80)
        self.setFixedSize(400,330)
        self.Btn_calc.clicked.connect(self.getProcessData)
        self.Btn_saveCSV.clicked.connect(self.saveCSV)
        self.calcFixFix=calcFixFix
    
    def getProcessData(self):

        try:
            filmT=sciPrefix.toUm*Decimal(self.Txt_grosor.text())
            stressMinLimit=int(sciPrefix.toMPa*Decimal(self.Txt_stressMinLimit.text()))
            stressMaxLimit=int(sciPrefix.toMPa*Decimal(self.Txt_stressMaxLimit.text()))
            numBeams=int(self.Txt_beamNumber.text())
            YoungMod=sciPrefix.toGPa*Decimal(self.Txt_E.text())

            calcFixFix.setGrosor(filmT)
            calcFixFix.setMinStress(stressMinLimit)
            calcFixFix.setMaxStress(stressMaxLimit)
            calcFixFix.setNumPoints(numBeams)
            calcFixFix.setE(YoungMod)

            self.stressArray=calcFixFix.getArrayStresses()
            self.beamLengths=calcFixFix.getArrayLengths()
            print(self.beamLengths)
            self.loadTable()

        except (ValueError, decimal.DecimalException):
            QMessageBox.warning(self,'Error','Error en el formato de las entradas, corregir')
            print('Error en el formato de las entradas')

        else:
            print('Sin error en las entradas')

    def loadTable(self):
        size = len(self.stressArray)
        self.Tbl_longitudes.setRowCount(size)

        for i in range(0,size):
            beamLen = str(self.beamLengths[i] * Decimal(1E6))
            stress = str(self.stressArray[i] / Decimal(1E6))

            beamLen = QtWidgets.QTableWidgetItem(beamLen)
            stress = QtWidgets.QTableWidgetItem(stress)

            self.Tbl_longitudes.setItem(i,0,beamLen)
            self.Tbl_longitudes.setItem(i,1,stress)
            
    def saveCSV(self):
        #Create Dataframe
        try:
            beamLengths = [str(beamLength*Decimal(1E6)) for beamLength in self.beamLengths] 
            stressArray = [str(stress/Decimal(1E6)) for stress in self.stressArray]
            data = pd.DataFrame({'Longitud_um':beamLengths, 'Esfuerzo_MPa': stressArray})
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","data.csv","CSV Files (*.csv);;Text Files (*.txt)", options=options)
            if fileName:
                data.to_csv(fileName)
        except AttributeError:
            QMessageBox.warning(self,'Error','No hay cosas para guardar')

class sciPrefix:
    toUm = Decimal(1E-6)
    toMPa = Decimal(1E6)
    toGPa = Decimal(1E9)


if __name__ == '__main__':
    #Decimal precision
    getcontext().prec = 8
    #Load of the song
    pygame.init()
    Track = pygame.mixer.music.load(R"Fluoride.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(-1)

    #Creation of the GUI
    app = QApplication(sys.argv)

    #Object to calculate the length of the fixed fixed beams
    calcFixFix = FixFixBeams()
    GUI = app_gui(calcFixFix)
    GUI.show()
    sys.exit(app.exec_())