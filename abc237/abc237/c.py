def main():
    S = input()

    ans = "No"
    if is_palindrome(S):
        ans = "Yes"
    else:
        head_a_len = 0
        for i in range(len(S)):
            if S[i] != "a":
                head_a_len = i
                break
        tail_a_len = 0
        for i in range(len(S)):
            if S[len(S) - 1 - i] != "a":
                tail_a_len = i
                break
        if head_a_len <= tail_a_len:
            padded = "a" * (tail_a_len - head_a_len) + S
            if is_palindrome(padded):
                ans = "Yes"
    print(ans)


def is_palindrome(s: str) -> bool:
    si = 0
    ei = len(s) - 1
    while si < ei:
        if s[si] != s[ei]:
            return False
        si += 1
        ei -= 1
    return True


if __name__ == "__main__":
    main()
