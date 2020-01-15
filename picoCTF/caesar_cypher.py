string = "ynkooejcpdanqxeykjrubvtagp"
rotate = 1

while 1:
    newString = ""
    for char in string:
        newString += chr((ord(char) + rotate) % 26 + ord('a'))
    print(newString)
    raw_input("Press Enter")
    rotate += 1
