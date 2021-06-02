import re
class Conversor:
    def __init__(self):
        self.re_unidade_medida = "(?:ha|hectare|hectares|al|alqs|alqueire|alqueires|ac|acre|acres|milesimo|milésimo|milesimos|milésimos|lt|lts|litro|litros|milha|milhas|milha2|milha quadrada|milhas quadradas|decimo milesimo|décimo milésimo|decimos milesimos|décimos milésimos|decimo milesimos|décimo milésimos|selamim|salamim|celamim)"
        self.re_unidade_hectare = "(?:ha|hectare|hectares)"
        self.re_unidade_acre = "(?:ac|acre|acres)"
        self.re_unidade_alqueire = "(?:al|alqs|alqueire|alqueires)"
        self.re_unidade_litro = "(?:lt|lts|litro|litros)"
        self.re_unidade_milesimo = "(?:milesimo|milésimo|milesimos|milésimos)"
        self.re_unidade_decimo_milesimo = "(?:decimo milesimo|décimo milésimo|decimos milesimos|décimos milésimos|decimo milesimos|décimo milésimos)"
        self.re_unidade_milha = "(?:milha|milhas|milha2|milha quadrada|milhas quadradas)"
        self.re_unidade_salamim = "(?:selamim|salamim|celamim)"
        self.re_valores = "\d+(?:\.\d*)?"
    
    def verificar_unidades(self, texto):
        texto = texto.replace(",", ".")
        self.unidades = re.findall(self.re_unidade_medida, texto)
        self.valores = re.findall(self.re_valores, texto)
        return True if len(self.valores) == len(self.unidades) else False

    def devolver_calculo(self, unidade):
        if len(re.findall(self.re_unidade_acre, unidade)) > 0:
            return lambda a : a * 0.407

        if len(re.findall(self.re_unidade_hectare, unidade)) > 0:
            return lambda a : a

        if len(re.findall(self.re_unidade_salamim, unidade)) > 0:
            return lambda a : a * 0.15125

        if len(re.findall(self.re_unidade_alqueire, unidade)) > 0:
            return lambda a : a * 2.42

        if len(re.findall(self.re_unidade_litro, unidade)) > 0:
            return lambda a : a * 0.06

        if len(re.findall(self.re_unidade_decimo_milesimo, unidade)) > 0:
            return lambda a : (a / 10000) * 2.42

        if len(re.findall(self.re_unidade_milesimo, unidade)) > 0:
            return lambda a : (a / 1000) * 2.42

        if len(re.findall(self.re_unidade_milha, unidade)) > 0:
            return lambda a : a * 259.0
        
        return 0


    def converter(self, texto):
        area = 0.0
        if self.verificar_unidades(texto):
            for i in range(len(self.valores)):
                print(self.unidades[i])
                calculo = self.devolver_calculo(self.unidades[i])
                area += calculo(float(self.valores[i]))

            return "Valor convertido: {} ha".format(area)

        else:
             return "Não informou todas as unidades ou há unidades inválidas."

if __name__ == "__main__":
    texto = "2 alqs 472.4 milésimos" #20,207
    conv = Conversor()
    print(conv.converter(texto))
    
