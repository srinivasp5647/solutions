def anagram(user):
    w = user.split()
    result = {}
    test = []
    for i in range(0, len(w)):
        result[w[i]] = []
        for j in range(0, len(w)):
            is_equal = sorted(w[i]) == sorted(w[j])
            result[w[i]].append(is_equal)
    for value in result.keys():
        print(value)
        a  = []
        for i, b in enumerate(result[value]):
            if (b == True):
                a.append(i+1)
        test.append(a)
    final_result = []
    for value in test:
        if value not in final_result:
            if len(value) > 1:
                final_result.append(value)
    return final_result




user = input("enter a string: ")
result = anagram(user)
print(result)
