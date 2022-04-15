from itertools import permutations


def nextPermutation(nums):
    """
    Do not return anything, modify nums in-place instead.
    """

    # lst=list(set(permutations(nums)))
    # lst.sort(key=str)
    # ind=lst.index(tuple(nums))
    # if ind==(len(lst)-1):
    #     nums[:]=lst[0]
    # else:
    #     nums[:]=lst[ind+1]

    i = j = len(nums)-1
    while i > 0 and nums[i-1] >= nums[i]:
        i -= 1

    # if all values are decreasing i will become 0
    # in that case we will just reverse the list

    if i == 0:
        nums.reverse()
        return

    # else we will find j and swap it
    # now our pivot is the left element of i as while loop break out at i not pivot

    while nums[j] <= nums[i-1]:
        j -= 1

    nums[j], nums[i-1] = nums[i-1], nums[j]

    nums[i:] = nums[len(nums)-1: i-1:-1]

    print(nums)


nums = [1, 1, 5]
print(nextPermutation(nums))
