class Solution:
    def appealSum(self, s: str) -> int:
        n = len(s)
        def getLimitCnt(limitCnt):
            dic = dict()
            last_idx = dict()
            left = 0
            cnt = 0
            for right in range(n):
                right_chr = s[right]
                if right_chr in dic:
                    dic[right_chr]+=1
                else:
                    dic[right_chr] = 1
                last_idx[right_chr] = right
                while left<right and len(dic)>limitCnt:
                    left_chr = s[left]
                    dic[left_chr]-=1
                    if dic[left_chr]==0:
                        dic.pop(left_chr)
                        last_idx.pop(left_chr)
                    left+=1
                if len(dic)==limitCnt:
                    min_idx = min(last_idx.values())
                    cnt += (min_idx-left+1)
            return cnt
        res = 0
        maxLimitCnt = len(set(s))
        for limitCnt in range(1, maxLimitCnt+1):
            # print(limitCnt, getLimitCnt(limitCnt))
            res += limitCnt*getLimitCnt(limitCnt)
        return res