# Create new function 'word_count' and assign 'str' parameter
def word_count(str):
  # Accumulator  
  total_words = 0

  # Split each word into a list from their spaces
  new_str = str.split(" ")
    
  # Iterate through elements from new list and counts for every iteration
  for word in new_str:
        total_words += 1
    print(total_words)

# Calls 'word_count' function and takes a sentence to count the words in
word_count("This is a test of my new function.")
