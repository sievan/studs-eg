# Translates input to "Rovarspraket".
def translate(input):
    result = ""
    for letter in input:
        if consonant(letter):
            result += letter + "o"
        result += letter
    return result

# Returns true if input letter is a consonant
def consonant(letter):
    consonants = ["b","c","d","f","g","h","j","k","l","m","n","p","q","r","s","t","v","w","x","z"]
    return (letter in consonants)
