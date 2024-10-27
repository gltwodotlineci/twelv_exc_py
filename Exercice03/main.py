words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]
voyels = ['a','e','i','o','u','y']

def count_voyels(word):
    i = 0
    for w in word:
        if w in voyels:
            i += 1
    return i

tuple_words = [(w,count_voyels(w)) for w in words]
print(tuple_words)
