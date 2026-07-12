# ==========================================
# Python String Methods
# ==========================================

# ------------------------------------------
# split()
# ------------------------------------------
print("===== split() =====")

text = "I love Python and Dart"

print(text.split())
print(type(text))

text = "I-love-Python-and-Dart"

print(text.split())
print(text.split("-"))
print(text.split("-", 2))

# ------------------------------------------
# rsplit()
# ------------------------------------------
print("\n===== rsplit() =====")

text = "I-love-Python-and-Dart"

print(text.rsplit("-", 2))

# ------------------------------------------
# center()
# ------------------------------------------
print("\n===== center() =====")

name = "Moustafa"

print(name.center(20))
print(name.center(20, "*"))

# ------------------------------------------
# count()
# ------------------------------------------
print("\n===== count() =====")

sentence = "I love Python and Dart"

print(sentence.count("o"))
print(sentence.count("a", 0, 15))

# ------------------------------------------
# swapcase()
# ------------------------------------------
print("\n===== swapcase() =====")

text1 = "I LOVE PYTHON AND DART"
text2 = "I Love Python and Dart"

print(text1.swapcase())
print(text2.swapcase())

# ------------------------------------------
# startswith()
# ------------------------------------------
print("\n===== startswith() =====")

sentence = "I love Python and Dart"

print(sentence.startswith("I"))
print(sentence.startswith("love", 2, 10))

# ------------------------------------------
# endswith()
# ------------------------------------------
print("\n===== endswith() =====")

print(sentence.endswith("Dart"))
print(sentence.endswith("Python", 2, 15))

# ------------------------------------------
# in Operator
# ------------------------------------------
print("\n===== contains =====")

print("Python" in sentence)
print("Java" in sentence)

# ------------------------------------------
# __contains__()
# ------------------------------------------
print("\n===== __contains__() =====")

print(sentence.__contains__("Python"))

# ------------------------------------------
# index()
# ------------------------------------------
print("\n===== index() =====")

print(sentence.index("P"))
print(sentence.index("P", 5, 15))

# print(sentence.index("P", 0, 5))
# Raises ValueError because "P" is not found.

# ------------------------------------------
# find()
# ------------------------------------------
print("\n===== find() =====")

print(sentence.find("P"))
print(sentence.find("P", 5, 15))
print(sentence.find("P", 0, 5))

# ------------------------------------------
# rjust() and ljust()
# ------------------------------------------
print("\n===== rjust() & ljust() =====")

name = "Moustafa"

print(name.rjust(20))
print(name.rjust(20, "*"))

print(name.ljust(20))
print(name.ljust(20, "*"))

# ------------------------------------------
# splitlines()
# ------------------------------------------
print("\n===== splitlines() =====")

paragraph = """First Line
Second Line
Third Line"""

print(paragraph)
print(paragraph.splitlines())

paragraph = "First Line\nSecond Line\nThird Line"

print(paragraph.splitlines())

# ------------------------------------------
# expandtabs()
# ------------------------------------------
print("\n===== expandtabs() =====")

text = "Name\tAge\tCountry"

print(text.expandtabs(4))

# ------------------------------------------
# istitle()
# ------------------------------------------
print("\n===== istitle() =====")

title = "I Love Python"

print(title.istitle())

# ------------------------------------------
# isspace()
# ------------------------------------------
print("\n===== isspace() =====")

space = " "

print(space.isspace())

# ------------------------------------------
# islower()
# ------------------------------------------
print("\n===== islower() =====")

lower = "python"
mixed = "Python"

print(lower.islower())
print(mixed.islower())

# ------------------------------------------
# isidentifier()
# ------------------------------------------
print("\n===== isidentifier() =====")

print("my_variable".isidentifier())
print("2variable".isidentifier())
print("my variable".isidentifier())

# ------------------------------------------
# isalpha()
# ------------------------------------------
print("\n===== isalpha() =====")

print("Python".isalpha())
print("Python123".isalpha())

# ------------------------------------------
# isalnum()
# ------------------------------------------
print("\n===== isalnum() =====")

print("Python123".isalnum())
print("Python123@".isalnum())

# ------------------------------------------
# replace()
# ------------------------------------------
print("\n===== replace() =====")

text = "one two one three one"

print(text.replace("one", "1", 2))

# ------------------------------------------
# join()
# ------------------------------------------
print("\n===== join() =====")

words = ["Hello", "World", "Python"]

print(" ".join(words))
print("-".join(words))
print(",".join(words))

# ------------------------------------------
# End of Program
# ------------------------------------------
print("\nProgram finished.")