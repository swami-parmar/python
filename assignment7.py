
# Task 1: Count Characters

text = input("Enter a string: ")

char_count = {}

for char in text:
    char_count[char] = char_count.get(char, 0) + 1

print("Task 1: Character Frequency")
print(char_count)


# Task 2: Count Words in a Food Delivery App Review

review = """
I love Zomato because Zomato delivers food quickly.
The food is tasty and the delivery service is good.
I use Zomato to order my favorite food.
"""

word_count = {}

for word in review.lower().split():
    word = word.strip(".,!?;:'\"()")
    if word:
        word_count[word] = word_count.get(word, 0) + 1

print("\nTask 2: Word Frequency")
print(word_count)


# Task 3: Word Frequency Using a Function

def word_freq_dict(text):
    word_count = {}

    for word in text.lower().split():
        word = word.strip(".,!?;:'\"()")
        if word:
            word_count[word] = word_count.get(word, 0) + 1

    return word_count


text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"

print("\nTask 3: Word Frequency Dictionary")
print(word_freq_dict(text))


# Task 4: Word Frequency Without Stopwords

stopwords = ["the", "and", "in", "of", "a", "to", "is"]

review = """
The food is tasty and the delivery is fast.
I use Zomato to order food in the evening.
The service of Zomato is good.
"""

word_count = {}

for word in review.lower().split():
    word = word.strip(".,!?;:'\"()")

    if word and word not in stopwords:
        word_count[word] = word_count.get(word, 0) + 1

print("\nTask 4: Word Frequency Without Stopwords")
print(word_count)


# Task 5: Character Count Using a Function and Sorting

def char_count_dict(text):
    char_count = {}

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1

    return char_count


text = input("\nEnter text for Task 5: ")

sorted_char_count = dict(sorted(char_count_dict(text).items()))

print("Task 5: Sorted Character Frequency")
print(sorted_char_count)
