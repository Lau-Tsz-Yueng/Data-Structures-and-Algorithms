#我是这样想的 在每一个上一次循环中添加括号
#比如 n = 2时 使用n=1的括号 -- '()'， 在n=1的括号间隙加括号
#for循环第一次时 ()() 第二次是 (()) 第三次是 ()() 所以排除第三个重复 所以
#加入数组。

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = ["()"]
        if n == 1:
            return ans
        new= []
        for k in range(n):
            for i in range(len(ans)):
                for j in range(len(ans[i])+1):
                    tmp = ans[i][:j] + '()' + ans[i][j:]
                    if tmp not in new:
                        new.append(tmp)
            if k == n-2:
                return new
            else:
                ans = new
                new = []
        return new
