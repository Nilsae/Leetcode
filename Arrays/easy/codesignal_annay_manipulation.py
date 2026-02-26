# You are given a list of n integers and a number k. Your task is to shuffle the array in such a way that, starting from the first element, every k-th element moves to the end of the array.

# For instance, if nums = [1, 2, 3, 4, 5, 6, 7, 8] and k = 3, the output should be [1, 2, 4, 5, 7, 8, 3, 6]. Here, the 3rd element 3 and the 6th element 6 (every 3rd element starting from the first) are moved to the end of the array.

def shuffle_array(nums, k):
    n = len(nums)
    k_list = []
    k_idx = k - 1
    while k_idx < n:
        k_list.append(k_idx)
        k_idx += k
    # print(k_list)
    num_k = len(k_list)
    tmp_list = []
    for i in range(num_k -1, -1, -1):
        k_idx = k_list[i]
        tmp_list.append(nums[k_idx])
        nums[k_idx:] = nums[k_idx+1:]
    # print(tmp_list)
    # print(nums)
    nums += tmp_list[::-1]
    return nums
        
# print(shuffle_array([1, 2, 3, 4, 5, 6, 7, 8], 3))





# You have been given an array of n integers. Your task is to write a function that reverses the array in groups of k size, and if the last group has fewer than k elements, reverse all of them. Return the newly organized array after the groups have been reversed.

# For example, given the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and k = 3, the output should be: [3, 2, 1, 6, 5, 4, 9, 8, 7, 10]. The first three elements are reversed to get [3, 2, 1], the next three become [6, 5, 4], the following three are [9, 8, 7], and the final one remains [10] as there are fewer than k elements remaining.
def solution(numbers, k):
    n = len(numbers)
    r = n//k
    # print(r)
    for i in range(r):
        # print(numbers[i * k - 1: i * (k+1)])
        numbers[i * k: (i+1) * k] = numbers[i * k: (i+1) * k][::-1]
    numbers[r * k:] = numbers[r * k:][::-1]
    return numbers

# print(solution([1, 2, 3, 4, 5, 6, 7], 3))



# You are given an array of n integers. Write a function that rearranges the array so that the middle half of the elements (considering the left and right quarters have been eliminated) move to the beginning of the array. The remaining elements, the left and right quarters, should move to the end of the array. If n is not divisible by 4, include the extra elements in the middle half.

# Specifically:

# Divide the array into four quarters.
# Move the second and third quarters to the front.
# Move the first and fourth quarters to the back.
# The function should modify the array in place.

# For example, if the input array is [1, 2, 3, 4, 5, 6, 7, 8], your function should rearrange the array to [3, 4, 5, 6, 1, 2, 7, 8].

# The solution should have a time complexity of 
# O
# (
# n
# )
# O(n).
def rearrange_array(nums):
    n = len(nums)  #4
    remainer = n % 4
    mid_portion = 2 *(n//4) + remainer
    print(n)
    print(mid_portion)
    wall_1 = (n - mid_portion)//2
    print(wall_1)
    wall_2 = wall_1 + mid_portion 
    first_q = nums[:wall_1]
    mid_q = nums[wall_1:wall_2]
    last_q = nums[wall_2:]
    print(first_q)
    print(mid_q)
    print(last_q)
    nums[:len(mid_q)] = mid_q
    nums[len(mid_q): len(mid_q) + len(first_q)] = first_q
    nums[len(mid_q) + len(first_q):] = last_q
    return nums

print(rearrange_array([1, 2, 3, 4, 5, 6, 7, 8, 9]))
