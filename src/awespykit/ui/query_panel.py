# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'query_panel.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_query_panel(object):
    def setupUi(self, query_panel):
        query_panel.setObjectName("query_panel")
        query_panel.setWindowModality(QtCore.Qt.WindowModal)
        query_panel.resize(330, 330)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei UI")
        query_panel.setFont(font)
        self.centralwidget = QtWidgets.QWidget(query_panel)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(8, 8, 8, 8)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.uiLineEdit_input_name = QtWidgets.QLineEdit(self.centralwidget)
        self.uiLineEdit_input_name.setObjectName("uiLineEdit_input_name")
        self.horizontalLayout.addWidget(self.uiLineEdit_input_name)
        self.uiPushButton_query = QtWidgets.QPushButton(self.centralwidget)
        self.uiPushButton_query.setObjectName("uiPushButton_query")
        self.horizontalLayout.addWidget(self.uiPushButton_query)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.uiRadioButton_pkg2import = QtWidgets.QRadioButton(self.centralwidget)
        self.uiRadioButton_pkg2import.setChecked(True)
        self.uiRadioButton_pkg2import.setObjectName("uiRadioButton_pkg2import")
        self.horizontalLayout_2.addWidget(self.uiRadioButton_pkg2import)
        self.uiRadioButton_import2pkg = QtWidgets.QRadioButton(self.centralwidget)
        self.uiRadioButton_import2pkg.setObjectName("uiRadioButton_import2pkg")
        self.horizontalLayout_2.addWidget(self.uiRadioButton_import2pkg)
        self.uiCheckBox_case_sensitive = QtWidgets.QCheckBox(self.centralwidget)
        self.uiCheckBox_case_sensitive.setObjectName("uiCheckBox_case_sensitive")
        self.horizontalLayout_2.addWidget(self.uiCheckBox_case_sensitive)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.uiLabel_query_environ = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel_query_environ.setFrameShape(QtWidgets.QFrame.Box)
        self.uiLabel_query_environ.setObjectName("uiLabel_query_environ")
        self.verticalLayout_2.addWidget(self.uiLabel_query_environ)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.uiLabel_query_result = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel_query_result.setObjectName("uiLabel_query_result")
        self.verticalLayout.addWidget(self.uiLabel_query_result)
        self.uiPlainTextEdit_query_result = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.uiPlainTextEdit_query_result.setObjectName("uiPlainTextEdit_query_result")
        self.verticalLayout.addWidget(self.uiPlainTextEdit_query_result)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        query_panel.setCentralWidget(self.centralwidget)

        self.retranslateUi(query_panel)
        QtCore.QMetaObject.connectSlotsByName(query_panel)

    def retranslateUi(self, query_panel):
        _translate = QtCore.QCoreApplication.translate
        query_panel.setWindowTitle(_translate("query_panel", "查询面板"))
        self.uiPushButton_query.setText(_translate("query_panel", "查询"))
        self.uiRadioButton_pkg2import.setText(_translate("query_panel", "以包名查导入名"))
        self.uiRadioButton_import2pkg.setText(_translate("query_panel", "以导入名查包名"))
        self.uiCheckBox_case_sensitive.setText(_translate("query_panel", "区分大小写"))
        self.label.setText(_translate("query_panel", "查询环境："))
        self.uiLabel_query_environ.setText(_translate("query_panel", "未设置任何环境！"))
        self.uiLabel_query_result.setText(_translate("query_panel", "查询结果："))
