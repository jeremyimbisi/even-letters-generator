def solution(S):
    letter_count = {} # initialize empty dictionary 
    
    for letter in S: # loop through every letter in S
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    
    deletions_needed = 0
    
    # to check for count in the inputed word and return the deletions needed to make it even
    
    for count in letter_count.values():
        if count % 2 != 0:  # modulus operator(%) to check if it not even  
            deletions_needed += 1 
    
    return deletions_needed

  
print(solution("aabcb"))
