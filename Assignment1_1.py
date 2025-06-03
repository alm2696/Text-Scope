def contents(infile):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    
    vowel_count = 0
    consonant_count = 0
    whitespace_count = 0
    
    for line in infile:
        for char in line:
            if char in vowels:
                vowel_count += 1
            elif char in consonants:
                consonant_count += 1
            elif char in [' ', '\t', '\n']:
                whitespace_count += 1
    
    return vowel_count, consonant_count, whitespace_count

def compare_files(infile1, infile2):
    file1 = set(infile1.read().split())
    file2 = set(infile2.read().split())

    common_words = list(file1.intersection(file2))
    unique_file1 = list(file1.difference(file2))
    unique_file2 = list(file2.difference(file1))

    return common_words, unique_file1, unique_file2

infile = open(r'C:\Users\angel\Documents\input.txt', 'r')
vowels, consonants, whitespaces = contents(infile)
infile.close()
print(f'Count of vowels: {vowels}')
print(f'Count of consonants: {consonants}')
print(f'Count of whitespaces: {whitespaces}')

infile1 = open(r'C:\Users\angel\Documents\PESTLE.txt', 'r')
infile2 = open(r'C:\Users\angel\Documents\Accessory Avenue.txt', 'r')
common, unique1, unique2 = compare_files(infile1, infile2)
infile1.close()
infile2.close()
print("\nWords present in both files:")
print(common)
print("\nWords present in first file but not in second:")
print(unique1)
print("\nWords present in second file but not in first:")
print(unique2)