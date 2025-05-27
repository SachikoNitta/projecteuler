## 一辺が3の正方形のグリッドを考える
## rightかdownを選び、両方を3回ずつ選んだらルートを一個開拓したとみなす
## 全6回の選択でrightを3回、downを3回選ぶパターンは何通りあるか？
## 6個の空きスペースに3個のrightを入れると考えると、6C3 = (6 * 5 * 4) / (3 * 2 * 1) = 20通り
## 問題は20*20のグリッドなので、40個の空きスペースに20個のrightを入れると考えると、40C20 を計算すればよい

from math import factorial
def combinations(n, r):
    """n個の中からr個を選ぶ組み合わせの数を計算する"""
    return factorial(n) // (factorial(r) * factorial(n - r))
combinations_count = combinations(40, 20)
print(combinations_count)