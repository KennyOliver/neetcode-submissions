class Solution:

    def __init__(self):
        self.delimiter = "|"

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        return self.delimiter.join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        return s.split(self.delimiter)
