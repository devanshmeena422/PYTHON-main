def two_sum(nums, target):
    seen = {}
    
    for i in range(len(nums)):
        complement = target - nums[i]
        
        if complement in seen:
            return [seen[complement], i]
        
        seen[nums[i]] = i

    return []

# Input
nums = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target: "))

print("Indices:", two_sum(nums, target))