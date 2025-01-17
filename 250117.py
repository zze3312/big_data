import os.path
import random
import time
import numpy as np

i = 1
print(f'i의 타입 : {type(i)}')
print(f'i의 주소 : {id(i)}')

a = "hello"
b = "hello"

print(f'a의 주소 : {id(a)}')
print(f'b의 주소 : {id(b)}')

print(f'a == b : {a == b}')
print(f'a is b : {a is b}')

a += ","
b += ","

print(f'a의 주소 : {id(a)}')
print(f'b의 주소 : {id(b)}')

print(f'a == b : {a == b}')
print(f'a is b : {a is b}')

def tmp() -> None:
    pass
n = None
for i in range(2):
    print(f'id(tmp()) : {id(tmp())}')

print(f'id(n) : {id(n)}')


list_ = [1, 2, 3]
for i in list_:
    print(f'i : {i}')

###iterable 속성을 받았다는건 상속을 받은 것인가??###

a = iter(list_)
print(next(a))
print(next(a))
print(next(a))
#print(next(a))

def tmp(x):
    return x + 10

m = map(tmp, list_)

print(f'next(m) : {next(m)}')
#print(f'm[1] : {m[1]}')

# import cv2
#
# img_path = ["./img/img_1", "./img/img_2"]
#
# def generator(list_):
#     for path in list_:
#         img = cv2.imread(path)
#         yield  img
#
# gen = generator(img_path)
# for i in gen:
#     print(i)


i = 257
print(f'i == i + 1 - 1 : {i == i + 1 - 1}')
print(f'i is i + 1 - 1 : {i is i + 1 - 1}')
print('---------------------')
i = 257
a = i
print(f'i == a : {i == a}')
print(f'i is a : {i is a}')
print('---------------------')
print(f'i + 1 - 1 == a : {i + 1 - 1 == a}' )
print(f'i + 1 - 1 is a : {i + 1 - 1 is a}')
print('---------------------')
a = []
b = []
print(f'a is b : {a is b}')
print('---------------------')

# 얕은복사에 의한 오류
tmp = []
list_ = []

for i in range(5):
    for j in range(5):
        tmp.append(j)
    list_.append(tmp)
    tmp.clear()

# [[], [], [], [], []]
print(list_)

# 깊은복사로 변경
tmp = []
list_ = []

for i in range(5):
    for j in range(5):
        tmp.append(j)
    list_.append(tmp[:])
    tmp.clear()

# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
print(list_)

list_ = []
for i in range(5):
    tmp = []
    for j in range(5):
        tmp.append(j)
    list_.append(tmp)

# [[0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4], [0, 1, 2, 3, 4]]
print(list_)

# Comprehension > for문을 돌리는 것보다 빠름(list, dict, set,  등 이런방식을 사용하는 것이 빠름)
list_ = [i for i in range(100000)]
dict_ = {i : i ** 2 for i in range(100000)}
set_ = {random.randint(1, 99999) for i in range(100000)}
generator_ = (i for i in range(100000))


# 0.04249429702758789
start = time.time()
list_ = [i for i in range(1000000)]
print(time.time() - start)

# 0.09060096740722656
start = time.time()
list_ = []
for i in range(1000000):
    list_.append(i)
print(time.time() - start)

# 0.0448451042175293
start = time.time()
list_ = list(range(1000000))
print(time.time() - start)

# lambda
def tmp():
    return 0

print(tmp)

print(f'(lambda  x : x + 2)(2) : {(lambda  x : x + 2)(2)}')

def square(x):
    return x ** 2

list_ = [1, 2, 3, 4, 5]

for i in map(square, list_):
    print(i)

def square(x, y) :
    return x ** y
for i in map(lambda x : square(x, x), list_):
    print(i)


x1 = np.add(1, 2)
print(f'x1 : {x1}')

x2 = np.add([1], [2])
print(f'x2 : {x2}')

x3 = np.add([[1]], [[2]])
print(f'x3 : {x3}')

