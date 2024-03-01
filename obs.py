import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit, QTableWidget, QTableWidgetItem, QHBoxLayout, QFileDialog

class OgrenciBilgiSistemi(QWidget):
    def __init__(self):
        super().__init__()

        self.ogrenciler = []

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.label_adi_soyadi = QLabel('Adı Soyadı:')
        self.edit_adi_soyadi = QLineEdit(self)

        self.label_numara = QLabel('Öğrenci Numarası:')
        self.edit_numara = QLineEdit(self)

        self.label_sinif = QLabel('Sınıf:')
        self.edit_sinif = QLineEdit(self)

        self.label_not = QLabel('Not:')
        self.edit_not = QLineEdit(self)

        self.button_ogrenci_ekle = QPushButton('Öğrenci Ekle', self)
        self.button_ogrenci_ekle.clicked.connect(self.ogrenci_ekle)

        self.table_ogrenciler = QTableWidget(self)
        self.table_ogrenciler.setColumnCount(4)
        self.table_ogrenciler.setHorizontalHeaderLabels(['Adı Soyadı', 'Numara', 'Sınıf', 'Not'])

        self.button_dosyaya_kaydet = QPushButton('Dosyaya Kaydet', self)
        self.button_dosyaya_kaydet.clicked.connect(self.dosyaya_kaydet)

        layout.addWidget(self.label_adi_soyadi)
        layout.addWidget(self.edit_adi_soyadi)
        layout.addWidget(self.label_numara)
        layout.addWidget(self.edit_numara)
        layout.addWidget(self.label_sinif)
        layout.addWidget(self.edit_sinif)
        layout.addWidget(self.label_not)
        layout.addWidget(self.edit_not)
        layout.addWidget(self.button_ogrenci_ekle)
        layout.addWidget(self.table_ogrenciler)
        layout.addWidget(self.button_dosyaya_kaydet)

        self.setLayout(layout)

        self.show()

    def ogrenci_ekle(self):
        adi_soyadi = self.edit_adi_soyadi.text()
        numara = self.edit_numara.text()
        sinif = self.edit_sinif.text()
        notu = self.edit_not.text()

        self.ogrenciler.append({'Adı Soyadı': adi_soyadi, 'Numara': numara, 'Sınıf': sinif, 'Not': notu})

        self.guncelle_tablo()

        # Ekledikten sonra alanları temizle
        self.edit_adi_soyadi.clear()
        self.edit_numara.clear()
        self.edit_sinif.clear()
        self.edit_not.clear()

    def guncelle_tablo(self):
        self.table_ogrenciler.setRowCount(len(self.ogrenciler))

        for row, ogrenci in enumerate(self.ogrenciler):
            self.table_ogrenciler.setItem(row, 0, QTableWidgetItem(ogrenci['Adı Soyadı']))
            self.table_ogrenciler.setItem(row, 1, QTableWidgetItem(ogrenci['Numara']))
            self.table_ogrenciler.setItem(row, 2, QTableWidgetItem(ogrenci['Sınıf']))
            self.table_ogrenciler.setItem(row, 3, QTableWidgetItem(ogrenci['Not']))

    def dosyaya_kaydet(self):
        dosya_adı, _ = QFileDialog.getSaveFileName(self, 'Dosyayı Kaydet', '', 'CSV Dosyaları (*.csv)')

        if dosya_adı:
            with open(dosya_adı, 'w') as file:
                for ogrenci in self.ogrenciler:
                    file.write(f"{ogrenci['Adı Soyadı']},{ogrenci['Numara']},{ogrenci['Sınıf']},{ogrenci['Not']}\n")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    uygulama = OgrenciBilgiSistemi()
    sys.exit(app.exec_())