# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RibbedWing.ui'
#
# Created: Tue Mar 13 21:18:10 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_RibbedWingDialog(object):
    def setupUi(self, RibbedWingDialog):
        RibbedWingDialog.setObjectName(_fromUtf8("RibbedWingDialog"))
        RibbedWingDialog.resize(216, 167)
        RibbedWingDialog.setWindowTitle(QtGui.QApplication.translate("RibbedWingDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(RibbedWingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 191, 31))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayoutWidget = QtGui.QWidget(RibbedWingDialog)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(9, 19, 201, 108))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.RibNumberLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.RibNumberLabel.setText(QtGui.QApplication.translate("RibbedWingDialog", "Number of Ribs", None, QtGui.QApplication.UnicodeUTF8))
        self.RibNumberLabel.setObjectName(_fromUtf8("RibNumberLabel"))
        self.gridLayout.addWidget(self.RibNumberLabel, 0, 0, 1, 1)
        self.RibThicknessLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.RibThicknessLabel.setText(QtGui.QApplication.translate("RibbedWingDialog", "RibThickness", None, QtGui.QApplication.UnicodeUTF8))
        self.RibThicknessLabel.setObjectName(_fromUtf8("RibThicknessLabel"))
        self.gridLayout.addWidget(self.RibThicknessLabel, 3, 0, 1, 1)
        self.ThicknessSpin = QtGui.QDoubleSpinBox(self.gridLayoutWidget)
        self.ThicknessSpin.setObjectName(_fromUtf8("ThicknessSpin"))
        self.gridLayout.addWidget(self.ThicknessSpin, 5, 0, 1, 1)
        self.RibNumberSpin = QtGui.QSpinBox(self.gridLayoutWidget)
        self.RibNumberSpin.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.RibNumberSpin.setObjectName(_fromUtf8("RibNumberSpin"))
        self.gridLayout.addWidget(self.RibNumberSpin, 1, 0, 1, 1)

        self.retranslateUi(RibbedWingDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), RibbedWingDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), RibbedWingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(RibbedWingDialog)
        RibbedWingDialog.setTabOrder(self.RibNumberSpin, self.ThicknessSpin)
        RibbedWingDialog.setTabOrder(self.ThicknessSpin, self.buttonBox)

    def retranslateUi(self, RibbedWingDialog):
        pass

