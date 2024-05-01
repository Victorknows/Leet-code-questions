class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string
        str_x = str(x)
        # Check if the string is equal to its reverse
        return str_x == str_x[::-1]

# Create an instance of the Solution class
sol = Solution()

# Test cases
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121)) # Output: False
print(sol.isPalindrome(10))   # Output: False
