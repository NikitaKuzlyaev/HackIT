def to_roman(n):
    if n <= 0 or n > 3999:
        return (1 / 0)  # self check

    roman_numerals = {
        1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
        100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
        10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
    }

    result = ''
    for value in sorted(roman_numerals.keys(), reverse=True):
        while n >= value:
            result += roman_numerals[value]
            n -= value

    return result


def solve():
    n = int(input())

    d = {"M": 4, "I": 1, "C": 2, "D": 3, "V": 2, "L": 2, "X": 2}

    res = 0
    for i in range(1, n + 1):
        rr = to_roman(i)
        for j in rr:
            res += d[j]

    print(res)


if __name__ == "__main__":
    solve()
