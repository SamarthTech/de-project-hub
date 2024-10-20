emoji_dict = {
    "happy": "😊",
    "sad": "😢",
    "love": "❤️",
    "food": "🍔",
    "dog": "🐶",
    "cat": "🐱",
    "sun": "☀️",
    "moon": "🌙",
    "party": "🎉",
    "car": "🚗"
}
def emoji_translator(sentence):
    words = sentence.split() 
    translated_sentence = []
    
    for word in words:
        translated_sentence.append(emoji_dict.get(word, word))
    
    return " ".join(translated_sentence)

user_input = input("Enter a sentence to translate into emojis: ")

translated = emoji_translator(user_input)
print(f"Translated sentence: {translated}")
