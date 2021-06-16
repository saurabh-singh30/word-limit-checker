your_file = open(input("enter full path of your text file:"), "rt")
s = your_file.read()
words = s.split()
print('Number of words in your file are:', len(words))
