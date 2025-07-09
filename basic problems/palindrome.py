def palindrome(string):
        if len(string) <= 1:
            return True
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False
n = input("Enter string: ")
if palindrome(n):
    print("It is a palindrome")
else:
    print("It is not a palindrome")




# class Solution:
#     def palindrome(self, string):
#         if len(string) <= 1:
#             return True
#         if string[0] == string[-1]:
#             return self.palindrome(string[1:-1])
#         else:
#             return False

# # create object
# s = Solution()
# n = input("Enter string: ")
# if s.palindrome(n):
#     print("It is a palindrome")
# else:
#     print("It is not a palindrome")