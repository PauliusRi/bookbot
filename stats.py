def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(string):
    count = {}
    for st in string.lower():
        if st in count:
            count[st] += 1
        else:
            count[st] = 1
    return count

def srt_list(letters_dictionary):
    for key, value in sorted(letters_dictionary.items(), key=lambda item: item[0]):
        print(key+":", value)