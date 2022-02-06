import math


def sum_seq(first: int, last: int) -> int:
    num = last - first + 1
    return (first + last) * num // 2


def main():
    DIV = 998244353
    N = int(input())

    Ndig = int(math.log10(N)) + 1

    ans = 0
    for d in range(1, Ndig + 1):
        # Calc sum sequence with the digit
        first = 1
        last = (
            pow(10, d) - 1 - (pow(10, d - 1) - 1)
            if d < Ndig
            else N - (pow(10, d - 1) - 1)
        )
        ans += sum_seq(first, last) % DIV
        ans %= DIV

    print(ans)


if __name__ == "__main__":
    main()
