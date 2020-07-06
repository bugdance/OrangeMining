#!/usr/bin/python env
# -*- coding: utf-8 -*-
import sys
from . import follow
from AnyQt import QtGui
from AnyQt.QtWidgets import *
from urllib import request, parse

class LoginDlg(QDialog):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        usr = QLabel("用户名:")
        pwd = QLabel("密  码:")
        self.usrLineEdit = QLineEdit()
        self.pwdLineEdit = QLineEdit()
        self.pwdLineEdit.setEchoMode(QLineEdit.Password)

        gridLayout = QGridLayout()
        gridLayout.addWidget(usr, 0, 0, 1, 1)
        gridLayout.addWidget(pwd, 1, 0, 1, 1)
        gridLayout.addWidget(self.usrLineEdit, 0, 1, 1, 3);
        gridLayout.addWidget(self.pwdLineEdit, 1, 1, 1, 3);

        okBtn = QPushButton("确定")
        cancelBtn = QPushButton("取消")
        btnLayout = QHBoxLayout()

        btnLayout.setSpacing(60)
        btnLayout.addWidget(okBtn)
        btnLayout.addWidget(cancelBtn)

        dlgLayout = QVBoxLayout()
        dlgLayout.setContentsMargins(40, 40, 40, 40)
        dlgLayout.addLayout(gridLayout)
        dlgLayout.addStretch(40)
        dlgLayout.addLayout(btnLayout)

        self.setLayout(dlgLayout)
        okBtn.clicked.connect(self.accept)
        cancelBtn.clicked.connect(self.reject)
        self.setWindowTitle("Logis PMT")
#        self.setWindowIcon("Icons/tubiao.ico")
        self.resize(300, 200)


    def accept(self):
        url = "http://www.cfdsj.cn/login/orange-login?"
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
                "Connection": "keep-alive"
        }
        data = {
                "username": self.usrLineEdit.text().strip(),
                "pwd": self.pwdLineEdit.text().strip(),
                "islogin": '0',
        }
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, headers=headers, data=data)
        try:
            import socket
            socket.setdefaulttimeout(20)
            page = request.urlopen(req).read()
        except Exception as e:
            QMessageBox.warning(self,
                    "错误",
                    "服务器连接不上!",
                    QMessageBox.Yes)
            self.usrLineEdit.setFocus()
        else:
            if str(page, encoding='utf-8') == '0':
                QMessageBox.warning(self,
                        "警告",
                        "用户名或密码不存在!",
                        QMessageBox.Yes)
                self.usrLineEdit.setFocus()
            elif str(page, encoding='utf-8') == '1':
                QMessageBox.warning(self,
                        "警告",
                        "此用户已经登录过!",
                        QMessageBox.Yes)
                self.usrLineEdit.setFocus()
            else:
                super(LoginDlg, self).accept()


def logout(self):
    url = "http://www.cfdsj.cn/login/orange-login?"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)",
            "Connection": "keep-alive"
    }
    data = {
            "username": LoginDlg.usrLineEdit.text().strip(),
            "pwd": '',
            "islogin": '1',
    }
    data = parse.urlencode(data).encode('utf-8')
    req = request.Request(url, headers=headers, data=data)


app = QApplication(sys.argv)
dlg = LoginDlg()
dlg.show()
if dlg.exec_():
    sys.exit(follow.main())
    logout()
app.exit()
del app
