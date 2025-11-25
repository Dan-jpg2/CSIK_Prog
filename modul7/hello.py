s = input('Enter an integer: ')
r = 0
i = 0
while i < len(s):
    r = 10 * r + ord(s[i]) - ord('0')
    i = i + 1
print(f"Converted text input '{s}' to the integer {r}.")
print(f"For comparison, Python's int() function gives {int(s)}.")