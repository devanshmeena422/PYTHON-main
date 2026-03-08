def remove_duplicates(lst):
    seen = []
    
    for num in lst:
        if num not in seen:
            seen.append(num)
            
    return seen

# Example
print(remove_duplicates([1,2,2,3,4,3,5]))