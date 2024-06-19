def Small_To_High(list):
    list = list.copy()
    new = []
    while list:
        lowest = min(list)
        new.append(lowest)
        list.remove(lowest)
    return new
  


def High_To_Small(list):
    list = list.copy()
    new = []
    while list:
        highest = max(list)
        new.append(highest)
        list.remove(highest)
    return new

