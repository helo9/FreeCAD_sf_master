# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Wing.ui'
#
# Created: Sat Mar 10 07:48:22 2012
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_WingDialog(object):
    def setupUi(self, WingDialog):
        WingDialog.setObjectName(_fromUtf8("WingDialog"))
        WingDialog.resize(455, 256)
        WingDialog.setWindowTitle(QtGui.QApplication.translate("WingDialog", "Profilauswahl", None, QtGui.QApplication.UnicodeUTF8))
        WingDialog.setSizeGripEnabled(False)
        WingDialog.setModal(False)
        self.buttonBox = QtGui.QDialogButtonBox(WingDialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 210, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayoutWidget = QtGui.QWidget(WingDialog)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 441, 181))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_aviable = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_aviable.setText(QtGui.QApplication.translate("WingDialog", "vorhanden", None, QtGui.QApplication.UnicodeUTF8))
        self.label_aviable.setObjectName(_fromUtf8("label_aviable"))
        self.verticalLayout.addWidget(self.label_aviable)
        self.list_aviable = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.list_aviable.setObjectName(_fromUtf8("list_aviable"))
        self.verticalLayout.addWidget(self.list_aviable)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.addButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.addButton.setText(QtGui.QApplication.translate("WingDialog", "hinzufügen", None, QtGui.QApplication.UnicodeUTF8))
        self.addButton.setObjectName(_fromUtf8("addButton"))
        self.verticalLayout_2.addWidget(self.addButton)
        self.removeButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.removeButton.setText(QtGui.QApplication.translate("WingDialog", "entfernen", None, QtGui.QApplication.UnicodeUTF8))
        self.removeButton.setObjectName(_fromUtf8("removeButton"))
        self.verticalLayout_2.addWidget(self.removeButton)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_used = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_used.setText(QtGui.QApplication.translate("WingDialog", "verwendet", None, QtGui.QApplication.UnicodeUTF8))
        self.label_used.setObjectName(_fromUtf8("label_used"))
        self.verticalLayout_3.addWidget(self.label_used)
        self.list_used = QtGui.QListWidget(self.horizontalLayoutWidget)
        self.list_used.setObjectName(_fromUtf8("list_used"))
        self.verticalLayout_3.addWidget(self.list_used)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.retranslateUi(WingDialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), WingDialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), WingDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(WingDialog)
        WingDialog.setTabOrder(self.list_aviable, self.addButton)
        WingDialog.setTabOrder(self.addButton, self.buttonBox)
        WingDialog.setTabOrder(self.buttonBox, self.list_used)
        WingDialog.setTabOrder(self.list_used, self.removeButton)

    def retranslateUi(self, WingDialog):
        pass

