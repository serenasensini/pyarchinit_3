# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pyarchinit_Detsesso_ui.ui'
#
# Created: Wed Feb 05 18:20:25 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s


class Ui_DialogDetsesso(object):
    def setupUi(self, DialogDetsesso):
        DialogDetsesso.setObjectName(_fromUtf8("DialogDetsesso"))
        DialogDetsesso.resize(607, 594)
        DialogDetsesso.setMinimumSize(QtCore.QSize(540, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/iconPAI.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DialogDetsesso.setWindowIcon(icon)
        self.gridLayout_6 = QtGui.QGridLayout(DialogDetsesso)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_29 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.gridLayout_2.addWidget(self.label_29, 0, 0, 1, 1)
        self.pushButton_connect = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_connect.setObjectName(_fromUtf8("pushButton_connect"))
        self.gridLayout_2.addWidget(self.pushButton_connect, 0, 1, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.pushButton_first_rec = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_first_rec.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/5_leftArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_first_rec.setIcon(icon1)
        self.pushButton_first_rec.setObjectName(_fromUtf8("pushButton_first_rec"))
        self.gridLayout.addWidget(self.pushButton_first_rec, 0, 5, 1, 1)
        self.pushButton_next_rec = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_next_rec.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/6_rightArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_next_rec.setIcon(icon2)
        self.pushButton_next_rec.setObjectName(_fromUtf8("pushButton_next_rec"))
        self.gridLayout.addWidget(self.pushButton_next_rec, 0, 7, 1, 1)
        self.pushButton_last_rec = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_last_rec.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/7_rightArrows.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_last_rec.setIcon(icon3)
        self.pushButton_last_rec.setObjectName(_fromUtf8("pushButton_last_rec"))
        self.gridLayout.addWidget(self.pushButton_last_rec, 0, 8, 1, 1)
        self.pushButton_new_rec = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_rec.setFont(font)
        self.pushButton_new_rec.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/newrec.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_rec.setIcon(icon4)
        self.pushButton_new_rec.setObjectName(_fromUtf8("pushButton_new_rec"))
        self.gridLayout.addWidget(self.pushButton_new_rec, 0, 9, 1, 1)
        self.pushButton_save = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/b_save.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save.setIcon(icon5)
        self.pushButton_save.setAutoDefault(False)
        self.pushButton_save.setObjectName(_fromUtf8("pushButton_save"))
        self.gridLayout.addWidget(self.pushButton_save, 0, 10, 1, 1)
        self.pushButton_new_search = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_new_search.setFont(font)
        self.pushButton_new_search.setText(_fromUtf8(""))
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/new_search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_new_search.setIcon(icon6)
        self.pushButton_new_search.setObjectName(_fromUtf8("pushButton_new_search"))
        self.gridLayout.addWidget(self.pushButton_new_search, 1, 7, 1, 1)
        self.pushButton_search_go = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_search_go.setFont(font)
        self.pushButton_search_go.setText(_fromUtf8(""))
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/search.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_search_go.setIcon(icon7)
        self.pushButton_search_go.setObjectName(_fromUtf8("pushButton_search_go"))
        self.gridLayout.addWidget(self.pushButton_search_go, 1, 8, 1, 1)
        self.pushButton_sort = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_sort.setFont(font)
        self.pushButton_sort.setText(_fromUtf8(""))
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/sort.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_sort.setIcon(icon8)
        self.pushButton_sort.setObjectName(_fromUtf8("pushButton_sort"))
        self.gridLayout.addWidget(self.pushButton_sort, 1, 9, 1, 1)
        self.pushButton_view_all = QtGui.QPushButton(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_view_all.setFont(font)
        self.pushButton_view_all.setText(_fromUtf8(""))
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/view_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_view_all.setIcon(icon9)
        self.pushButton_view_all.setObjectName(_fromUtf8("pushButton_view_all"))
        self.gridLayout.addWidget(self.pushButton_view_all, 1, 10, 1, 1)
        self.pushButton_delete = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_delete.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pushButton_delete.setFont(font)
        self.pushButton_delete.setText(_fromUtf8(""))
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_delete.setIcon(icon10)
        self.pushButton_delete.setObjectName(_fromUtf8("pushButton_delete"))
        self.gridLayout.addWidget(self.pushButton_delete, 1, 2, 1, 1)
        self.pushButton_prev_rec = QtGui.QPushButton(DialogDetsesso)
        self.pushButton_prev_rec.setText(_fromUtf8(""))
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/4_leftArrow.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_prev_rec.setIcon(icon11)
        self.pushButton_prev_rec.setObjectName(_fromUtf8("pushButton_prev_rec"))
        self.gridLayout.addWidget(self.pushButton_prev_rec, 0, 6, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_2)
        self.line_6 = QtGui.QFrame(DialogDetsesso)
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.horizontalLayout.addWidget(self.line_6)
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_42 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.label_42.setFont(font)
        self.label_42.setAutoFillBackground(True)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.gridLayout_5.addWidget(self.label_42, 0, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.label_43 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_43.setFont(font)
        self.label_43.setMargin(0)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.gridLayout_4.addWidget(self.label_43, 0, 1, 1, 1)
        self.label_status = QtGui.QLabel(DialogDetsesso)
        self.label_status.setMinimumSize(QtCore.QSize(40, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_status.setFont(font)
        self.label_status.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_status.setMouseTracking(False)
        self.label_status.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_status.setFrameShape(QtGui.QFrame.Box)
        self.label_status.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_status.setText(_fromUtf8(""))
        self.label_status.setAlignment(QtCore.Qt.AlignCenter)
        self.label_status.setMargin(0)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.gridLayout_4.addWidget(self.label_status, 1, 0, 1, 1)
        self.label_sort = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.label_sort.setFont(font)
        self.label_sort.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_sort.setMouseTracking(False)
        self.label_sort.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_sort.setFrameShape(QtGui.QFrame.Box)
        self.label_sort.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_sort.setText(_fromUtf8(""))
        self.label_sort.setAlignment(QtCore.Qt.AlignCenter)
        self.label_sort.setMargin(0)
        self.label_sort.setObjectName(_fromUtf8("label_sort"))
        self.gridLayout_4.addWidget(self.label_sort, 1, 1, 1, 1)
        self.label_34 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_34.setFont(font)
        self.label_34.setMargin(0)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout_4.addWidget(self.label_34, 0, 0, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 1, 0, 1, 1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label_27 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_27.setFont(font)
        self.label_27.setMargin(0)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.gridLayout_3.addWidget(self.label_27, 0, 0, 1, 1)
        self.label_rec_corrente = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_corrente.setFont(font)
        self.label_rec_corrente.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_corrente.setMouseTracking(False)
        self.label_rec_corrente.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_corrente.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_corrente.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_corrente.setObjectName(_fromUtf8("label_rec_corrente"))
        self.gridLayout_3.addWidget(self.label_rec_corrente, 0, 1, 1, 1)
        self.label_28 = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setWeight(75)
        font.setBold(True)
        self.label_28.setFont(font)
        self.label_28.setMargin(0)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.gridLayout_3.addWidget(self.label_28, 1, 0, 1, 1)
        self.label_rec_tot = QtGui.QLabel(DialogDetsesso)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Microsoft Sans Serif"))
        font.setPointSize(12)
        self.label_rec_tot.setFont(font)
        self.label_rec_tot.setCursor(QtCore.Qt.ForbiddenCursor)
        self.label_rec_tot.setMouseTracking(False)
        self.label_rec_tot.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_rec_tot.setFrameShape(QtGui.QFrame.Box)
        self.label_rec_tot.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_rec_tot.setObjectName(_fromUtf8("label_rec_tot"))
        self.gridLayout_3.addWidget(self.label_rec_tot, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 3)
        self.line_8 = QtGui.QFrame(DialogDetsesso)
        font = QtGui.QFont()
        font.setWeight(75)
        font.setBold(True)
        self.line_8.setFont(font)
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.gridLayout_6.addWidget(self.line_8, 1, 0, 1, 3)
        self.comboBox_sito = QtGui.QComboBox(DialogDetsesso)
        self.comboBox_sito.setEnabled(True)
        self.comboBox_sito.setMinimumSize(QtCore.QSize(341, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_sito.setFont(font)
        self.comboBox_sito.setMouseTracking(True)
        self.comboBox_sito.setEditable(True)
        self.comboBox_sito.setMaxVisibleItems(99999)
        self.comboBox_sito.setMaxCount(2147483647)
        self.comboBox_sito.setObjectName(_fromUtf8("comboBox_sito"))
        self.comboBox_sito.addItem(_fromUtf8(""))
        self.gridLayout_6.addWidget(self.comboBox_sito, 2, 0, 2, 1)
        self.label_numero_individuo = QtGui.QLabel(DialogDetsesso)
        self.label_numero_individuo.setObjectName(_fromUtf8("label_numero_individuo"))
        self.gridLayout_6.addWidget(self.label_numero_individuo, 3, 1, 1, 1)
        self.lineEdit_nr_individuo = QtGui.QLineEdit(DialogDetsesso)
        self.lineEdit_nr_individuo.setObjectName(_fromUtf8("lineEdit_nr_individuo"))
        self.gridLayout_6.addWidget(self.lineEdit_nr_individuo, 3, 2, 1, 1)
        self.label_sito = QtGui.QLabel(DialogDetsesso)
        self.label_sito.setObjectName(_fromUtf8("label_sito"))
        self.gridLayout_6.addWidget(self.label_sito, 4, 0, 1, 1)
        self.label_15 = QtGui.QLabel(DialogDetsesso)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.gridLayout_6.addWidget(self.label_15, 5, 0, 1, 1)
        self.toolBox = QtGui.QToolBox(DialogDetsesso)
        self.toolBox.setEnabled(True)
        self.toolBox.setCursor(QtCore.Qt.ArrowCursor)
        self.toolBox.setMouseTracking(False)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.toolBoxPage1 = QtGui.QWidget()
        self.toolBoxPage1.setGeometry(QtCore.QRect(0, 0, 635, 401))
        self.toolBoxPage1.setObjectName(_fromUtf8("toolBoxPage1"))
        self.gridLayout_7 = QtGui.QGridLayout(self.toolBoxPage1)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.label_2 = QtGui.QLabel(self.toolBoxPage1)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit_mfmand_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_mfmand_grado_imp.setEnabled(False)
        self.lineEdit_mfmand_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_mfmand_grado_imp.setObjectName(_fromUtf8("lineEdit_mfmand_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_mfmand_grado_imp, 4, 5, 1, 1)
        self.lineEdit_msorb_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_msorb_grado_imp.setEnabled(False)
        self.lineEdit_msorb_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_msorb_grado_imp.setObjectName(_fromUtf8("lineEdit_msorb_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_msorb_grado_imp, 12, 1, 1, 1)
        self.comboBox_pzig_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_pzig_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_pzig_valori.setEditable(True)
        self.comboBox_pzig_valori.setObjectName(_fromUtf8("comboBox_pzig_valori"))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.comboBox_pzig_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.comboBox_pzig_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_pzig_valori, 6, 2, 1, 1)
        self.comboBox_pnuc_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_pnuc_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_pnuc_valori.setEditable(True)
        self.comboBox_pnuc_valori.setObjectName(_fromUtf8("comboBox_pnuc_valori"))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.comboBox_pnuc_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.comboBox_pnuc_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_pnuc_valori, 5, 2, 1, 1)
        self.lineEdit_sex_cr_tot = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_sex_cr_tot.setEnabled(False)
        self.lineEdit_sex_cr_tot.setObjectName(_fromUtf8("lineEdit_sex_cr_tot"))
        self.gridLayout_7.addWidget(self.lineEdit_sex_cr_tot, 12, 5, 1, 2)
        self.comboBox_zig_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_zig_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_zig_valori.setEditable(True)
        self.comboBox_zig_valori.setObjectName(_fromUtf8("comboBox_zig_valori"))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.comboBox_zig_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.comboBox_zig_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_zig_valori, 11, 2, 1, 1)
        self.comboBox_brmont_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_brmont_valori.setEditable(True)
        self.comboBox_brmont_valori.setObjectName(_fromUtf8("comboBox_brmont_valori"))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.comboBox_brmont_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.comboBox_brmont_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_brmont_valori, 8, 6, 1, 1)
        self.comboBox_glab_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_glab_valori.setEnabled(True)
        self.comboBox_glab_valori.setMinimumSize(QtCore.QSize(72, 26))
        self.comboBox_glab_valori.setMaximumSize(QtCore.QSize(72, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_glab_valori.setFont(font)
        self.comboBox_glab_valori.setMouseTracking(True)
        self.comboBox_glab_valori.setEditable(True)
        self.comboBox_glab_valori.setMaxVisibleItems(99999)
        self.comboBox_glab_valori.setMaxCount(2147483647)
        self.comboBox_glab_valori.setObjectName(_fromUtf8("comboBox_glab_valori"))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.comboBox_glab_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.comboBox_glab_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_glab_valori, 3, 2, 1, 1)
        self.label_90_condilo_mandibolare = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_condilo_mandibolare.setObjectName(_fromUtf8("label_90_condilo_mandibolare"))
        self.gridLayout_7.addWidget(self.label_90_condilo_mandibolare, 9, 3, 1, 1)
        self.comboBox_mfmand_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_mfmand_valori.setEditable(True)
        self.comboBox_mfmand_valori.setObjectName(_fromUtf8("comboBox_mfmand_valori"))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.comboBox_mfmand_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.comboBox_mfmand_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_mfmand_valori, 4, 6, 1, 1)
        self.label_87_inclinazione_frontale_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_87_inclinazione_frontale_3.setObjectName(_fromUtf8("label_87_inclinazione_frontale_3"))
        self.gridLayout_7.addWidget(self.label_87_inclinazione_frontale_3, 10, 0, 1, 1)
        self.label_86_protuberanza_occipitale_esterna_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_86_protuberanza_occipitale_esterna_3.setObjectName(
            _fromUtf8("label_86_protuberanza_occipitale_esterna_3"))
        self.gridLayout_7.addWidget(self.label_86_protuberanza_occipitale_esterna_3, 9, 0, 1, 1)
        self.label_70_morfologia_mandibola_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_70_morfologia_mandibola_3.setObjectName(_fromUtf8("label_70_morfologia_mandibola_3"))
        self.gridLayout_7.addWidget(self.label_70_morfologia_mandibola_3, 4, 3, 1, 2)
        self.label_90_palato = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_palato.setObjectName(_fromUtf8("label_90_palato"))
        self.gridLayout_7.addWidget(self.label_90_palato, 3, 3, 1, 1)
        self.label_83_processo_zigomatico_3 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_83_processo_zigomatico_3.setFont(font)
        self.label_83_processo_zigomatico_3.setObjectName(_fromUtf8("label_83_processo_zigomatico_3"))
        self.gridLayout_7.addWidget(self.label_83_processo_zigomatico_3, 6, 0, 1, 1)
        self.label_82_piano_nucale_3 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_82_piano_nucale_3.setFont(font)
        self.label_82_piano_nucale_3.setObjectName(_fromUtf8("label_82_piano_nucale_3"))
        self.gridLayout_7.addWidget(self.label_82_piano_nucale_3, 5, 0, 1, 1)
        self.pushButton_calcola_ind_sex = QtGui.QPushButton(self.toolBoxPage1)
        self.pushButton_calcola_ind_sex.setObjectName(_fromUtf8("pushButton_calcola_ind_sex"))
        self.gridLayout_7.addWidget(self.pushButton_calcola_ind_sex, 14, 4, 1, 3)
        self.lineEdit_zig_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_zig_grado_imp.setEnabled(False)
        self.lineEdit_zig_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_zig_grado_imp.setObjectName(_fromUtf8("lineEdit_zig_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_zig_grado_imp, 11, 1, 1, 1)
        self.lineEdit_pocc_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_pocc_grado_imp.setEnabled(False)
        self.lineEdit_pocc_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_pocc_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_pocc_grado_imp.setObjectName(_fromUtf8("lineEdit_pocc_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_pocc_grado_imp, 9, 1, 1, 1)
        self.comboBox_condm_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_condm_valori.setEditable(True)
        self.comboBox_condm_valori.setObjectName(_fromUtf8("comboBox_condm_valori"))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.comboBox_condm_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.comboBox_condm_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_condm_valori, 9, 6, 1, 1)
        self.lineEdit_arcsop_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_arcsop_grado_imp.setEnabled(False)
        self.lineEdit_arcsop_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_arcsop_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_arcsop_grado_imp.setObjectName(_fromUtf8("lineEdit_arcsop_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_arcsop_grado_imp, 7, 1, 1, 1)
        self.lineEdit_palato_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_palato_grado_imp.setEnabled(False)
        self.lineEdit_palato_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_palato_grado_imp.setObjectName(_fromUtf8("lineEdit_palato_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_palato_grado_imp, 3, 5, 1, 1)
        self.lineEdit_tub_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_tub_grado_imp.setEnabled(False)
        self.lineEdit_tub_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_tub_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_tub_grado_imp.setObjectName(_fromUtf8("lineEdit_tub_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_tub_grado_imp, 8, 1, 1, 1)
        self.label_90_indice_sessualizzazione_cranio = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_indice_sessualizzazione_cranio.setObjectName(_fromUtf8("label_90_indice_sessualizzazione_cranio"))
        self.gridLayout_7.addWidget(self.label_90_indice_sessualizzazione_cranio, 13, 3, 1, 1)
        self.comboBox_arcsop_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_arcsop_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_arcsop_valori.setEditable(True)
        self.comboBox_arcsop_valori.setObjectName(_fromUtf8("comboBox_arcsop_valori"))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.comboBox_arcsop_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.comboBox_arcsop_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_arcsop_valori, 7, 2, 1, 1)
        self.label_78_processo_mastoideo_3 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_78_processo_mastoideo_3.setFont(font)
        self.label_78_processo_mastoideo_3.setObjectName(_fromUtf8("label_78_processo_mastoideo_3"))
        self.gridLayout_7.addWidget(self.label_78_processo_mastoideo_3, 4, 0, 1, 1)
        self.comboBox_palato_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_palato_valori.setEditable(True)
        self.comboBox_palato_valori.setObjectName(_fromUtf8("comboBox_palato_valori"))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.comboBox_palato_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.comboBox_palato_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_palato_valori, 3, 6, 1, 1)
        self.label_89_valore_totale_sex_cranio = QtGui.QLabel(self.toolBoxPage1)
        self.label_89_valore_totale_sex_cranio.setObjectName(_fromUtf8("label_89_valore_totale_sex_cranio"))
        self.gridLayout_7.addWidget(self.label_89_valore_totale_sex_cranio, 12, 3, 1, 1)
        self.comboBox_pmast_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_pmast_valori.setEnabled(True)
        self.comboBox_pmast_valori.setMinimumSize(QtCore.QSize(72, 26))
        self.comboBox_pmast_valori.setMaximumSize(QtCore.QSize(72, 26))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        self.comboBox_pmast_valori.setFont(font)
        self.comboBox_pmast_valori.setMouseTracking(True)
        self.comboBox_pmast_valori.setEditable(True)
        self.comboBox_pmast_valori.setMaxVisibleItems(99999)
        self.comboBox_pmast_valori.setMaxCount(2147483647)
        self.comboBox_pmast_valori.setObjectName(_fromUtf8("comboBox_pmast_valori"))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.comboBox_pmast_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.comboBox_pmast_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_pmast_valori, 4, 2, 1, 1)
        self.comboBox_inclfr_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_inclfr_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_inclfr_valori.setEditable(True)
        self.comboBox_inclfr_valori.setObjectName(_fromUtf8("comboBox_inclfr_valori"))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.comboBox_inclfr_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.comboBox_inclfr_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_inclfr_valori, 10, 2, 1, 1)
        self.label_89_margine_sopraorbitale_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_89_margine_sopraorbitale_3.setObjectName(_fromUtf8("label_89_margine_sopraorbitale_3"))
        self.gridLayout_7.addWidget(self.label_89_margine_sopraorbitale_3, 12, 0, 1, 1)
        self.lineEdit_minf_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_minf_grado_imp.setEnabled(False)
        self.lineEdit_minf_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_minf_grado_imp.setObjectName(_fromUtf8("lineEdit_minf_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_minf_grado_imp, 7, 5, 1, 1)
        self.label_48_caratteri_cranio_6 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_48_caratteri_cranio_6.setFont(font)
        self.label_48_caratteri_cranio_6.setObjectName(_fromUtf8("label_48_caratteri_cranio_6"))
        self.gridLayout_7.addWidget(self.label_48_caratteri_cranio_6, 1, 0, 1, 1)
        self.label_90_margine_inferiore = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_margine_inferiore.setObjectName(_fromUtf8("label_90_margine_inferiore"))
        self.gridLayout_7.addWidget(self.label_90_margine_inferiore, 7, 3, 1, 1)
        self.comboBox_pocc_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_pocc_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_pocc_valori.setEditable(True)
        self.comboBox_pocc_valori.setObjectName(_fromUtf8("comboBox_pocc_valori"))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.comboBox_pocc_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.comboBox_pocc_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_pocc_valori, 9, 2, 1, 1)
        self.lineEdit_anmand_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_anmand_grado_imp.setEnabled(False)
        self.lineEdit_anmand_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_anmand_grado_imp.setObjectName(_fromUtf8("lineEdit_anmand_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_anmand_grado_imp, 6, 5, 1, 1)
        self.label_90_angolo_mandibolare = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_angolo_mandibolare.setObjectName(_fromUtf8("label_90_angolo_mandibolare"))
        self.gridLayout_7.addWidget(self.label_90_angolo_mandibolare, 6, 3, 1, 1)
        self.comboBox_anmand_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_anmand_valori.setEditable(True)
        self.comboBox_anmand_valori.setObjectName(_fromUtf8("comboBox_anmand_valori"))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.comboBox_anmand_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.comboBox_anmand_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_anmand_valori, 6, 6, 1, 1)
        self.label_19 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.gridLayout_7.addWidget(self.label_19, 1, 2, 1, 1)
        self.label_20 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.gridLayout_7.addWidget(self.label_20, 1, 6, 1, 1)
        self.lineEdit_inclfr_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_inclfr_grado_imp.setEnabled(False)
        self.lineEdit_inclfr_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_inclfr_grado_imp.setObjectName(_fromUtf8("lineEdit_inclfr_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_inclfr_grado_imp, 10, 1, 1, 1)
        self.lineEdit_brmont_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_brmont_grado_imp.setEnabled(False)
        self.lineEdit_brmont_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_brmont_grado_imp.setObjectName(_fromUtf8("lineEdit_brmont_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_brmont_grado_imp, 8, 5, 1, 1)
        self.comboBox_msorb_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_msorb_valori.setMaximumSize(QtCore.QSize(72, 16777215))
        self.comboBox_msorb_valori.setEditable(True)
        self.comboBox_msorb_valori.setObjectName(_fromUtf8("comboBox_msorb_valori"))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.comboBox_msorb_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.comboBox_msorb_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_msorb_valori, 12, 2, 1, 1)
        self.label_48_caratteri_cranio_5 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_48_caratteri_cranio_5.setFont(font)
        self.label_48_caratteri_cranio_5.setObjectName(_fromUtf8("label_48_caratteri_cranio_5"))
        self.gridLayout_7.addWidget(self.label_48_caratteri_cranio_5, 1, 3, 1, 1)
        self.comboBox_tub_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_tub_valori.setMaximumSize(QtCore.QSize(72, 26))
        self.comboBox_tub_valori.setEditable(True)
        self.comboBox_tub_valori.setObjectName(_fromUtf8("comboBox_tub_valori"))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.comboBox_tub_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.comboBox_tub_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_tub_valori, 8, 2, 1, 1)
        self.comboBox_minf_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_minf_valori.setEditable(True)
        self.comboBox_minf_valori.setObjectName(_fromUtf8("comboBox_minf_valori"))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.comboBox_minf_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.comboBox_minf_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_minf_valori, 7, 6, 1, 1)
        self.label_88_osso_zigomatico_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_88_osso_zigomatico_3.setObjectName(_fromUtf8("label_88_osso_zigomatico_3"))
        self.gridLayout_7.addWidget(self.label_88_osso_zigomatico_3, 11, 0, 1, 1)
        self.label_84_arcata_sopraciliare_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_84_arcata_sopraciliare_3.setObjectName(_fromUtf8("label_84_arcata_sopraciliare_3"))
        self.gridLayout_7.addWidget(self.label_84_arcata_sopraciliare_3, 7, 0, 1, 1)
        self.label_85_tuberosita_frontale_e_parietale_3 = QtGui.QLabel(self.toolBoxPage1)
        self.label_85_tuberosita_frontale_e_parietale_3.setObjectName(
            _fromUtf8("label_85_tuberosita_frontale_e_parietale_3"))
        self.gridLayout_7.addWidget(self.label_85_tuberosita_frontale_e_parietale_3, 8, 0, 1, 1)
        self.lineEdit_mento_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_mento_grado_imp.setEnabled(False)
        self.lineEdit_mento_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_mento_grado_imp.setObjectName(_fromUtf8("lineEdit_mento_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_mento_grado_imp, 5, 5, 1, 1)
        self.comboBox_ind_cr_sex = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_ind_cr_sex.setEnabled(False)
        self.comboBox_ind_cr_sex.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.comboBox_ind_cr_sex.setEditable(True)
        self.comboBox_ind_cr_sex.setMaxCount(2147483647)
        self.comboBox_ind_cr_sex.setObjectName(_fromUtf8("comboBox_ind_cr_sex"))
        self.comboBox_ind_cr_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_cr_sex.setItemText(0, _fromUtf8(""))
        self.comboBox_ind_cr_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_cr_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_cr_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_cr_sex.setItemText(3, _fromUtf8("Indeterminato"))
        self.comboBox_ind_cr_sex.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_ind_cr_sex, 13, 4, 1, 3)
        self.comboBox_mento_valori = QtGui.QComboBox(self.toolBoxPage1)
        self.comboBox_mento_valori.setEditable(True)
        self.comboBox_mento_valori.setObjectName(_fromUtf8("comboBox_mento_valori"))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.comboBox_mento_valori.setItemText(0, _fromUtf8(""))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.comboBox_mento_valori.addItem(_fromUtf8(""))
        self.gridLayout_7.addWidget(self.comboBox_mento_valori, 5, 6, 1, 1)
        self.lineEdit_condm_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_condm_grado_imp.setEnabled(False)
        self.lineEdit_condm_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_condm_grado_imp.setObjectName(_fromUtf8("lineEdit_condm_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_condm_grado_imp, 9, 5, 1, 1)
        self.label_18 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.gridLayout_7.addWidget(self.label_18, 1, 5, 1, 1)
        self.label_3 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 1, 1, 1, 1)
        self.lineEdit_glab_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_glab_grado_imp.setEnabled(False)
        self.lineEdit_glab_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_glab_grado_imp.setMaxLength(32768)
        self.lineEdit_glab_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_glab_grado_imp.setObjectName(_fromUtf8("lineEdit_glab_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_glab_grado_imp, 3, 1, 1, 1)
        self.lineEdit_pmast_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_pmast_grado_imp.setEnabled(False)
        self.lineEdit_pmast_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_pmast_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_pmast_grado_imp.setObjectName(_fromUtf8("lineEdit_pmast_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_pmast_grado_imp, 4, 1, 1, 1)
        self.label_47_glabella_3 = QtGui.QLabel(self.toolBoxPage1)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_47_glabella_3.setFont(font)
        self.label_47_glabella_3.setObjectName(_fromUtf8("label_47_glabella_3"))
        self.gridLayout_7.addWidget(self.label_47_glabella_3, 3, 0, 1, 1)
        self.label_90_branca_montante = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_branca_montante.setObjectName(_fromUtf8("label_90_branca_montante"))
        self.gridLayout_7.addWidget(self.label_90_branca_montante, 8, 3, 1, 1)
        self.lineEdit_pnuc_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_pnuc_grado_imp.setEnabled(False)
        self.lineEdit_pnuc_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_pnuc_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_pnuc_grado_imp.setObjectName(_fromUtf8("lineEdit_pnuc_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_pnuc_grado_imp, 5, 1, 1, 1)
        self.lineEdit_pzig_grado_imp = QtGui.QLineEdit(self.toolBoxPage1)
        self.lineEdit_pzig_grado_imp.setEnabled(False)
        self.lineEdit_pzig_grado_imp.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_pzig_grado_imp.setAlignment(
            QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.lineEdit_pzig_grado_imp.setObjectName(_fromUtf8("lineEdit_pzig_grado_imp"))
        self.gridLayout_7.addWidget(self.lineEdit_pzig_grado_imp, 6, 1, 1, 1)
        self.label_90_mento = QtGui.QLabel(self.toolBoxPage1)
        self.label_90_mento.setObjectName(_fromUtf8("label_90_mento"))
        self.gridLayout_7.addWidget(self.label_90_mento, 5, 3, 1, 1)
        self.pushButton_cranio = QtGui.QPushButton(self.toolBoxPage1)
        self.pushButton_cranio.setObjectName(_fromUtf8("pushButton_cranio"))
        self.gridLayout_7.addWidget(self.pushButton_cranio, 0, 1, 1, 1)
        self.toolBox.addItem(self.toolBoxPage1, _fromUtf8(""))
        self.toolBoxPage2 = QtGui.QWidget()
        self.toolBoxPage2.setGeometry(QtCore.QRect(0, 0, 572, 468))
        self.toolBoxPage2.setObjectName(_fromUtf8("toolBoxPage2"))
        self.gridLayout_8 = QtGui.QGridLayout(self.toolBoxPage2)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.label_4 = QtGui.QLabel(self.toolBoxPage2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_8.addWidget(self.label_4, 1, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.toolBoxPage2)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_8.addWidget(self.label_6, 1, 5, 1, 2)
        self.label_5 = QtGui.QLabel(self.toolBoxPage2)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_8.addWidget(self.label_5, 1, 1, 1, 2)
        self.label_12 = QtGui.QLabel(self.toolBoxPage2)
        self.label_12.setTextFormat(QtCore.Qt.LogText)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.gridLayout_8.addWidget(self.label_12, 2, 1, 1, 2)
        self.label_13 = QtGui.QLabel(self.toolBoxPage2)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.gridLayout_8.addWidget(self.label_13, 3, 1, 1, 2)
        self.label_14 = QtGui.QLabel(self.toolBoxPage2)
        self.label_14.setWordWrap(True)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.gridLayout_8.addWidget(self.label_14, 5, 1, 2, 2)
        self.label_7 = QtGui.QLabel(self.toolBoxPage2)
        self.label_7.setText(_fromUtf8(""))
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_8.addWidget(self.label_7, 3, 0, 1, 1)
        self.label_16 = QtGui.QLabel(self.toolBoxPage2)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.gridLayout_8.addWidget(self.label_16, 1, 3, 1, 1)
        self.comboBox_sup_p_I = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_sup_p_I.setEditable(True)
        self.comboBox_sup_p_I.setObjectName(_fromUtf8("comboBox_sup_p_I"))
        self.comboBox_sup_p_I.addItem(_fromUtf8(""))
        self.comboBox_sup_p_I.setItemText(0, _fromUtf8(""))
        self.comboBox_sup_p_I.addItem(_fromUtf8(""))
        self.comboBox_sup_p_I.addItem(_fromUtf8(""))
        self.comboBox_sup_p_I.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_sup_p_I, 2, 3, 1, 1)
        self.comboBox_sup_p_II = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_sup_p_II.setEditable(True)
        self.comboBox_sup_p_II.setObjectName(_fromUtf8("comboBox_sup_p_II"))
        self.comboBox_sup_p_II.addItem(_fromUtf8(""))
        self.comboBox_sup_p_II.setItemText(0, _fromUtf8(""))
        self.comboBox_sup_p_II.addItem(_fromUtf8(""))
        self.comboBox_sup_p_II.addItem(_fromUtf8(""))
        self.comboBox_sup_p_II.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_sup_p_II, 3, 3, 1, 1)
        self.comboBox_sup_p_III = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_sup_p_III.setEditable(True)
        self.comboBox_sup_p_III.setObjectName(_fromUtf8("comboBox_sup_p_III"))
        self.comboBox_sup_p_III.addItem(_fromUtf8(""))
        self.comboBox_sup_p_III.setItemText(0, _fromUtf8(""))
        self.comboBox_sup_p_III.addItem(_fromUtf8(""))
        self.comboBox_sup_p_III.addItem(_fromUtf8(""))
        self.comboBox_sup_p_III.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_sup_p_III, 5, 3, 1, 1)
        self.comboBox_sup_p_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_sup_p_sex.setEnabled(False)
        self.comboBox_sup_p_sex.setEditable(True)
        self.comboBox_sup_p_sex.setObjectName(_fromUtf8("comboBox_sup_p_sex"))
        self.comboBox_sup_p_sex.addItem(_fromUtf8(""))
        self.comboBox_sup_p_sex.setItemText(0, _fromUtf8(""))
        self.comboBox_sup_p_sex.addItem(_fromUtf8(""))
        self.comboBox_sup_p_sex.addItem(_fromUtf8(""))
        self.comboBox_sup_p_sex.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_sup_p_sex, 3, 5, 1, 1)
        self.comboBox_in_isch_I = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_in_isch_I.setEditable(True)
        self.comboBox_in_isch_I.setObjectName(_fromUtf8("comboBox_in_isch_I"))
        self.comboBox_in_isch_I.addItem(_fromUtf8(""))
        self.comboBox_in_isch_I.setItemText(0, _fromUtf8(""))
        self.comboBox_in_isch_I.addItem(_fromUtf8(""))
        self.comboBox_in_isch_I.addItem(_fromUtf8(""))
        self.comboBox_in_isch_I.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_in_isch_I, 11, 3, 1, 1)
        self.label_37 = QtGui.QLabel(self.toolBoxPage2)
        self.label_37.setWordWrap(True)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.gridLayout_8.addWidget(self.label_37, 12, 1, 1, 2)
        self.label_36 = QtGui.QLabel(self.toolBoxPage2)
        self.label_36.setWordWrap(True)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.gridLayout_8.addWidget(self.label_36, 13, 1, 1, 2)
        self.comboBox_in_isch_II = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_in_isch_II.setEditable(True)
        self.comboBox_in_isch_II.setObjectName(_fromUtf8("comboBox_in_isch_II"))
        self.comboBox_in_isch_II.addItem(_fromUtf8(""))
        self.comboBox_in_isch_II.setItemText(0, _fromUtf8(""))
        self.comboBox_in_isch_II.addItem(_fromUtf8(""))
        self.comboBox_in_isch_II.addItem(_fromUtf8(""))
        self.comboBox_in_isch_II.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_in_isch_II, 12, 3, 1, 1)
        self.comboBox_in_isch_III = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_in_isch_III.setEditable(True)
        self.comboBox_in_isch_III.setObjectName(_fromUtf8("comboBox_in_isch_III"))
        self.comboBox_in_isch_III.addItem(_fromUtf8(""))
        self.comboBox_in_isch_III.setItemText(0, _fromUtf8(""))
        self.comboBox_in_isch_III.addItem(_fromUtf8(""))
        self.comboBox_in_isch_III.addItem(_fromUtf8(""))
        self.comboBox_in_isch_III.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_in_isch_III, 13, 3, 1, 1)
        self.label_41 = QtGui.QLabel(self.toolBoxPage2)
        self.label_41.setWordWrap(True)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.gridLayout_8.addWidget(self.label_41, 18, 1, 1, 2)
        self.label_40 = QtGui.QLabel(self.toolBoxPage2)
        self.label_40.setWordWrap(True)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gridLayout_8.addWidget(self.label_40, 19, 1, 1, 2)
        self.label_39 = QtGui.QLabel(self.toolBoxPage2)
        self.label_39.setWordWrap(True)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.gridLayout_8.addWidget(self.label_39, 20, 1, 1, 2)
        self.label_10 = QtGui.QLabel(self.toolBoxPage2)
        self.label_10.setText(_fromUtf8(""))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.gridLayout_8.addWidget(self.label_10, 19, 0, 1, 1)
        self.comboBox_in_isch_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_in_isch_sex.setEnabled(False)
        self.comboBox_in_isch_sex.setEditable(True)
        self.comboBox_in_isch_sex.setObjectName(_fromUtf8("comboBox_in_isch_sex"))
        self.comboBox_in_isch_sex.addItem(_fromUtf8(""))
        self.comboBox_in_isch_sex.setItemText(0, _fromUtf8(""))
        self.comboBox_in_isch_sex.addItem(_fromUtf8(""))
        self.comboBox_in_isch_sex.addItem(_fromUtf8(""))
        self.comboBox_in_isch_sex.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_in_isch_sex, 12, 5, 1, 1)
        self.comboBox_ramo_ip_III = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_ramo_ip_III.setEditable(True)
        self.comboBox_ramo_ip_III.setObjectName(_fromUtf8("comboBox_ramo_ip_III"))
        self.comboBox_ramo_ip_III.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_III.setItemText(0, _fromUtf8(""))
        self.comboBox_ramo_ip_III.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_III.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_III.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_ramo_ip_III, 20, 3, 1, 1)
        self.comboBox_ramo_ip_II = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_ramo_ip_II.setEditable(True)
        self.comboBox_ramo_ip_II.setObjectName(_fromUtf8("comboBox_ramo_ip_II"))
        self.comboBox_ramo_ip_II.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_II.setItemText(0, _fromUtf8(""))
        self.comboBox_ramo_ip_II.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_II.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_II.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_ramo_ip_II, 19, 3, 1, 1)
        self.comboBox_ramo_ip_I = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_ramo_ip_I.setEditable(True)
        self.comboBox_ramo_ip_I.setObjectName(_fromUtf8("comboBox_ramo_ip_I"))
        self.comboBox_ramo_ip_I.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_I.setItemText(0, _fromUtf8(""))
        self.comboBox_ramo_ip_I.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_I.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_I.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_ramo_ip_I, 18, 3, 1, 1)
        self.comboBox_ramo_ip_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_ramo_ip_sex.setEnabled(False)
        self.comboBox_ramo_ip_sex.setEditable(True)
        self.comboBox_ramo_ip_sex.setObjectName(_fromUtf8("comboBox_ramo_ip_sex"))
        self.comboBox_ramo_ip_sex.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_sex.setItemText(0, _fromUtf8(""))
        self.comboBox_ramo_ip_sex.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_sex.addItem(_fromUtf8(""))
        self.comboBox_ramo_ip_sex.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_ramo_ip_sex, 19, 5, 1, 1)
        self.label_45 = QtGui.QLabel(self.toolBoxPage2)
        self.label_45.setWordWrap(True)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.gridLayout_8.addWidget(self.label_45, 23, 1, 1, 2)
        self.label_38 = QtGui.QLabel(self.toolBoxPage2)
        self.label_38.setWordWrap(True)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.gridLayout_8.addWidget(self.label_38, 11, 1, 1, 2)
        self.label_9 = QtGui.QLabel(self.toolBoxPage2)
        self.label_9.setText(_fromUtf8(""))
        self.label_9.setWordWrap(True)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout_8.addWidget(self.label_9, 14, 0, 1, 1)
        self.label = QtGui.QLabel(self.toolBoxPage2)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_8.addWidget(self.label, 0, 0, 1, 1)
        self.comboBox_prop_ip_sex_2 = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_prop_ip_sex_2.setEnabled(True)
        self.comboBox_prop_ip_sex_2.setEditable(True)
        self.comboBox_prop_ip_sex_2.setObjectName(_fromUtf8("comboBox_prop_ip_sex_2"))
        self.comboBox_prop_ip_sex_2.addItem(_fromUtf8(""))
        self.comboBox_prop_ip_sex_2.setItemText(0, _fromUtf8(""))
        self.comboBox_prop_ip_sex_2.addItem(_fromUtf8(""))
        self.comboBox_prop_ip_sex_2.addItem(_fromUtf8(""))
        self.comboBox_prop_ip_sex_2.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_prop_ip_sex_2, 23, 3, 1, 1)
        self.comboBox_ind_bac_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_ind_bac_sex.setEnabled(False)
        self.comboBox_ind_bac_sex.setMaximumSize(QtCore.QSize(150, 16777215))
        self.comboBox_ind_bac_sex.setEditable(True)
        self.comboBox_ind_bac_sex.setObjectName(_fromUtf8("comboBox_ind_bac_sex"))
        self.comboBox_ind_bac_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_bac_sex.setItemText(0, _fromUtf8(""))
        self.comboBox_ind_bac_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_bac_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_bac_sex.addItem(_fromUtf8(""))
        self.comboBox_ind_bac_sex.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_ind_bac_sex, 24, 5, 1, 1)
        self.pushButton_calcola_ind_sex_bac = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_calcola_ind_sex_bac.setObjectName(_fromUtf8("pushButton_calcola_ind_sex_bac"))
        self.gridLayout_8.addWidget(self.pushButton_calcola_ind_sex_bac, 25, 5, 1, 1)
        self.label_17 = QtGui.QLabel(self.toolBoxPage2)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.gridLayout_8.addWidget(self.label_17, 24, 2, 1, 2)
        self.comboBox_prop_ip_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_prop_ip_sex.setEnabled(False)
        self.comboBox_prop_ip_sex.setEditable(True)
        self.comboBox_prop_ip_sex.setObjectName(_fromUtf8("comboBox_prop_ip_sex"))
        self.gridLayout_8.addWidget(self.comboBox_prop_ip_sex, 23, 5, 1, 1)
        self.pushButton_bacino_sup_preauricolare = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_bacino_sup_preauricolare.setObjectName(_fromUtf8("pushButton_bacino_sup_preauricolare"))
        self.gridLayout_8.addWidget(self.pushButton_bacino_sup_preauricolare, 2, 0, 1, 1)
        self.pushButton_bacino_grande_incisura_ischiatica = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_bacino_grande_incisura_ischiatica.setObjectName(
            _fromUtf8("pushButton_bacino_grande_incisura_ischiatica"))
        self.gridLayout_8.addWidget(self.pushButton_bacino_grande_incisura_ischiatica, 11, 0, 1, 1)
        self.pushButton_bacino_ramo_ischio_pubico = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_bacino_ramo_ischio_pubico.setObjectName(_fromUtf8("pushButton_bacino_ramo_ischio_pubico"))
        self.gridLayout_8.addWidget(self.pushButton_bacino_ramo_ischio_pubico, 18, 0, 1, 1)
        self.pushButton_proporzioni_ischio_pubiche = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_proporzioni_ischio_pubiche.setObjectName(_fromUtf8("pushButton_proporzioni_ischio_pubiche"))
        self.gridLayout_8.addWidget(self.pushButton_proporzioni_ischio_pubiche, 23, 0, 1, 1)
        self.pushButton_bacino_arco_composito = QtGui.QPushButton(self.toolBoxPage2)
        self.pushButton_bacino_arco_composito.setObjectName(_fromUtf8("pushButton_bacino_arco_composito"))
        self.gridLayout_8.addWidget(self.pushButton_bacino_arco_composito, 16, 0, 1, 1)
        self.label_44 = QtGui.QLabel(self.toolBoxPage2)
        self.label_44.setWordWrap(True)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.gridLayout_8.addWidget(self.label_44, 16, 1, 1, 1)
        self.comboBox_arco_c_sex_2 = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_arco_c_sex_2.setEnabled(True)
        self.comboBox_arco_c_sex_2.setEditable(True)
        self.comboBox_arco_c_sex_2.setObjectName(_fromUtf8("comboBox_arco_c_sex_2"))
        self.comboBox_arco_c_sex_2.addItem(_fromUtf8(""))
        self.comboBox_arco_c_sex_2.setItemText(0, _fromUtf8(""))
        self.comboBox_arco_c_sex_2.addItem(_fromUtf8(""))
        self.comboBox_arco_c_sex_2.addItem(_fromUtf8(""))
        self.comboBox_arco_c_sex_2.addItem(_fromUtf8(""))
        self.gridLayout_8.addWidget(self.comboBox_arco_c_sex_2, 16, 3, 1, 1)
        self.comboBox_arco_c_sex = QtGui.QComboBox(self.toolBoxPage2)
        self.comboBox_arco_c_sex.setEnabled(False)
        self.comboBox_arco_c_sex.setEditable(True)
        self.comboBox_arco_c_sex.setObjectName(_fromUtf8("comboBox_arco_c_sex"))
        self.gridLayout_8.addWidget(self.comboBox_arco_c_sex, 16, 5, 1, 1)
        self.toolBox.addItem(self.toolBoxPage2, _fromUtf8(""))
        self.gridLayout_6.addWidget(self.toolBox, 6, 0, 1, 3)

        self.retranslateUi(DialogDetsesso)
        QtCore.QMetaObject.connectSlotsByName(DialogDetsesso)

    def retranslateUi(self, DialogDetsesso):
        DialogDetsesso.setWindowTitle(
            QtGui.QApplication.translate("DialogDetsesso", "pyArchInit Gestione Scavi - Scheda Determinazione Sesso",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.label_29.setText(
            QtGui.QApplication.translate("DialogDetsesso", "DBMS Toolbar", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_connect.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Connection test", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_first_rec.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "First rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_next_rec.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Next rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_last_rec.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Last rec", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_rec.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "New record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_save.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_new_search.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "new search", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_search_go.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "search !!!", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_sort.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Order by", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_view_all.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "View alls records", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_delete.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Delete record", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_prev_rec.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Prev rec", None, QtGui.QApplication.UnicodeUTF8))
        self.label_42.setText(
            QtGui.QApplication.translate("DialogDetsesso", "DB Info", None, QtGui.QApplication.UnicodeUTF8))
        self.label_43.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Ordinamento", None, QtGui.QApplication.UnicodeUTF8))
        self.label_34.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_27.setText(
            QtGui.QApplication.translate("DialogDetsesso", "record n.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_corrente.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(
            QtGui.QApplication.translate("DialogDetsesso", "record tot.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_rec_tot.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sito.setItemText(0,
                                       QtGui.QApplication.translate("DialogDetsesso", "Inserisci un valore pippo", None,
                                                                    QtGui.QApplication.UnicodeUTF8))
        self.label_numero_individuo.setText(
            QtGui.QApplication.translate("DialogDetsesso", "N. individuo", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sito.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Sito ", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("DialogDetsesso", "Indice di sessualizzazione", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setToolTip(
            QtGui.QApplication.translate("DialogDetsesso", "Grado/importanza", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("DialogDetsesso", "Acsadi e Nemeskeri, 1970", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_mfmand_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_msorb_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pzig_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pzig_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pzig_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pzig_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pzig_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pnuc_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pnuc_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pnuc_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pnuc_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pnuc_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_zig_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_zig_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_zig_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_zig_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_zig_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_brmont_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_brmont_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_brmont_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_brmont_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_brmont_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_glab_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_glab_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_glab_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_glab_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_glab_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.label_90_condilo_mandibolare.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Condilo mandibolare", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mfmand_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mfmand_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mfmand_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mfmand_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mfmand_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_87_inclinazione_frontale_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Inclinazione frontale", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_86_protuberanza_occipitale_esterna_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Protuberanza occipitale est.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_70_morfologia_mandibola_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Morfologia mandibola", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_90_palato.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Palato", None, QtGui.QApplication.UnicodeUTF8))
        self.label_83_processo_zigomatico_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Processo zigomatico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_82_piano_nucale_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Piano nucale", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_calcola_ind_sex.setText(
            QtGui.QApplication.translate("DialogDetsesso", "calcola", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_zig_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_pocc_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_condm_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_condm_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_condm_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_condm_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_condm_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_arcsop_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_palato_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_tub_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90_indice_sessualizzazione_cranio.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Indice sessualizzazione", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arcsop_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arcsop_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arcsop_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arcsop_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arcsop_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_78_processo_mastoideo_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Processo mastoideo", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_palato_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_palato_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_palato_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_palato_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_palato_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_89_valore_totale_sex_cranio.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Valore totale", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pmast_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pmast_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pmast_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pmast_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pmast_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_inclfr_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_inclfr_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_inclfr_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_inclfr_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_inclfr_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_89_margine_sopraorbitale_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Margine sopraorbitale", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_minf_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_48_caratteri_cranio_6.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Caratteri", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90_margine_inferiore.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Margine inferiore", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pocc_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pocc_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pocc_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pocc_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_pocc_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_anmand_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90_angolo_mandibolare.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Angolo mandibolare", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_anmand_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_anmand_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_anmand_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_anmand_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_anmand_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Valori", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Valori", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_inclfr_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_brmont_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_msorb_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_msorb_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_msorb_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_msorb_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_msorb_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.label_48_caratteri_cranio_5.setText(QtGui.QApplication.translate("DialogDetsesso",
                                                                              "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                              "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                              "p, li { white-space: pre-wrap; }\n"
                                                                              "</style></head><body style=\" font-family:\'Lucida Grande\'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
                                                                              "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Caratteri</p></body></html>",
                                                                              None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tub_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tub_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tub_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tub_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_tub_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_minf_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_minf_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_minf_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_minf_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_minf_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.label_88_osso_zigomatico_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Osso zigomatico", None, QtGui.QApplication.UnicodeUTF8))
        self.label_84_arcata_sopraciliare_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Arcata sopraciliare", None, QtGui.QApplication.UnicodeUTF8))
        self.label_85_tuberosita_frontale_e_parietale_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Tuberosità front. e par.", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_mento_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "2", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_cr_sex.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "Maschio", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_cr_sex.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "Femmina", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_cr_sex.setItemText(4,
                                             QtGui.QApplication.translate("DialogDetsesso", "Non determinabile", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mento_valori.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "-2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mento_valori.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "-1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mento_valori.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "0", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mento_valori.setItemText(4, QtGui.QApplication.translate("DialogDetsesso", "+1", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_mento_valori.setItemText(5, QtGui.QApplication.translate("DialogDetsesso", "+2", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_condm_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "1", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Grado imp", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Grado imp", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_glab_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_pmast_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_47_glabella_3.setToolTip(QtGui.QApplication.translate("DialogDetsesso",
                                                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                                         "p, li { white-space: pre-wrap; }\n"
                                                                         "</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
                                                                         "<p style=\" margin-to", None,
                                                                         QtGui.QApplication.UnicodeUTF8))
        self.label_47_glabella_3.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Glabella", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90_branca_montante.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Branca montante", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_pnuc_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit_pzig_grado_imp.setText(
            QtGui.QApplication.translate("DialogDetsesso", "3", None, QtGui.QApplication.UnicodeUTF8))
        self.label_90_mento.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Mento", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_cranio.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Apri tavola", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage1),
                                 QtGui.QApplication.translate("DialogDetsesso", "Cranio", None,
                                                              QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Caratteri", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Sesso stimato", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("DialogDetsesso", "Indice di sessualizzazione", None,
                                                          QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("DialogDetsesso", "I: sviluppo negativo dei rilievi ", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("DialogDetsesso", "II: aspetto incavo o puntinato", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(
            QtGui.QApplication.translate("DialogDetsesso", "III: sviluppo positivo dei rilievi ", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Sesso stimato", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_I.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_I.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_I.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                          QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_II.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                           QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_II.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                           QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_II.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                           QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_III.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_III.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_III.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_sex.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_sex.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_sup_p_sex.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_I.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_I.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_I.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.label_37.setText(
            QtGui.QApplication.translate("DialogDetsesso", "II: forma contorno dell\'arco incisura ischiatica", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_36.setText(QtGui.QApplication.translate("DialogDetsesso",
                                                           "III: contorno della corda dell\'arco posteriore relativo alla linea dal punto A all\'incisura ischiatica",
                                                           None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_II.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_II.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_II.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_III.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_III.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_III.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.label_41.setText(
            QtGui.QApplication.translate("DialogDetsesso", "I: caratterizzazione del margine inf. dell\'osso coxale ",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.label_40.setText(
            QtGui.QApplication.translate("DialogDetsesso", "II: assenza o presenza della cresta fallica", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_39.setText(
            QtGui.QApplication.translate("DialogDetsesso", "III: aspetto del ramo ischio-pubico", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_sex.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_sex.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_in_isch_sex.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_III.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_III.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_III.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_II.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_II.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_II.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                             QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_I.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_I.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_I.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                            QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_sex.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_sex.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ramo_ip_sex.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.label_45.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Relazione tra la lunghezza dell\'ischio e del pube ", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.label_38.setText(
            QtGui.QApplication.translate("DialogDetsesso", "I: proporz. della lunghezza dell\'arco incisura ischiatica",
                                         None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Bruzek, 2002", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_prop_ip_sex_2.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_prop_ip_sex_2.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_prop_ip_sex_2.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                                QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_bac_sex.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "Maschio", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_bac_sex.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "Femmina", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_bac_sex.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "Indeterminato", None,
                                                                              QtGui.QApplication.UnicodeUTF8))
        self.comboBox_ind_bac_sex.setItemText(4,
                                              QtGui.QApplication.translate("DialogDetsesso", "Non determinabile", None,
                                                                           QtGui.QApplication.UnicodeUTF8))
        self.pushButton_calcola_ind_sex_bac.setText(
            QtGui.QApplication.translate("DialogDetsesso", "calcola", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("DialogDetsesso", "Indice di sessualizzazione", None,
                                                           QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bacino_sup_preauricolare.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Superficie preauricolare", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bacino_grande_incisura_ischiatica.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Grande inc. ischiatica", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bacino_ramo_ischio_pubico.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Ramo ischio-pubico", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_proporzioni_ischio_pubiche.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Prop. ischio-pubiche", None,
                                         QtGui.QApplication.UnicodeUTF8))
        self.pushButton_bacino_arco_composito.setText(
            QtGui.QApplication.translate("DialogDetsesso", "Arco composito", None, QtGui.QApplication.UnicodeUTF8))
        self.label_44.setText(QtGui.QApplication.translate("DialogDetsesso",
                                                           "Relazione tra il contorno dell\'arco dell\'ischio e della sup. auricolare",
                                                           None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arco_c_sex_2.setItemText(1, QtGui.QApplication.translate("DialogDetsesso", "M", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arco_c_sex_2.setItemText(2, QtGui.QApplication.translate("DialogDetsesso", "I", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.comboBox_arco_c_sex_2.setItemText(3, QtGui.QApplication.translate("DialogDetsesso", "F", None,
                                                                               QtGui.QApplication.UnicodeUTF8))
        self.toolBox.setItemText(self.toolBox.indexOf(self.toolBoxPage2),
                                 QtGui.QApplication.translate("DialogDetsesso", "Bacino", None,
                                                              QtGui.QApplication.UnicodeUTF8))
