import sys
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi

class POSFunctions:
    def __init__(self, ui):
        self.ui = ui
        self.cart_items = []

        self.products = {
            "" : 0,
            "Bimoli (Rp. 20,000)": 20000,
            "Kecap ABC (Rp. 7,000)": 7000,
            "Indomie Goreng (Rp. 3,500)": 3500,
            "Susu Ultra (Rp. 8,000)": 8000
        }

        self.add_products()
        self.add_discounts()

        self.ui.pushButton.clicked.connect(self.add_to_cart)
        self.ui.pushButton_2.clicked.connect(self.clear_cart)

    def add_products(self):
        self.ui.comboBox.clear()
        for product in self.products.keys():
            self.ui.comboBox.addItem(product)

    def add_discounts(self):
        self.ui.comboBox_2.clear()
        discount_options = ["0%", "5%", "10%", "15%", "20%"]
        for discount in discount_options:
            self.ui.comboBox_2.addItem(discount)

    def add_to_cart(self):
        product = self.ui.comboBox.currentText()
        quantity = self.ui.textEdit_2.toPlainText()
        discount = self.ui.comboBox_2.currentText()

        if not quantity.isdigit():
            self.ui.label_4.setText("Invalid quantity")
            return
        quantity = int(quantity)

        if product in self.products:
            price = self.products[product]
        else:
            return

        discount_value = int(discount.replace('%', ''))
        total_price = quantity * price * (1 - discount_value / 100)

        self.cart_items.append(total_price)

        item_text = f"{product} (Rp. {price:,}) - {quantity} x Rp. {price:,} (disc {discount})"
        self.ui.listWidget.addItem(QListWidgetItem(item_text))

        self.update_total()

    def update_total(self):
        total_price = sum(self.cart_items)
        self.ui.label_4.setText(f"Total: Rp. {total_price:,.0f}")

    def clear_cart(self):
        self.cart_items.clear()
        self.ui.listWidget.clear()
        self.update_total()


class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        loadUi("POS.ui", self)
        self.setWindowTitle("POS Application (F1D022095)")

        self.pos_functions = POSFunctions(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainUI()
    window.show()
    sys.exit(app.exec_())