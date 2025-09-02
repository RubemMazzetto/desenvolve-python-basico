import emoji

emojis = {
    "❤️": ":red_heart:",
    "👍": ":thumbs_up:",
    "🤔": ":thinking_face:",
    "🥳": ":partying_face:"
}

print("Emojis disponíveis:")
for emoji_char, code in emojis.items():
    print(f"{emoji_char} - {code}")

phrase = input("\nDigite uma frase e ela será emojizada: ")

emojized_phrase = emoji.emojize(phrase, language='alias')

print(f"Frase emojizada:\n{emojized_phrase}")