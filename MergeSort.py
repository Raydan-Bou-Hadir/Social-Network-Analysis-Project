import Graph
import User

def mergeSorted(users, key=lambda x:x.name):
    if len(users) <= 1:
        return users
    mid = len(users) // 2
    left = mergeSorted(users[:mid], key)
    right = mergeSorted(users[mid:], key)
    return merge(left, right, key)

def merge (left, right, key):
    result = []
    while left and right:
        if key(left[0]) <= key(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left if left else right)
    return result