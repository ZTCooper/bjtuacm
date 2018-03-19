# -*- coding: UTF-8 -*-
# 模拟竖式除法，余数之前出现过则为循环节


def divide(a, b):
    quotient = []
    remainder = []
    quotient.append(divmod(a, b)[0])
    remainder.append(divmod(a, b)[1])
    for i in range(100):
        if remainder[-1] * 10 % b not in remainder:
            quotient.append(divmod(remainder[-1] * 10, b)[0])
            remainder.append(divmod(remainder[-1] * 10, b)[1])
    result = str(quotient[0]) + "."
    if remainder[-1] * 10 % b not in remainder:
        for i in quotient[1:]:
            result += str(i)
        return result
    quotient.append(divmod(remainder[-1] * 10, b)[0])
    remainder.append(divmod(remainder[-1] * 10, b)[1])
    circular = quotient[remainder[1:].index(
        remainder[-1] * 10 % b) + 1:]

    for i in quotient[1:remainder.index(remainder[-1] * 10 % b)]:
        result += str(i)
    result += "("
    for i in circular:
        result += str(i)
    result += ")"
    return result


def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    if a % b == 0:
        print(a // b)
    else:
        print(divide(a, b))


if __name__ == '__main__':
    main()
