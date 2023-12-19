from morse import morse

# Get text from user to convert
text = input("Enter the text you want to convert: ").upper()
# Empty string for morse code
converted = ""

# Loop through text and convert to morse adding space if not end of text
for i in range(len(text)):
    try:
        if i + 1 != len(text):
            converted += morse[text[i]] + " "
        else:
            converted += morse[text[i]]
    except KeyError:
        pass

print(converted)