x4 = np.add([[1, 2]], [[3], [4]])
print(f'x4 : {x4}')

x5 = np.array([[1, 2]]) + np.array([[3], [4]])
print(f'x5 : {x5}')

print([1] + [2])

x1 = np.zeros(4)
print(f'x1 : {x1}')

x2 = np.ones((1, 4), dtype=np.int32)
print(f'x2 : {x2}')

x3 = np.arange(1, 9, dtype='int64').reshape((2, 4))
print(f'x3 : {x3}')

print(f'x3[0] : {x3[0]}')
print(f'x3[0][0] : {x3[0][0]}')
print(f'x3[0][1:3] : {x3[0][1:3]}')
print(f'np.sum(x3) : {np.sum(x3)}')
print(f'np.mean(x3) : {np.mean(x3)}')
print(f'np.var(x3) : {np.var(x3)}')
print(f'np.max(x3) : {np.max(x3)}')
print(f'np.argmax(x3) : {np.argmax(x3)}')

x = np.zeros((3, 3))
x1 = np.insert(x, 3, 1, axis = 1)
print(f'x1 : {x1}')
x2 = np.insert(x, 3, 1, axis = 0)
print(f'x2 : {x2}')
x3 = np.insert(x, 1, 1, axis = 0)
print(f'x3 : {x3}')
x4 = np.insert(x, 3, [1, 2, 3], axis = 1)
print(f'x4 : {x4}')

x_c = x.copy()
for i in range(3):
    for j in range(3):
        x_c[i][j] = i * j

print(x_c)

x_c[0][0] = 1
x_c[1, 1] = 2
print(x_c)

x_c[0] = 1
print(x_c)

x_c[:, 0] = [1, 2, 3]
print(x_c)

list_ = [3, 2, 1]
print(sorted(list_))
print(list_)
print('--------------------')
print(list_.sort())
print(list_)

print(x_c > 2)
print(x_c > [1, 2, 3])

print(x_c)

x_c[x_c == 1] = 0
print(x_c)

np.putmask(x_c, x_c > 2, [9, 8, 7])
print(x_c)

np.place(x_c, x_c > 2, [9, 8, 7])
print(x_c)

np.putmask(x_c, x_c > 2, x_c ** 2)
print(x_c)

x1 = np.delete(x_c, 4)
print(x1)

x2 = np.delete(x_c, 0, axis = 0)
print(x2)

x3 = np.delete(x_c, 0, axis = 1)
print(x3)

x_c2 = x_c.copy()
x_c2[x_c2 == 2] = np.nan
print(x_c2)

x_c2 = x_c.copy()
x_c2[x_c2 == 2] = np.nan
print(x_c)
print(x_c2)

x_c_plus_y = np.concatenate([x_c, x_c2], axis = 0)
print(x_c_plus_y)

x_c_plus_x = np.concatenate([x_c, x_c2], axis = 1)
print(x_c_plus_x)

import pandas as pd

pd.set_option("display.max_row", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.expand_frame_repr", False)

df = pd.read_csv(os.path.join('titanic.csv'))
print(df)
print(df["PassengerId"])

print('-' * 50)
print(df.loc[0])
print('-' * 50)
print(df.iloc[0])
print('-' * 50)
print(df[df['Sex'] == 'male'])
print('-' * 50)
print(df['Sex'] == 'male')

print(f'df.count() : {df.count()}')
print(f'df.iloc[1].values : {df.iloc[1].values}')
print(f'df["Fare"].mean() : {df["Fare"].mean()}')
print(f'df["Fare"].max() : {df["Fare"].max()}')
print(f'df["Fare"].argmax() : {df["Fare"].argmax()}')
print(f'df.corr(numeric_only=True) : \n{df.corr(numeric_only=True)}')

def change_value(row):
    if row["Sex"] == "male":
        row["Sex"] = 1
    else:
        row["Sex"] = 0
    return row

print()
df = df.apply(change_value, axis = 1)
print(df.corr(numeric_only=True)["Survived"])
