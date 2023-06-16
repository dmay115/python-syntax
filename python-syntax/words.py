def print_upper_words(array, must_start_with):
    start_list = []
    for letter in must_start_with:
        start_list.append(letter[0].upper())
    for word in array:
        upper_word = (word.upper())
        if upper_word[0] in start_list:
            print(upper_word)

print_upper_words(["eek", "gasp", "yelp", "eurika"], must_start_with=["e", "g"])