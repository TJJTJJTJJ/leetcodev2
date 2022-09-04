def print_NxN(n):
    res = [[0 for _ in range(n)] for _ in range(n)]
    # 打印第k圈,k=0...
    total = 1
    for k in range(n//2):
        # 先竖着 k...n-1-k
        for i in range(k, n-k):
            j = k 
            res[i][j] = total
            total+=1
        # 再横着 
        for j in range(k+1, n-k):
            i = n-1-k
            res[i][j] = total
            total+=1
        # 再竖着
        for i in range(n-2-k, k-1, -1):
            j = n-1-k
            res[i][j] = total
            total+=1
        # 再横着
        for j in range(n-2-k, k, -1):
            i = k
            res[i][j] = total
            total+=1
    # 如果n是奇数，需要补充最中间的值
    if n%2==1:
        res[n//2][n//2] = total
    print(res)

if __name__ == "__main__":
    n = 4
    print_NxN(n)
    n = 3
    print_NxN(n)