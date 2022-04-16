import collections
import math


class Solution:
    def threeSumMulti(self, arr, target):
        arrayMap = collections.Counter(arr)
        res = 0
        combs = set()
        for i in arrayMap.keys():
            for j in arrayMap.keys():
                k = target-i-j
                if k in arrayMap.keys():
                    combs.add(tuple(sorted([i, j, k])))
        for c in combs:
            i, j, k = c[0], c[1], c[2]
            if i == j and i == k:
                res += math.comb(arrayMap[i], 3)
            elif i == j:
                res += math.comb(arrayMap[i], 2)*math.comb(arrayMap[k], 1)
            elif i == k:
                res += math.comb(arrayMap[i], 2)*math.comb(arrayMap[j], 1)
            elif k == j:
                res += math.comb(arrayMap[k], 2)*math.comb(arrayMap[i], 1)
            else:
                res += math.comb(arrayMap[i], 1) * \
                    math.comb(arrayMap[j], 1)*math.comb(arrayMap[k], 1)
        return res % 1000000007

#         c = Counter(arr)
#         res = 0
#         for i, j in itertools.combinations_with_replacement(c, 2):
#             k = target - i - j
#             if i == j == k: res += c[i] * (c[i] - 1) * (c[i] - 2) / 6
#             elif i == j != k: res += c[i] * (c[i] - 1) / 2 * c[k]
#             elif k > i and k > j: res += c[i] * c[j] * c[k]
#         return int(res % 1000000007)


arr = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
target = 8
sln = Solution()
print(sln.threeSumMulti(arr, target))
