"""
给定一个字符串，返回该字符串最长回文子串的长度
时间复杂度big O(n)
"""


def manacher(string: str) -> int:
    s = "#"
    s += "#".join(list(string))
    s += "#"
    length_arr = [None for _ in range(len(s))]
    r = -1
    cur = -1
    ret = 1
    for i in range(len(s)):
        if i > r:
            left = i - 1
            right = i + 1
            r = i
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    r = right
                    right += 1
                    left -= 1
                else:
                    break
            length_arr[i] = right - left - 1
            cur = i
        elif i < r and (2*cur - r) < 2*cur - i - (length_arr[2*cur - i] // 2):
            length_arr[i] = length_arr[2*cur - i]
        elif i > r and (2*cur - r) > 2*cur - i - (length_arr[2*cur - i] // 2):
            length_arr[i] = 2*(r - i) + 1
        else:
            left = 2*i - r - 1
            right = r + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    r = right
                    right += 1
                    left -= 1
                else:
                    break
            length_arr[i] = right - left - 1
            cur = i
        ret = length_arr[i] if length_arr[i] > ret else ret
    return ret // 2


ret = manacher("abba")
print(ret)
