with open("pushkin.txt", "r", encoding="utf-8") as file:
    note = file.read().lower()
all_letters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
key = "мороз"
size = len(all_letters)
ideal_equal = 1 / size
letters = "".join([let for let in note if let in all_letters])
key_text = "".join([key[i % len(key)] for i in range(len(letters))])
shifr = "".join([
        chr(ord("а") + ((ord(letters[i]) - ord("а")) + (ord(key_text[i]) - ord("а"))) % size)
        for i in range(len(letters))
])
count = [shifr.count(l) / len(shifr) for l in all_letters]
maxi = max(count)
mini = min(count)
max_otlich = abs(maxi - ideal_equal)
mini_otlich = abs(mini - ideal_equal)
print(max_otlich, mini_otlich)

