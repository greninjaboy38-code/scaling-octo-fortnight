class StringReverse:
    def __init__(self, text):
        self.text = text

    def reverse_words(self):
        words = self.text.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

text = input("Enter a string: ")
obj = StringReverse(text)

print("Reversed string:", obj.reverse_words())
