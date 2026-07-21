class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits_as_string: str = ""

        for digit in digits:
            digits_as_string += str(digit)
        
        as_num: int = int(digits_as_string)

        incremented: int = as_num + 1

        incremented_as_string: str = str(incremented)

        result: List[int] = []

        for num in incremented_as_string:
            result.append(int(num))
        
        return result