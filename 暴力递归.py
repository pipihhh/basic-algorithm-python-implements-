from math import sqrt


def move(n, cur, to, other):
    """
    汉诺塔问题
    :param n:有几个环
    :param cur: 环当前所在的柱子名
    :param to: 需要到达的柱子名
    :param other: 另一个柱子名
    :return:
    """
    if n == 1:
        print(f"1:{cur}->{to}")
        return
    move(n - 1, cur, other, to)
    print(f"{n}:{cur}->{to}")
    move(n - 1, other, to, cur)


move(4, "A", "C", "B")


def print_all_subsquence(string, index, ret, path):
    """
    打印字符串所有的子序列
    :param string: 字符串列表
    :param index: 字符串开始的索引
    :param ret: 答案列表
    :param path: 起始位置字符串 多为空字符串
    :return:
    """
    if index == len(string):
        ret.append(path)
        return
    print_all_subsquence(string, index + 1, ret, path)
    print_all_subsquence(string, index + 1, ret, path + string[index])


ret = []
print_all_subsquence(list("abc"), 0, ret, "")
print(ret)


def string_plzh(string_arr, path, ans, string_set):
    """
    打印字符串的所有排列组合
    :param string_arr:
    :param path:
    :param ans:
    :return:
    """
    if len(string_arr) == 1:
        res = path + string_arr[0]
        if res not in string_set:
            ans.append(res)
            string_set.add(res)
        return

    for s in string_arr:
        tmp_arr = string_arr[:]
        tmp_arr.remove(s)
        string_plzh(tmp_arr, path + s, ans, string_set)


ret = []
string_plzh(list("aac"), "", ret, set())
print(ret)


def sub_num(num, k):
    if num < 1 or k < 1:
        return 0
    if num == k or k == 1:
        return 1
    return sub_num(num - k, k) + sub_num(num - 1, k - 1)


ret = sub_num(5, 2)
print(ret)


def find_prime(arr, k, path, ans):
    if k == 0:
        ans.append(path)
        return
    if len(arr) == k:
        ans.append(sum(arr) + path)
        return
    # if k >= len(arr):
    #     return
    find_prime(arr[1:], k - 1, path + arr[0], ans)
    find_prime(arr[1:], k, path, ans)


def is_prime(num):
    tmp = 2
    target = sqrt(num)
    while tmp <= target:
        if num % tmp == 0:
            return False
        tmp += 1
    return True


def prime_in_list(arr, k):
    """
    给定一个数组和一个k数字，让数组中任意k个数字相加的和如果是素数，计数加一，返回这个计数
    :param arr: 给定的数组
    :param k: 给定的k
    :return: 素数的个数
    """
    ans = []
    find_prime(arr, k, 0, ans)
    count = 0
    for i in ans:
        if is_prime(i):
            count += 1
    return count


ret = prime_in_list([3, 7, 12, 19], 3)
print(ret)


def num2str(string):
    """
    给定一个纯数字的字符串，返回能有多少种字符串的组合方式，数字与字符串的对应为1-26为a-z
    :param string:
    :return:
    """
    str_map = {str(i): chr(96 + i) for i in range(1, 27)}

    def process(s, index):
        if index >= len(s) or index == len(s) - 1:
            return 1
        if s[index] == "0":
            return 0
        if s[index] == "1":
            ret1 = process(s, index + 1)
            ret2 = process(s, index + 2)
            return ret1 + ret2
        if s[index] == "2" and s[index + 1] <= "6":
            ret1 = process(s, index + 1)
            ret2 = process(s, index + 2)
            return ret1 + ret2
        return process(s, index + 1)

    return process(string, 0)


ret = num2str("32412312")
print(ret)


def backpack_problem(weights, values, bag):
    """
    给定一个weights数组和一个values数组本别表示一个物品的数量和对应的价值
    给定背包的重量为bag
    返回背包能装物品的最大价值为多少
    :param weights:
    :param values:
    :param bag:
    :return:
    """

    def process(w, v, rest, cur):
        if cur == len(w)-1:
            if rest > w[cur]:
                return v[cur]
            else:
                return 0
        if rest < w[cur]:
            return process(w, v, rest, cur+1)
        price1 = process(w, v, rest-w[cur], cur+1)
        price2 = process(w, v, rest, cur+1)
        return max(price1+v[cur], price2)
    return process(weights, values, bag, 0)


ret = backpack_problem([10, 5, 2], [100, 200, 50], 10)
print(ret)


def reverse_stack(stack, tmp_stack):
    """
    逆序一个栈，只能用递归的方式
    :param stack:
    :param tmp_stack:
    :return:
    """
    if not stack:
        return
    tmp_stack.append(stack.pop())
    reverse_stack(stack, tmp_stack)


ret = []
stack = [1, 2, 3, 4]
reverse_stack(stack, ret)
print(ret)


def pop_stack_bottom(stack):
    ret = stack.pop()
    if not stack:
        return ret
    last = pop_stack_bottom(stack)
    stack.append(ret)
    return last


def reverse_stack_2(stack):
    if not stack:
        return
    tmp = pop_stack_bottom(stack)
    reverse_stack_2(stack)
    stack.append(tmp)


ret = [1, 2, 3, 4]
reverse_stack_2(ret)
print(ret)


def num2str2(string):
    """
    给定一个纯数字的字符串，返回能有多少种字符串的组合方式，数字与字符串的对应为1-26为a-z
    :param string:
    :return:
    """
    str_map = {str(i): chr(96 + i) for i in range(1, 27)}

    def process(s, index, ans, path, db):
        if index >= len(s):
            if path not in db:
                ans.append(path)
                db.add(path)
            return
        if index == len(s) - 1:
            if path not in db:
                ans.append(path+str_map[s[index]])
                db.add(path)
            return
        if s[index] == "0":
            return
        if s[index] == "1":
            process(s, index + 1, ans, path+str_map["1"], db)
            process(s, index + 2, ans, path+str_map["1"+s[index+1]], db)
        if s[index] == "2" and s[index + 1] <= "6":
            process(s, index + 1, ans, path+str_map["2"], db)
            process(s, index + 2, ans, path+str_map["2"+s[index+1]], db)
        process(s, index + 1, ans, path+str_map[s[index]], db)

    ans = []
    process(string, 0, ans, "", set())
    return ans


ret = num2str2("21387201")
print(ret)


def first_hand(arr, left, right):
    if left == right:
        return arr[left]
    return max(arr[left] + second_hand(arr, left+1, right), arr[right] + second_hand(arr, left, right-1))


def second_hand(arr, left, right):
    if left == right:
        return 0
    return min(first_hand(arr, left+1, right), first_hand(arr, left, right-1))


ret = first_hand([7, 8, 100, 2], 0, 3)
print(ret)
