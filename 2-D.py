# -*- coding: UTF-8 -*-


def equation_format(equa):
    equa_list = list(equa)
    eq = ""
    j = 0
    for i in range(len(equa)):
        if equa[i].isalpha():
            var = equa[i]
            if not equa[i - 1].isnumeric():
                equa_list.insert(i + j, "1*")
                j += 1
            else:
                equa_list.insert(i + j, "*")
                j += 1
    for i in equa_list:
        eq += i
    return eq, var


# 解方程的奇淫技巧
def solve(eq, var):
    eq1 = eq.replace("=", "-(") + ")"
    c = eval(eq1, {var: 1j})
    return -c.real / c.imag


def main():
    equation = input()
    eq, var = equation_format(equation)
    print(var + "=" + "%.3f" % solve(eq, var))


if __name__ == '__main__':
    main()
