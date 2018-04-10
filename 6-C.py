def solution(n):
    # 三个队列分别存储3 * x, 5 * x, 7 * x
    q3 = [3]
    q5 = [5]
    q7 = [7]
    res = 3
    count = -1
    while res <= n:
        res = min(q3[0], q5[0], q7[0])  # 找出队头最小元素
        if res in q3:       # 如果最小在q3中
            q3 = q3[1:]     # q3队头出队
            q3.append(3 * res)
            q5.append(5 * res)
            q7.append(7 * res)
        elif res in q5:     # 同上
            q5 = q5[1:]
            q5.append(5 * res)
            q7.append(7 * res)
        elif res in q7:     # 同上
            q7 = q7[1:]
            q7.append(7 * res)
        count += 1
    return count


if __name__ == '__main__':
    n = int(input())
    print(solution(n))
