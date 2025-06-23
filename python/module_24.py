# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 のlexicolographic順に並べたときの100万番目の数字を求める

from math import factorial
import time

def find_millionth_permutation():
    # 0から9までの数字のリスト
    remaining_digits = list(range(10))

    # 100万番目の数字の各桁
    millionth_num_digits = []
    
    # 現在の総順列数
    total_permutations = 0

    while remaining_digits:
        print(f"Remaining digits: {remaining_digits}, Total permutations so far: {total_permutations}")
        # 現在の桁に入れる数字の候補
        candidates = remaining_digits[:]

        while candidates:
            # 現在の桁に入れる数字の候補から最小値を取得
            n = min(candidates)
            print(f"Current candidates: {candidates}, Selected digit: {n}")

            # 残りの数字で作れる順列の数
            num_permutations = factorial(len(remaining_digits) - 1)
            print(f"Number of permutations with {n} at current position: {num_permutations}")

            # 順列の数を足しても100万以下になる場合は次の候補を確認
            if num_permutations + total_permutations < 1000000:
                total_permutations += num_permutations
                candidates.remove(n)

            # 100万を超える場合はその数字を確定し、次の桁へ
            else:
                millionth_num_digits.append(n)
                remaining_digits.remove(n)
                break

        
    return ''.join(map(str, millionth_num_digits))

if __name__ == "__main__":
    start = time.time()
    result = find_millionth_permutation()
    end = time.time()
    print(result)
    print(f"処理時間: {end - start} 秒")