# write a program to create a dictionary of hindi words and their english meaning and print the dictionary.program should ask user to input hindi word and its english meaning and store it in dictionary and print the dictionary after 5 words have been added

words={
    "namaste":"hello",
    "duniya":"world",
    "mohabbat":"love",
    "khushi":"happiness",
    "dukh":"sadness"
}

word=input("enter a hindi word: ")
print(words.get(word, "Word not found"))