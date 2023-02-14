def sort_hyphenated_sequence(sequence):
    # split the input sequence into a list of words
    words = sequence.split("-")
    
    # sort the list of words alphabetically
    words.sort()
    
    # join the sorted list of words into a hyphen-separated sequence
    sorted_sequence = "-".join(words)
    
    # return the sorted sequence
    return sorted_sequence
