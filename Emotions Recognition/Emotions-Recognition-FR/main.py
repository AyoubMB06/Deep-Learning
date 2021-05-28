import string
from collections import Counter

import matplotlib.pyplot as plt

# On fait passer notre fichier txt à la variable text avec l'encodage utf-8:
text = open("read.txt", encoding="utf-8").read()

# On convertit le texte en minuscule car en Python on respecte la casse : text # Text
lower_case = text.lower()

# On supprime la ponctuation pour nettoyer plus le texte:
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

# On fait diviser le texte en mots par la fonction split():
tokenized_words = cleaned_text.split()

# Les mots qu'on va enlever du texte (en anglais):
stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

# On supprimer les stop_words de notre liste de mots (texte):
final_words = []
for word in tokenized_words:
    if word not in stop_words:
        final_words.append(word)

# NLP Emotion Algorithm
# 1) On vérifie si chaque élément de la liste [final_words] appartient à la liste des émotions: 
#  - On ouvre la liste des émotions
#  - On passe par chaque ligne
#  - Si le mot appartient, on l'extrait avec la méthode split()

# 2) Si le mot est présent dans la liste des émotions, on l'ajoute à [emotion_list]
# 3) Après on calcule le nombre de chaque sentiment.

emotion_list = []
with open('emotions.txt', 'r', encoding="utf-8") as file:
    for line in file:
        clear_line = line.replace("\n", '').replace(",", '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

# Présenter les sentiments (émotions dans un graphe):

fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
ax1.set_ylabel('Nombre d\'occurences')
ax1.set_xlabel('Emotions')
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()
