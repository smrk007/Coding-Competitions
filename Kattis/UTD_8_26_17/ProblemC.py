output = []

while True:
    try:
        rawLine = input()
        words = rawLine.split(' ')
        mergedWords = "".join(words)

        lineOutput = []
        wordLength = 0
        while True:
            wordLength += 1

            stringList = dict()
            wordsList = []
            for i in range(len(mergedWords) - wordLength + 1):
                string = mergedWords[i:i+wordLength]
                if string not in stringList:
                    stringList[string] = 1
                    wordsList.append(string)
                else:
                    stringList[string] += 1

            max = 1
            for word in wordsList:
                if stringList[word] > max:
                    max = stringList[word]

            if max > 1:
                lineOutput.append(str(max))
            else:
                break
        output.append(lineOutput)

    except EOFError:
        break

for i in range(len(output)):
    output[i] = '\n'.join(output[i])
print('\n\n'.join(output))