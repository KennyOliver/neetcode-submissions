class Solution:
    def count_chars(self, to_count: str) -> dict[str, int]:
        char_count = {}

        for char in to_count:
            if char in char_count:
                char_count[char] = char_count[char] + 1
            else:
                char_count[char] = 1
        
        return char_count

    def isAnagram(self, s: str, t: str) -> bool:
        return self.count_chars(s) == self.count_chars(t)
