def Small_To_High(arr):
    nl = []
    while arr:
        lowest = min(arr)
        nl.append(lowest)
        arr.remove(lowest)
    return nl

def High_To_Small(arr):
    nl = []
    while arr:
        highest = max(arr)
        nl.append(highest)
        arr.remove(highest)
    return nl