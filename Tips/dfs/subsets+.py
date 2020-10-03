nums = list(map(int, input().split()))

def subsets(nums):
    result = []

    def dfs(idx, path):
        # 매번 결과 추가
        result.append(path)
        
        for i in range(idx, len(nums)):
            dfs(i+1, path+[nums[i]])
    
    dfs(0, [])
    return result

print(subsets(nums))