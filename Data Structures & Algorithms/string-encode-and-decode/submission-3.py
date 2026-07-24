class Solution:

    def __init__(self):
        self.delimiter = "|"

    def encode(self, strs: List[str]) -> str:
        result = self.delimiter.join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        result1 = s.split(self.delimiter)
        result2 = [x.trim() for x in result1]
        return result2
