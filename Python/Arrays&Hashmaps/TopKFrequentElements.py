class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Hashmap for storing our value counts
        import collections
        count = collections.defaultdict(int)
        # This is our frequency map to take the top k of
        # Index maps to the frequency and value is integer
        freq = [[] for i in range(len(nums) + 1)]

        # iterate over the numbers, increasing the counts
        for n in nums:
            count[n] += 1

        # append at count index the elements
        for n,c in count.items():
            freq[c].append(n)


        res = []
        # iterate backwards over the frequency array
        for i in range(len(freq) -1, 0, -1):
            # for each element with the frequency
            # append and check whether we're at k length
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res