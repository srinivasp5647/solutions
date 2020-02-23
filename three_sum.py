class Solution:
    def threeSumClosest(self, a, target):
        result = []
        for i in range(0, len(a)):
            for j in range(1, len(a)):
                for k in range(2, len(a)):
                    if (i != j and i != k and j != k):
                        r = a[i] + a[j] + a[k]
                        result.append(r)
        diff = []
        for i in range(0, len(result)):
            if result[i] > target:
                diff.append(result[i] - target)
            else:
                diff.append(target - result[i])
        index = diff.index(min(diff))
        return result[index]
