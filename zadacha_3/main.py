with open("pushkin.txt", "r", encoding="utf-8") as file:
     note1 = file.read().lower()
with open("article.txt", "r", encoding="utf-8") as file:
     note2 = file.read().lower()
all_letters = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
combi = [first + second for first in all_letters for second in all_letters]
count1 = [note1.count(couple) / len(note1) for couple in combi]
count2 = [note2.count(couple) / len(note2) for couple in combi]
count_all = [ abs(count1[num] - count2[num]) for (num,pair)  in enumerate(combi)]
print(max(count_all))
