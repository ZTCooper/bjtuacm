# -*- coding: UTF-8 -*-
# 这个方法太过暴力，有待改进


def make_cube(num, n):
    big_cube = []
    for i in range(9):
        row = input().split()
        big_cube.append(row)
    if num != n - 1:
        input()
    return big_cube


def check_row(big_cube):
    for i in range(9):
        if (len(set(big_cube[i])) < 9):
            return "Wrong"
    return "Right"


def check_column(big_cube):
    column = [[], [], [], [], [], [], [], [], []]
    for i in range(9):
        column[0].append(big_cube[i][0])
        column[1].append(big_cube[i][1])
        column[2].append(big_cube[i][2])
        column[3].append(big_cube[i][3])
        column[4].append(big_cube[i][4])
        column[5].append(big_cube[i][5])
        column[6].append(big_cube[i][6])
        column[7].append(big_cube[i][7])
        column[8].append(big_cube[i][8])
    if ((len(set(column[0])) + len(set(column[0])) + len(set(column[0])) + len(set(column[0])) + len(set(column[0])) + len(set(column[0])) + len(set(column[0])) + len(set(column[0]))) < 72):
        return "Wrong"
    return "Right"


def check_smallCube(big_cube):
    small_cube = [[], [], [], [], [], [], [], [], []]
    for i in range(3):
        for j in range(3):
            small_cube[0].append(big_cube[i][j])
        for j in range(3, 6):
            small_cube[1].append(big_cube[i][j])
        for j in range(6, 9):
            small_cube[2].append(big_cube[i][j])
    for i in range(3, 6):
        for j in range(3):
            small_cube[3].append(big_cube[i][j])
        for j in range(3, 6):
            small_cube[4].append(big_cube[i][j])
        for j in range(6, 9):
            small_cube[5].append(big_cube[i][j])
    for i in range(6, 9):
        for j in range(3):
            small_cube[6].append(big_cube[i][j])
        for j in range(3, 6):
            small_cube[7].append(big_cube[i][j])
        for j in range(6, 9):
            small_cube[8].append(big_cube[i][j])
    if ((len(set(small_cube[0])) < 9) or (len(set(small_cube[1])) < 9) or (len(set(small_cube[2])) < 9) or (len(set(small_cube[3])) < 9) or (len(set(small_cube[4])) < 9) or (len(set(small_cube[5])) < 9) or (len(set(small_cube[6])) < 9) or (len(set(small_cube[7])) < 9) or (len(set(small_cube[8])) < 9)):
        return "Wrong"
    return "Right"


def main():
    n = int(input())
    answers = []
    for num in range(n):
        cube = make_cube(num, n)
        check_r = check_row(cube)
        check_c = check_column(cube)
        check_s = check_smallCube(cube)

        if check_r == "Right" and check_c == "Right" and check_s == "Right":
            answers.append("Right")
        elif check_r == "Wrong" or check_c == "Wrong" or check_s == "Wrong":
            answers.append("Wrong")
    for answer in answers:
        print(answer)


if __name__ == '__main__':
    main()
