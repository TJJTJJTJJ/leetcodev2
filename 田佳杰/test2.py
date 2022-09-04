import functools
def compare(x, y):
    xx = x+y
    yy = y+x
    n = len(xx)
    for i in range(n):
        if int(xx[i]) < int(yy[i]):
            return -1
        elif int(xx[i]) > int(yy[i]):
            return 1
    return 1
def compare2(x):
    n = len(x)
    return int(x)/(10**n-1)
def cat(nums):
    # nums: list [str]
    def reverse(num):
        # num: str
        return "".join(list(num)[::-1])
    # 对每一个字符串取翻转前后的最大值
    for i, num in enumerate(nums):
        if int(num) < int(reverse(num)):
            nums[i] = reverse(num)
    # 自定义排序规则：拼接
    # nums.sort(key=functools.cmp_to_key(compare), reverse=True)
    # 或者是直接本身
    nums.sort(key = compare2, reverse=True)
    return "".join(nums)

if __name__ == "__main__":
    nums = ["22", "23", "11", "444"]
    res = cat(nums)
    print(res)

'''
2. 解题思路：
2.1 先证明 对每个字符串，取 max(num, reverse(num))
对于已经拼接好的结果，以三个字符串为例，nums[0]+nums[1]+nums[2]，与翻转相比 nums[0]+reverse(nums[1])+nums[2]，可以看出如果翻转后数值更大，那么取翻转后的最终解总是优于翻转前的最终解
2.2 证明 排序规则: 对于字符串 x, y ,如果x+y > y+x ，那么 x 更大
第一：对于两个字符串，显然有 如果x+y > y+x，那么 x+y的拼接比 y+x的拼接更优，且是最优的
第二：对于n个字符串，假设已经有拼接好的字符串，以三个字符串为例， 不妨设当前是 nums[0]+nums[1]+nums[2]，对于任意相邻的两个字符串，如果 nums[i]+nums[i+1] < nums[i+1]+nums[i]，显然根据第一步，nums[i+1]更大，需要交换 nums[i]和nums[i+1]的位置，这就是冒泡排序从大到小的规则，对比相邻的字符串，每次将较大的放在左边，较小的放在右边。所以可以自定义排序规则 compare
第三：对于排序规则 compare,可以更简化成compare2.理由如下：对于相邻字符串 x, y, 令 n1=len(x), n2 = len(y),x+y = 10^(n2)*x+y, y+x = 10^(n1) * y+x， 由 (x+y) > (y+x)，可以推导出 x/(10^n1-1)>y/(10^n2-1)，所以也可以根据 num/(10^n-1)进行排序
证毕 

'''