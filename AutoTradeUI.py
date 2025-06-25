import sys

print(sys.executable)
print(sys.version)


from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QComboBox, QPushButton, QTextEdit, QVBoxLayout, QHBoxLayout
)

class AutoTradeUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("풍경&샬라 자동매매 v0.1")
        self.setGeometry(300, 300, 400, 300)
        self.init_ui()

    def init_ui(self):
        # 종목 선택
        lbl_coin = QLabel('종목:')
        self.cmb_coin = QComboBox()
        self.cmb_coin.addItems(['BTC/KRW', 'ETH/KRW', 'XRP/KRW', 'BTT/KRW'])

        # 익절률
        lbl_takeprofit = QLabel('익절률(%)')
        self.edit_takeprofit = QLineEdit('5')  # 기본 5%
        # 손절률
        lbl_stoploss = QLabel('손절률(%)')
        self.edit_stoploss = QLineEdit('-3')   # 기본 -3%
        # 매수금액
        lbl_amount = QLabel('매수금액(원)')
        self.edit_amount = QLineEdit('10000')  # 기본 1만원

        # 시작/정지 버튼
        self.btn_start = QPushButton('자동매매 시작')
        self.btn_stop = QPushButton('자동매매 정지')

        # 로그창
        self.logbox = QTextEdit()
        self.logbox.setReadOnly(True)

        # 배치
        layout = QVBoxLayout()
        h1 = QHBoxLayout()
        h1.addWidget(lbl_coin)
        h1.addWidget(self.cmb_coin)
        layout.addLayout(h1)

        h2 = QHBoxLayout()
        h2.addWidget(lbl_takeprofit)
        h2.addWidget(self.edit_takeprofit)
        h2.addWidget(lbl_stoploss)
        h2.addWidget(self.edit_stoploss)
        layout.addLayout(h2)

        h3 = QHBoxLayout()
        h3.addWidget(lbl_amount)
        h3.addWidget(self.edit_amount)
        layout.addLayout(h3)

        h4 = QHBoxLayout()
        h4.addWidget(self.btn_start)
        h4.addWidget(self.btn_stop)
        layout.addLayout(h4)

        layout.addWidget(QLabel("실시간 로그"))
        layout.addWidget(self.logbox)
        self.setLayout(layout)

        # 버튼 이벤트 연결(아직 실제 자동매매 연동 X, 이후 구현)
        self.btn_start.clicked.connect(self.log_start)
        self.btn_stop.clicked.connect(self.log_stop)

    def log_start(self):
        self.logbox.append("[자동매매] 시작 버튼 클릭!")

    def log_stop(self):
        self.logbox.append("[자동매매] 정지 버튼 클릭!")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AutoTradeUI()
    win.show()
    sys.exit(app.exec_())
