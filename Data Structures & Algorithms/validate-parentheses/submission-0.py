class Solution:
    def isValid(self, s: str) -> bool:
        PARENTHESES: Dict[str, str] = {
            "(": ")",
            ")": "(",
            "{": "}",
            "}": "{",
            "[": "]",
            "]": "[",
        }

        # string_list: List[str] = list(s)
        string: str = s

        median: int = len(string) // 2

        if len(string) % 2 == 0:
            left: str = string[:median]
            right: str = string[median:]
        else:
            left: str = string[:median]
            right: str = string[(median + 1):]
        
        right_mapped: str = right

        for key, val in PARENTHESES.items():
            right_mapped = right_mapped.replace(key, val)
        
        right_mapped_reversed: str = right_mapped[::-1]

        return left == right_mapped_reversed
        