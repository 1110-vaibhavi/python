def binary_search(sorted_list,target):
    low=0
    high=len(sorted_list)
    while low<=high:
        mid=(low+high)//2
        if sorted_list[mid]== target:
            return mid
        elif sorted_list[mid]<target:
            low=mid+1
        else:
            high=mid-1
    return -1
numbers=[10,23,45,68,97,15]
target=97
result=binary_search(numbers,target)
print(f"list: {numbers}")
print(f"Element:{target} found at index:{result}")