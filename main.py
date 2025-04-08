def min_jumps(arr):
    n = len(arr)
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    
    maxReach = arr[0]
    steps = arr[0]
    jumps = 1
    
    for i in range(1, n):
        if i == n - 1:
            return jumps
        
        maxReach = max(maxReach, i + arr[i])
        steps -= 1
        
        if steps == 0:
            jumps += 1
            if i >= maxReach:
                return -1
            steps = maxReach - i
    
    return -1
print(min_jumps([2, 3, 1, 1, 4]))  
print(min_jumps([1, 1, 1, 1]))    
print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9])) 
print(min_jumps([0]))                
print(min_jumps([0, 1, 2])) 
