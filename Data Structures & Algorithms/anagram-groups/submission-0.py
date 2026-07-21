class Solution:
    def makeFreqArr(self, toAnalyze: str) -> List[int]:
        freqArr = [0] * 26
        for char in toAnalyze:
            freqArr[ord(char) - ord("a")] += 1
        return tuple(freqArr)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for x in strs:
            key = self.makeFreqArr(x)
            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(x)
        
        return list(my_dict.values())
        
        