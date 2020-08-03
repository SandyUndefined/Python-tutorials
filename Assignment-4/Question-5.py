def palindrome(n):
    print()
    return "Yes" if str(n)==str(n)[::-1] else "NO"


if __name__ == '__main__':
    print(palindrome(int(input())))