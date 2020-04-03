# init executes if using [class_name]() format
class apple():
    print('This is an opening')
    # self = the class 'apple'
    # init = apple(args, args, args)
    def __init__(self, warna, bentuk, stok):
        # apple.color
        self.color = warna
        # apple.shape
        self.shape = bentuk
        # apple.stock
        self.stock = stok

    print('This is a middle')

    # apple(args).cetak()
    def cetak(self):
        print(self.color)
        print(self.shape)
        print(self.stock)
        print()

    # apple(args).rot(args)
    # apple.mold
    def rot(self, days, temperature):
        self.mold = days * (temperature * .1)

# method 1
apple('Red', 'Bulat', 'Banyaklah').cetak()
# method 2
apple = apple('Hijau', 'lonjong', 'sedikit')
apple.cetak()
print(apple.color)
print(apple.stock)

apple.rot(5, 35)
print(apple.mold)