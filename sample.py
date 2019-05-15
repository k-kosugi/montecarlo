# coding=utf-8
import numpy as np
from matplotlib import pyplot as plt
import time
import sys
import codecs

# 標準出力の先をUTF-8に変更する
sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# 半径1の円の内側にあるか外側にあるかを判定するための関数
# x^2 + y^2 = z^2が三平方の定理で、現時点でz=1
def is_inner(x, y):
    return x ** 2 + y ** 2 < 1

# 開始時間
start = time.time()

# 内部にプロットした点の数
inner_points_cnt = 0

# すべてのプロットした点の数
all_points_cnt = 0

# ランダム関数を利用して、xとyに点をランダムにプロットする。
X, Y = np.random.rand(2, 10 ** 3)

for x, y in zip(X, Y):
    all_points_cnt += 1
    if is_inner(x, y):
        inner_points_cnt += 1

# 終了時刻
end = time.time()

# 計算にかかった時間
elasted_time = end - start

# 標準出力に計算にかかった時間を出力
print("elapsed_time = :{0}".format(elasted_time) + "[sec]")

# 円の内側にプロットした総数を標準出力
print(inner_points_cnt)
print(all_points_cnt)

pi = float(4) * inner_points_cnt / all_points_cnt

print u'pi'
print ':{0}'.format(pi)

plt.scatter(X, Y, s=1)

cx = np.linspace(0, 1, 100)
cy = np.sqrt(np.subtract(1, cx ** 2))
plt.plot(cx, cy, linewidth=3, color='r')

plt.gca().set_aspect('equal', adjustable='box')

plt.show()
