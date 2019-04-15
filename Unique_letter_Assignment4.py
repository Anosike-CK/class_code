# Write a program to reverse a users text
# The program should count how many vowels and consonants
#The program should identify unique vowels and consonants and how many times,
#they occur in a text

User_text = input("Enter a word of your choice : ").lower()     # prompt for user text and split into a list format
reverse_text = User_text[::-1]                                   # Reverses the user input
User_text_join = ''.join(reverse_text.split())                  # join reverse user text to eliminate spaces
vowel_list = ['a','e','i','o','u']                              # Vowel list to identify vowels

consonant_list = ['b','c','d','f','g','h','j','k','l','m',
                   'n','p','q','r','s','t','v','w','x','y',
                   'z']                                         # Consonant list to identify vowels

emptylist_vowels = []                                           # Stores vowels from the user input
emptylist_consonants = []                                       # Stores consonants from the user input
emptylist_consonants = []                                       # Stores other characters from the user input
Other_char = []                                                     
count_vowels = 0                                                # Stores the number of vowels in the text
count_consonant = 0                                             # Stores the number of consonants in user text
count_other_char = 0                                            # Stores the number of non vowels and consonants in user text



for letters in User_text_join:                                  #Iterates over the letters in the joined user input

    if letters in vowel_list:                                   # Checks if the letters are vowels

        emptylist_vowels.append(letters)                        # Stores the vowels in an empty string
        count_vowels += 1                                       # Stores the count for each vowel iterated

    elif letters in consonant_list:                             # Checks if the letters are consonants

        emptylist_consonants.append(letters)                    # Stores consonants in an empty list
        count_consonant += 1

    else:                                                       # Do other character checks

        Other_char.append(letters)                              # Store the characters 
        count_other_char += 1                                   # Count the characters

    
print(f" \nYour text is : \n {User_text}\n")                                                                    # Print the user text
print(f" Your reversed joined text is : \n {reverse_text}\n")                                                   # Print the user text in reverse
print(f" Your reversed joined text is : \n {User_text_join}\n")                                                 # Print the joined reversed text
print(f"The total number of vowels in the text(s) is : {count_vowels}\n")                                       # Print the number of vowels
print(f"The total number of consonant in the text(s) is : {count_consonant}\n")                                 # Print the number of consonants
print(f"The total number of other characters in the text(s) is : {count_other_char}\n")                         # Print the number of other characters
print(f"The total number of your text is :  {len(User_text_join)}\n")                                           # Print the length of user text
print(f" The list of vowels in your text : {emptylist_vowels}\n")                                               # Print the vowels in the user text
print(f" The list of consonants in your text : {emptylist_consonants}\n")                                       # Print the consonants in the user text
print(f" The list of other characters in your text : {Other_char}\n")                                           # Print the other characters in user text if any

unique_vowel_count = {letters:emptylist_vowels.count(letters) for letters in emptylist_vowels}                  # Create a dictionary that stores the unique vowel repetitions
print(unique_vowel_count)

unique_consonant_count = {letters:emptylist_consonants.count(letters) for letters in emptylist_consonants}      # Create a dictonary that stores the unique consonant repetiions
print(unique_consonant_count)

# print(f"a has {emptylist.count('a')}")
# print(f"e has {emptylist.count('e')}")
# print(f"i has {emptylist.count('i')}")
# print(f"o has {emptylist.count('o')}")
# print(f"u has {emptylist.count('u')}")