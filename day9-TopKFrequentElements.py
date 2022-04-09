def topKFrequent(nums, k):

    # first solution:

    # first make counter dictionary
    # then sort the nums list with descending freq ie with highest freq first
    # then make a dictinory with that list so
    # items with highest freq are arranged
    # then extract required key numbers from that dict

    # mapp=Counter(nums)
    # nums.sort(key= lambda x: (-mapp[x],x))
    # dictionay=Counter(nums)
    # return (list(dictionay.keys())[:k])

    # 2nd Solution:

    # take count dictionary:
    # then make a freq list so that index denotes freq of element
    # and item is list of numbers having that freq
    # now iterate from backwards and into that each list and append result list
    # once the len is equal to k return
    # index           1   2   3   4   5   6
    # val(arr of nums)   [3] [2] [1]

    count = {}
    freq = [[] for i in range(len(nums)+1)]

    for items in nums:
        count[items] = 1+count.get(items, 0)
    for item, occurance in count.items():
        freq[occurance].append(item)

    res = []
    for i in range(len(freq)-1, 0, -1):
        for item in freq[i]:
            res.append(item)
            if len(res) == k:
                return res


nums = [1, 1, 1, 2, 2, 3]
k = 2
print(topKFrequent(nums, k))
