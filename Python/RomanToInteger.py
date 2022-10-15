#https://leetcode.com/problems/roman-to-integer/


from functools import reduce


class Solution:
    def romanToInt(self, s: str) -> int:
        MAPPING = {
            "I" : {
                "value" : 1,
                "magnitude": 1
            },
             "V" : {
                "value" : 5,
                "magnitude": 2
            },
             "X" : {
                "value" : 10,
                "magnitude": 3
            },
             "L" : {
                "value" : 50,
                "magnitude": 4
            },
             "C" : {
                "value" : 100,
                "magnitude": 5
            },
             "D" : {
                "value" : 500,
                "magnitude": 6
            },
             "M" : {
                "value" : 1000,
                "magnitude": 7
            },
        }
        # Case 1: Ordered, no funny business
        #Check if ordered
            # Split the string into list
            # map each element in the list to the magnitude
            # Use sorted which will reutrn a sorted list, compare the two 
            # if equal I can map to value and reduce
        split = [c for c in s]
        mag_mapped = list(map(lambda x: MAPPING[x]["magnitude"], split))
        mag_sorted = sorted(mag_mapped, reverse=True)
        print(f"Checking for equivalency:")
        print(f"{mag_mapped}")
        print(f"{mag_sorted}")
        if mag_sorted == mag_mapped:
            values = list(map(lambda x: MAPPING[x]["value"], split))
            print("in ordered list, no funny business")
            print(f"the items: {values}")
            val = reduce(lambda x,y: x + y, values, 0)
            print(f"reduced: {val}")
            return val

        print(f"List is not in order, magnitudes: {mag_mapped}")
        val_mapped = [MAPPING[ele]["value"] for ele in split]
        print(f"List is not in order, values: {mag_mapped}")
        prev = split[0]
        for i,char in enumerate(split):
            if MAPPING[prev]["magnitude"] < MAPPING[char]["magnitude"]:
                val_mapped[i-1] *= -1
            prev = char

        print(f"Iterated over list, new list: {val_mapped}")

        val = reduce(lambda x,y: x + y, val_mapped, 0)
        print(f"Reduced to {val}")
        return val



    def test_romanToInt(self):
        ret = self.romanToInt("III")
        print(f"{ret} should equal 3")
        ret = self.romanToInt("LVIII")
        print(f"{ret} should equal 58")
        ret = self.romanToInt("MCMXCIV")
        print(f"{ret} should equal 1994")
    # 


sol = Solution()
sol.test_romanToInt()
