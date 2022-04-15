# https://leetcode.com/problems/valid-palindrome-ii/

def validPalindrome(s):
    # n=len(s)
    # ind=0
    # if s==s[::-1]:
    #     return True
    # while ind<n:
    #     x=s[:ind]+s[ind+1:]
    #     if x==x[::-1]:
    #         return True
    #     ind+=1
    # return False

    st, end = 0, len(s)-1
    if s == s[::-1]:
        return True
    while st <= end:
        if s[st] != s[end]:
            x1 = s[st+1:end+1]  # excluding start and including end
            x2 = s[st:end]  # including start and excluding end
            return x1 == x1[::-1] or x2 == x2[::-1]
        st += 1
        end -= 1
    return False


s = "abca"
print(validPalindrome(s))
