# https://leetcode.com/problems/reverse-string/

def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    st, end = 0, len(s)-1
    while st <= end:
        s[st], s[end] = s[end], s[st]
        st += 1
        end -= 1

    # only for local, return string
    return s


s = ["h", "e", "l", "l", "o"]
print(reverseString(s))
