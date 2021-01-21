# NIESKOŃCZONE ZADANIE
import xml.dom.minidom as xml


class CurrencyExchange:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file = xml.parse(file_path)
        self.currency_name = self.file.getElementsByTagName("nazwa_waluty")
        self.currency_code = self.file.getElementsByTagName("kod_waluty")
        self.rate = self.file.getElementsByTagName("przelicznik")
        self.average_exchange_rate = self.file.getElementsByTagName(
            "kurs_sredni")

    def test(self):
        for index, element in enumerate(self.currency_name):
            print(element.firstChild.data,
                  self.currency_code[index].firstChild.data)


c_exchange = CurrencyExchange("kursy.xml")
c_exchange.test()
