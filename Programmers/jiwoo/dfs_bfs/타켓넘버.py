def solution(numbers, target):
    root = [0]
    
    for num in numbers:
        subTree = []
        for i in root:
            subTree.append(i+num)
            subTree.append(i-num)
        root = subTree
        
    return root.count(target)