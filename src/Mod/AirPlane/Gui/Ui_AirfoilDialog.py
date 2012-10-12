# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Airfoil.ui'
#
# Created: Sun Mar 18 09:47:05 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AirfoilDialog(object):
    def setupUi(self, AirfoilDialog):
        AirfoilDialog.setObjectName(_fromUtf8("AirfoilDialog"))
        AirfoilDialog.resize(402, 230)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(AirfoilDialog.sizePolicy().hasHeightForWidth())
        AirfoilDialog.setSizePolicy(sizePolicy)
        AirfoilDialog.setWindowTitle(QtGui.QApplication.translate("AirfoilDialog", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.buttonBox = QtGui.QDialogButtonBox(AirfoilDialog)
        self.buttonBox.setGeometry(QtCore.QRect(100, 190, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(AirfoilDialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 381, 161))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setText(QtGui.QApplication.translate("AirfoilDialog", "Length", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setText(QtGui.QApplication.translate("AirfoilDialog", "Thickness", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        self.label_4.setText(QtGui.QApplication.translate("AirfoilDialog", "Distance to Root", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.formLayoutWidget)
        self.label_5.setText(QtGui.QApplication.translate("AirfoilDialog", "Distance to Front", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.spin_length = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_length.setDecimals(2)
        self.spin_length.setProperty("value", 1.0)
        self.spin_length.setObjectName(_fromUtf8("spin_length"))
        self.gridLayout.addWidget(self.spin_length, 0, 1, 1, 1)
        self.spin_thickness = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_thickness.setDecimals(2)
        self.spin_thickness.setProperty("value", 1.0)
        self.spin_thickness.setObjectName(_fromUtf8("spin_thickness"))
        self.gridLayout.addWidget(self.spin_thickness, 1, 1, 1, 1)
        self.spin_z = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_z.setDecimals(2)
        self.spin_z.setProperty("value", 1.0)
        self.spin_z.setObjectName(_fromUtf8("spin_z"))
        self.gridLayout.addWidget(self.spin_z, 2, 1, 1, 1)
        self.spin_x = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_x.setDecimals(2)
        self.spin_x.setProperty("value", 1.0)
        self.spin_x.setObjectName(_fromUtf8("spin_x"))
        self.gridLayout.addWidget(self.spin_x, 3, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        self.label_3.setText(QtGui.QApplication.translate("AirfoilDialog", "Distance to Bottom", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.spin_y = QtGui.QDoubleSpinBox(self.formLayoutWidget)
        self.spin_y.setDecimals(2)
        self.spin_y.setProperty("value", 1.0)
        self.spin_y.setObjectName(_fromUtf8("spin_y"))
        self.gridLayout.addWidget(self.spin_y, 4, 1, 1, 1)
        self.label.setBuddy(self.spin_length)
        self.label_2.setBuddy(self.spin_thickness)
        self.label_4.setBuddy(self.spin_z)
        self.label_5.setBuddy(self.spin_x)
        self.label_3.setBuddy(self.spin_y)

        self.retranslateUi(AirfoilDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AirfoilDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AirfoilDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(AirfoilDialog)

    def retranslateUi(self, AirfoilDialog):
        pass

