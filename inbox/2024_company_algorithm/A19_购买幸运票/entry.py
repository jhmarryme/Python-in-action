'''
我希望您能够充当算法工程师，使用python解答算法题。给出可运行在codeCampus上的嗯代码，并提供解题思路。
需要最高优先级保证代码的正确性，同时尽可能多的考虑多种输入的运行情况。
题目信息如下：

如果一张彩票号码由2n位数字组成，前n位数字的和等于后n位数字的和，则成为一张幸运票
小明想要收藏一张这样的彩票，他买了一张票，检查了号码，如果不是幸运票，再购买几张连续号码的票。请问小明最少需要再买多少张额外的票才能买到幸运票？
其中：1 <= n <= 4

输入
包含一行2n位数字（这是第一张票的号码）

输出
还需要额外购买的票的数量

输入样例
125070

输出样例
1

函数定义风格:
def luckyTicket(n):
    return 0


'''
# 答案正确
def is_lucky_ticket(ticket, n):
    first_half_sum = sum(int(digit) for digit in ticket[:n])
    second_half_sum = sum(int(digit) for digit in ticket[n:])

    return first_half_sum == second_half_sum

def luckyTicket(n):
    ticket = str(n)
    n = len(ticket) // 2

    extra_tickets = 0

    current_ticket = ticket

    while not is_lucky_ticket(current_ticket, n):
        extra_tickets += 1

        current_ticket = str(int(current_ticket) + 1).zfill(2 * n)

    return extra_tickets

# 示例测试
print(luckyTicket(125070))  # 应输出 1