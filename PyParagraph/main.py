import os
import re

input_path = os.path.join(os.path.join(os.path.dirname(os.path.abspath(__file__))), "..", "Resources", "paragraph_1.txt")

txtFile = open(input_path, 'r')
txt = txtFile.read()

paragraphs = txt.split("\n\n") #paragraphs

for i in range(len(paragraphs)): 
    
    sentences = re.split("(?<=[.!?]) +", paragraphs[i]) #sentences
    sentenceCount = len(sentences)
    wordCount = 0
    letterCount = 0

    for j in range(len(sentences)): #words
        wordSplit = sentences[j].split()
        wordCount += len(wordSplit)
        for k in range(len(wordSplit)): #letters
            letterCount += len(wordSplit[k])

    averageSentenceLength = wordCount / sentenceCount
    averageLetterCount = format(letterCount / wordCount, ".1f")
   
    print("Paragraph analysis")
    print("------------------")
    print("Aproximate word count: ", wordCount)
    print("Aproximate sentence count: ", sentenceCount)
    print("Average letter count: ", averageLetterCount)
    print("Average sentence length: ", averageSentenceLength)