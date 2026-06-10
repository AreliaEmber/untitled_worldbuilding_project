import random

onset = ["t", "d", "k", "g", "f", "v", "s", "z", "h", "w", "r"]
monophthong = ["a", "e", "i", "o"]
diphthong = ["ao", "ae", "ai", "oi", "ei", "a", "e", "i", "o"] # diphthong here describes all vowels *including* diphthongs, so monophthongs are here as well
coda = ["t", "d", "k", "g", "m", "n", "ng", "f", "v", "s", "z",]
glottal_stop = ["'", "t", "d", "k", "g", "f", "v", "s", "z", "h", "w", "r"] # basically just the onset with the glottal stop as well

## syntax settings

max_length = 3 # max number of syllables
syllable_chance = 0.5 # the chance that each further syllable should be included in the word after the first
number_of_words = 10 # how many words do we generate at once
initial_syllable_structures = [
    [onset, monophthong, coda], 
    [monophthong, coda], 
    [onset, monophthong], 
    [monophthong], 
    [onset, diphthong], 
    [onset, diphthong, coda], 
    [diphthong, coda], 
    [diphthong], 
    ]
syllable_structures_after_no_coda = [
    [onset, monophthong, coda], 
    [onset, monophthong], 
    [onset, diphthong], 
    [onset, diphthong, coda], 
    [glottal_stop, monophthong, coda], 
    [glottal_stop, monophthong], 
    [glottal_stop, diphthong], 
    [glottal_stop, diphthong, coda], 
    ]
syllable_structures_after_coda = [
    [onset, monophthong, coda], 
    [onset, monophthong], 
    [onset, diphthong], 
    [onset, diphthong, coda], 
    ]

all_words = []

for x in range(number_of_words):
    previous_structure = []
    new_word = ""  
    for i in range(max_length):
        if i != 0 and random.random() > syllable_chance:
            continue

        new_syllable = ""
        structure = []

        if i == 0:
            structure = random.choice(initial_syllable_structures)
        elif previous_structure[-1] == coda:
            structure = random.choice(syllable_structures_after_coda)
        else:
            structure = random.choice(syllable_structures_after_no_coda)
        
        for item in structure:
            new_syllable += random.choice(item)
        previous_structure = structure
        new_word += new_syllable

    print(new_word)
    all_words.append(new_word)