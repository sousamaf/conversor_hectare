import re

class Conversor:
    def __init__(self):
        self.re_unidade_medida = "(?:al|alqueire|alqueires|ac|acre|acres|lt|litro|litros)"
        self.re_valores = "\d+(?:\.\d*)?"

    def converter(self, texto):
        texto = texto.replace(",", ".")

        valores = re.findall(self.re_unidade_medida, texto)
        unidades = re.findall(self.re_valores, texto)

        if len(valores) == len(unidades):
            print("Potencial")
        else:
            print("faltando")

if __name__ == "__main__":
    conv = Conversor()
    conv.converter(input("Entrada: "))