class Solution:
    def maximumWidth(self, planks: list[int]) -> int:
        dictionary = dict()
        for i in planks:
            dictionary[i] = dictionary.get(i,0)+1

        freq = dict(dictionary)
        uni = list(dictionary.keys())
        n = len(uni)
        for i in range(n):
            for j in range(i,n):
                if i == j:
                    curr_h = dictionary[uni[i]] //2
                    if curr_h >0:
                        h = uni[i] * 2
                        freq[h] = freq.get(h,0) + curr_h
                else:
                    curr_h = min(dictionary[uni[i]],dictionary[uni[j]])
                    if curr_h > 0:
                        h = uni[i] + uni[j]
                        freq[h] = freq.get(h,0) + curr_h
        ans = max(freq.values()) if freq else 0
        return ans