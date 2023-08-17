#!/usr/bin/env python

def word_count(text):
    word_count = {}
    for word in text.split():
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

# Creating a hashmap (dictionary)
phone_book = {
    'Alice': '123-456-7890',
    'Bob': '987-654-3210',
    'Eve': '555-555-5555'
}

# Accessing values using keys
alice_phone = phone_book['Alice']
print(f"Alice's phone number: {alice_phone}")

# Adding a new entry
phone_book['Charlie'] = '111-222-3333'

# Counting occurrences using a hashmap
text = "apple banana apple orange banana apple"
count = word_count(text)
print(count)

# Using a hashmap to eliminate duplicates
numbers = [3, 7, 2, 7, 3, 8, 1, 2]

# converting the array to a set removes duplicates as sets do not allow duplicates
# sets in Python are immutable, unordered hashes
# converting the set back to an array allows us to return the same data type
unique_numbers = list(set(numbers))
print(unique_numbers)
