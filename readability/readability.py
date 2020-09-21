from cs50 import get_string

text = get_string("Text: ")
arr_text = text.split(" ")

#counting variables
words = len(arr_text)
sentences = 0
letters = 0 

for w in arr_text:
    for l in w:
        if (l.isalpha()):
            letters += 1
        elif(l is '?' or l is '.' or l is '!'):
            sentences += 1
        
avg_letters = letters * 100 / words;
avg_sentences =  sentences * 100 / words;

index = round(0.0588 * avg_letters - 0.296 * avg_sentences - 15.8)

if (index < 1):
    print("Before Grade 1")
elif (index >= 16):
    print("Grade 16+")
else:
    print("Grade",index)
    
  

