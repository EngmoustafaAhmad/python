
# \b => back space
# \newline => escape the new line + \
# \ => escape the backslash
# \ => escape the single quote 
# \n => new line (line feed character)
# \r => carriage return
# \t => horizontal tab
# \v => vertical tab
# \f => form feed
# \ooo => octal value
# \xhh => hex value
# \uhhhh => unicode character with 16-bit hex value
# \Uhhhhhhhh => unicode character with 32-bit hex value
# \N{name} => unicode character with name
# \a => ASCII bell (BEL)
# \b => ASCII backspace (BS)
# \c => ASCII escape (ESC)
# \e => ASCII escape (ESC)
# \f => ASCII form feed (FF)
# \n => ASCII line feed (LF)
# \r => ASCII carriage return (CR)
# \t => ASCII horizontal tab (TAB)
# \v => ASCII vertical tab (VT)

# ==========================================
# Python Escape Sequences
# ==========================================

# New Line (\n)
print("1. New Line (\\n)")
print("Hello\nPython")

# Horizontal Tab (\t)
print("\n2. Horizontal Tab (\\t)")
print("Name\tAge\tCountry")
print("Ali\t20\tEgypt")

# Backslash (\\)
print("\n3. Backslash (\\\\)")
print("C:\\Users\\Moustafa\\Documents")

# Single Quote (\')
print("\n4. Single Quote (\\')")
print('It\'s a beautiful day.')

# Double Quote (\")
print("\n5. Double Quote (\\\")")
print("He said, \"Hello!\"")

# Carriage Return (\r)
print("\n6. Carriage Return (\\r)")
print("12345\rABC")

# Backspace (\b)
print("\n7. Backspace (\\b)")
print("ABC\bD")

# Form Feed (\f)
print("\n8. Form Feed (\\f)")
print("Hello\fWorld")

# Vertical Tab (\v)
print("\n9. Vertical Tab (\\v)")
print("Hello\vWorld")

# Octal Value (\ooo)
print("\n10. Octal Value (\\101)")
print("\101")  # A

# Hexadecimal Value (\xhh)
print("\n11. Hexadecimal Value (\\x41)")
print("\x41")  # A

# Unicode (16-bit)
print("\n12. Unicode (\\u)")
print("\u03A9")  # Ω

# Unicode (32-bit)
print("\n13. Unicode (\\U)")
print("\U0001F600")  # 😀

# Unicode by Name
print("\n14. Unicode by Name")
print("\N{BLACK HEART SUIT}")

# ASCII Bell
print("\n15. ASCII Bell (\\a)")
print("Bell Sound\a")