sentence = "I love you"
reverse_sentence=''
for char in sentence:
    print("char:", char)
    print("reverse_before:", reverse_sentence)
    reverse_sentence = char + reverse_sentence
    print("reverse_after:", reverse_sentence)
print(reverse_sentence)
