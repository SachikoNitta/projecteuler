import time

MAX_NUM = 28123

# 豊富数を求める関数
def getAbundantNumbers():
    divisor_sum = [0] * (MAX_NUM + 1)
    for i in range(1, MAX_NUM // 2 + 1):
        for j in range(i * 2, MAX_NUM + 1, i):
            divisor_sum[j] += i
    return [i for i in range(1, MAX_NUM + 1) if divisor_sum[i] > i]

def main():
    # 28123以下の豊富数を取得
    abundant = getAbundantNumbers()
    # 豊富数の和で表せない数の合計を求める
    abundant_set = set(abundant)
    can_be_written = [False] * (MAX_NUM + 1)
    for i in abundant:
        for j in abundant:
            s = i + j
            if s > MAX_NUM:
                break
            can_be_written[s] = True
    # 1から28123までの数のうち、豊富数の和で表せないものを合計
    total = sum(i for i, x in enumerate(can_be_written) if i >= 1 and not x)
    print(f"合計: {total}")

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(f"処理時間: {end - start:.2f}秒")
