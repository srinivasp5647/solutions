# This Function returns a number
# Which is nearest to given target
def three_sum(a, target):
    result = []
    for i in range(0, len(a)):                     # Loop will return all added values in a list
        for j in range(1, len(a)):
            for k in range(2, len(a)):
                if (i != j and i != k and j != k):
                    r = a[i] + a[j] + a[k]
                    result.append(r)
    diff = []
    for i in range(0, len(result)):                # Loop will return the nearest value of the target
        if result[i] > target:
            diff.append(result[i] - target)
        else:
            diff.append(target - result[i])
    index = diff.index(min(diff))
    return result[index]

user_input = [-1, 2, 1, -4]
target = 1
result = three_sum(user_input, target)
# Below prints nearest value of the target
print(result)
