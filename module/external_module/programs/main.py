from sys import path

path.append('C:\\Users\\USER\\PycharmProjects\\python\\module\\external_module\\modules')
print(path)

import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]

print(module.suml(zeroes))
print(module.prodl(ones))