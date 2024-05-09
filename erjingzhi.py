# -*- coding: utf-8 -*-
# @Author: JogFeelingVI
# @Date:   2024-05-08 22:21:02
# @Last Modified by:   JogFeelingVI
# @Last Modified time: 2024-05-08 22:59:57


def convert_to_binary(num: int):
    """
    将数字转换为二进制字符串。

    Args:
        num: 要转换的数字。

    Returns:
        二进制字符串表示形式。
    """
    return format(num, "06b")


def binary_to_decimal(binary_string: str):
    """
    将二进制字符串转换为十进制整数。

    Args:
        binary_string: 要转换的二进制字符串。

    Returns:
        相应的十进制整数。
    """
    return int(binary_string, 2)


def levenshtein_distance(bina: str, binb: str):
    """
    计算两个列表的编辑距离。
    """
    m = len(bina)
    n = len(binb)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if bina[i - 1] == binb[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    return dp[m][n]


def main():
    tmp = ""
    bls = [11, 6, 10, 10, 13, 6, 13, 5, 4, 10, 2, 16, 5, 4, 6, 2, 13, 2, 10, 2, 16, 14, 8, 6, 3, 15, 15, 2, 11, 2, 6]
    ctobin = [[x, convert_to_binary(x)] for x in bls]
    print("convert_to_binary")
    dp = 0
    for k, bins in ctobin:
        if tmp != "":
            dp = levenshtein_distance(bins, tmp)
        print(f"{k:>2}: {bins} {dp}")
        tmp = bins


def temp_bit7():
    bins = [6, "000110"]
    tmp = []
    for n in range(1, 17):
        bin_n = convert_to_binary(n)
        dp_n = levenshtein_distance(bins[1], bin_n)
        if dp_n == 2:
            tmp.append(f"{n:>02}, {bin_n}, {dp_n}")
            print(f"{tmp[-1]}")


if __name__ == "__main__":
    temp_bit7()
