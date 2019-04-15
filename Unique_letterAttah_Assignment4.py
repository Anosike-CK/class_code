user_text = input("Please enter text to work on : ")

#reverse using slicing
reversed_user_text = user_text[::1]
print(reversed_user_text)

vowels = ""
consonants = ""

vowel_count = 0
consonant_count = 0

vowels_in_english = "aeiou"

for letter in reversed_user_text:

    if letter in vowels_in_english:

        vowel_count += 1
        if letter not in vowels:

            vowels += letter

    elif letter not in vowels_in_english and letter.isalpha():

        consonant_count += 1
        if letter not in consonants:

            consonants += letter


print(f"Vowels = {vowel_count}, consonants = {consonant_count}, \n O-chars = {len(user_text) - vowel_count - consonant_count} \n  Total = {len(user_text)} \n \n unique consonant = {consonants} \n unique vowels = {vowels}")