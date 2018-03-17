# -*- coding: UTF-8 -*-


def time2second(timestr):
    items = [int(item) for item in timestr.split(":")]
    return items[0] * 60 * 60 + items[1] * 60 + items[2]


def first_and_last(M):
    first = 24 * 60 * 60
    last = 0
    daily_record = []
    for j in range(M):
        daily_record.append(input().split())
        if time2second(daily_record[j][1]) < first:
            first = time2second(daily_record[j][1])
            first_j = j
        if time2second(daily_record[j][2]) > last:
            last = time2second(daily_record[j][2])
            last_j = j
    return daily_record[first_j][0], daily_record[last_j][0]


def main():
    N = int(input())
    if not N:
        return 0
    result = []
    for i in range(N):
        M = int(input())
        if not M:
            return 0
        first, last = first_and_last(M)
        result.append([first, last])
    for i in result:
        print(i[0], i[1])


if __name__ == '__main__':
    main()
