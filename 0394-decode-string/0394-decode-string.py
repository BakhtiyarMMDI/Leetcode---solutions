class Solution:
    def decodeString(self, s: str) -> str:

        stack = []

        number = 0
        word = ""

        for char in s:

            if char.isdigit():

                number = number * 10 + int(char)

            elif char == "[":

                stack.append((word, number))

                word = ""
                number = 0

            elif char == "]":

                previous_word, repeat = stack.pop()

                word = previous_word + word * repeat

            else:

                word += char

        return word
        