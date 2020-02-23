class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        result = {}
        test = []
        for i in range(0, len(A)):
            result[A[i]] = []
            for j in range(0, len(A)):
                is_equal = sorted(A[i]) == sorted(A[j])
                result[A[i]].append(is_equal)
        for value in result.keys():
            a  = []
            for i, b in enumerate(result[value]):
                if (b == True):
                    a.append(i+1)
            test.append(a)
        final_result = []
        for value in test:
            if value not in final_result:
                final_result.append(value)
        return final_result
