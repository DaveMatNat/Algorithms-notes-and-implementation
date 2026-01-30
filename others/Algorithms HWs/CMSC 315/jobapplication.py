def decode(fileToDecode):
    message_words = []
    out = ""

    # Opening the file to the read the encrypted message 
    with open(fileToDecode, "r") as f:
        lines = f.readlines()

    # Storing a null length placeholder in each list element
    for x in range(100):
        message_words.append('')

    # iterating over each line in the file 
    for line in lines:
        # Getting the number on each line
        number = int(line.split()[0])

        # checking if the number above corresponds to the last number in the pyramid
        for x in range(100):
            if number == (int((x * x + x)/2)):
                message_words[x] = line.split()[1]
                break

    # Assembling the final decoded output
    for word in message_words:
        if word != '':
            out = out + word + " "

    return out

print(decode("coding_qual_input.txt"))
