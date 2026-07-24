class Solution:

    def __init__(self):
        self.delimiter = "|"

    def encode(self, strs: List[str]) -> str:
        result = self.delimiter.join(strs)
        return result

    def decode(self, s: str) -> List[str]:
        result = s.split(self.delimiter)
        return result
