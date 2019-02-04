import os
import re

input_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "..", "Resources", "paragraph_1.txt")

txtFile = open(input_path, 'r')
txt = txtFile.read()

paragraphs = txt.split("\n\n")
for i in range(len(paragraphs)):
    
    sentences = re.split("(?<=[.!?]) +", paragraphs[i])
    sentenceCount = len(sentences)
    wordCount = 0
    letterCount = 0
    for i in range(len(sentences)):
        wordSplit = sentences[i].split(" ")
        wordCount += len(wordSplit)
        for j in range(len(wordSplit)):
            letterCount += len(wordSplit[j])
            print(wordSplit[j])

    averageSentenceLength = wordCount / sentenceCount
    averageLetterCount = format(letterCount / wordCount, ".1f")
   
    print("Paragraph analysis")
    print("------------------")
    print("Aproximate word count: ", wordCount)
    print("Aproximate sentence count: ", sentenceCount)
    print("Average letter count: ", averageLetterCount)
    print("Average letter count: ", averageSentenceLength)