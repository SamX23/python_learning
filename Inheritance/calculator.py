class calculator:
    def __init__(self, nilai=0):
        self.nilai = nilai

    def add_num(self, num1, num2):
        self.nilai = num1 + num2
        if self.nilai > 9:
            print('Sudah melebihi batas angka: {}'.format(self.nilai))
        return self.nilai


class calculatorx(calculator):

    def m_num(self, num1, num2):
        self.nilai = num1 * num2
        return self.nilai

    # overrie
    def add_num(self, num1, num2):
        self.nilai = num1 + num2
        return self.nilai


calcX = calculatorx()
a = calcX.m_num(2, 3)
print('Perkalian: ', a)

b = calcX.add_num(2, 3)
print('Penjumlahan: ', b)
