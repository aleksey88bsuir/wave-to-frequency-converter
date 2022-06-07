from email.mime import application
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from user_interface import Ui_MainWindow
from Converter import convert_wave_number_to_frequency_when_receiving as cwn_rc
from Converter import convert_wave_number_to_frequency_when_transmitting as cwn_ts
from Converter import convert_frequency_in_wave_number_when_transmitting as cfw_tx
from Converter import convert_frequency_in_wave_number_when_receiving as cfw_rx


class Currency_conv(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle("Конвертер волн в частоты и обратно")
        self.setWindowIcon(QIcon("pictures/icons8-ок-16.png"))
        self.ui.input_vawe_or_frequency.setPlaceholderText('Например: 17270')
        self.ui.output_vawe_or_frequency.setPlaceholderText('Результат:')
        self.ui.button_converter.clicked.connect(self.convert_value)

    def convert_value(self):
        check_value, input_value = self.\
            checking_the_correctness_of_the_entered_data()
        if check_value:
            input_formula = self.checking_combo_box()
            input_transponder = int(self.ui.choose_transponder.\
                currentText()[-1])
            if input_transponder == 0:
                input_transponder = 10 
            answer = input_formula(input_value, input_transponder)
            self.ui.output_vawe_or_frequency.setText(str(answer))

    def checking_the_correctness_of_the_entered_data(self):
        try:
            input_value = int(self.ui.input_vawe_or_frequency.text())
            if input_value < 0:
                self.ui.output_vawe_or_frequency.setText('Волна не может' +\
                     ' быть отрицательной')
                return False, input_value
            return True, input_value
        except ValueError:
            self.ui.output_vawe_or_frequency.setText('Вы должны ввести' +\
                     ' целое число')
            return False, 0     

    def checking_combo_box(self):
        dictionary_with_formulas = {"Номер волны в КГц (ПРМ)": cwn_rc,
                                    "Номер волны в КГц (ПРД)": cwn_ts,
                                    "КГц в номер волны (ПРМ)": cfw_rx,
                                    "КГц в номер волны (ПРД)": cfw_tx}
        input_formula = self.ui.choose_action.currentText()
        return dictionary_with_formulas.get(input_formula)

def main():
    app = QtWidgets.QApplication([])
    application = Currency_conv()
    application.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
