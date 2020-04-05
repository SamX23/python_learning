# encapsulation is ensuring the data inside cannot be changed and accessed freely
class Data:
    # def get_data(index):
    def get_data(self,index, n):
        data = [1, 2, 3, 4, 5]
        data.append(n)
        # return data[index]

# print(Data.get_data(2))