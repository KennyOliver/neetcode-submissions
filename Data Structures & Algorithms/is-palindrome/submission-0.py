class Solution:
    def isPalindrome(self, s: str) -> bool:
        edited_string: str = s.lower()
        chars: str = ""

        for char in edited_string:
            if char.isalnum():
                chars += char
        
        median = len(chars) // 2

        left_half: str = ""
        right_half: str = ""

        if len(chars) % 2 == 0:
            left_half = chars[:median]
            right_half = chars[median:]
        else:
            left_half = chars[:median]
            right_half = chars[(median + 1):]
        
        # print("Left:", left_half)
        # print("Right:", right_half)
        
        return left_half == right_half[::-1]
