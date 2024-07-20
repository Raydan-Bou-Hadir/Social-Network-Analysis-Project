def binarySearch(users, target, key=lambda unknown: unknown.userId):
    low, high = 0, len(users)-1
    while low <= high:
        mid = (low + high)//2
        if key(users[mid]) == target:
            return users[mid]
        elif key(users[mid]) < target:
            low = mid + 1
        else:
            high = mid - 1
    return None