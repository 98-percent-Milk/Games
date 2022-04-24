import re
from settings import vowels, cons
from random import choice, randint, sample


def main():
    words = load_data('engmix.txt')
    a = solution(words)
    print(a)
    for word in a:
        print(word)


def solution(words: list):
    while True:
        l_sets = generate_sets()
        result, word_list = [], []
        for i in range(3, 17):
            a = generate_pattern(l_sets, i)
            word_list.extend(check_duplicate(a, words[:], l_sets))
        temp = populate_answer(
            [x for sl in l_sets for x in sl], word_list, result)
        if temp == [] and len(result) <= 4:
            return result


def populate_answer(letters: list, words: list, result: list):
    if letters == []:
        return
    a = find_max(words, set(letters))
    [letters.remove(x) for x in a[1]]
    result.append((a[0], letters[:]))
    words.remove(a[0])
    populate_answer_rec(letters, words, a[0], result)
    return letters


def populate_answer_rec(letters: list, words: list, last: str, result: list):
    if letters == []:
        return
    a = find_max(words, set(letters), last[-1])
    if a == ():
        return
    [letters.remove(x) for x in a[1] if x in letters]
    result.append((a[0], letters[:]))
    words.remove(a[0])
    populate_answer_rec(letters, words, a[0], result)


def find_max(words: list, letters: set, s: str = ''):
    if s == '':
        temp_list = [x for x in words]
    else:
        temp_list = [x for x in words if x[0] == s]
    temp_list = [(len(letters.intersection(set(x))), x) for x in temp_list]
    try:
        i = max(temp_list)
    except ValueError:
        return ()
    return i[1], set(i[1])


def test_helper(words: dict, s: str = '') -> tuple:
    if s != '':
        temp = [item for sl in words for item in words[sl] if item[0] == s]
    else:
        temp = [item for sl in words for item in words[sl]]
    i = max([x for x in enumerate([len(set(x)) for x in temp])])
    print(temp[i[0]], i[1])


def split_by_length(words: list) -> dict:
    """Split list of words by length and convert it into dictionary object

    Args:
        words (list): list of words

    Returns:
        dict: key - length of words, values - words
    """
    noc = [len(x) for x in words]
    z = 0
    ii = [noc[z: (z := y)] for y in [noc.index(x) for x in set(noc)]][1:]
    z = -1
    temp = {}
    for sl in ii:
        for item in sl:
            try:
                temp[str(item)].append(words[(z := z + 1)])
            except KeyError:
                temp[str(item)] = [words[(z := z + 1)]]
    return temp


def generate_sets() -> list:
    """Return 12 random characters (at least 3 vowels max 5)

    Returns:
        list: Nested list with 12 characters
    """
    v, c = vowels[:], cons[:]
    i = randint(3, 5)
    t = ''.join([v.pop(v.index(choice(v))) for _ in range(i)])
    t += ''.join([c.pop(c.index(choice(c))) for _ in range(12 - i)])
    t = ''.join(sample(t, len(t)))
    return [t[i:i + 3] for i in range(0, 12, 3)]


def generate_pattern(l_sets: list, i: int) -> str:
    """Generate string pattern which will be used for extracting possible solutions

    Args:
        l_sets (list): list of characters (12 letters)
        i (int): length of the string

    Returns:
        str: [chars] string value for re.findall() function
    """
    temp = '[' + ''.join([''.join(x) for x in l_sets]) + ']'
    return temp * i


def check_duplicate(pattern: str, data: str, l_sets: list) -> list:
    """Check if any adjacent 2 characters in a string are same or not

    Args:
        pattern (str): pattern used to populate the word list
        data (str): list of words in string format
        l_sets (list): letters used in the pattern (12 characters)

    Returns:
        list: list of string values (words generated from 4 sets of 3 letter values)
    """
    words = re.findall(f"\n({pattern})\n", data)
    temp_arr = words[:]
    temp = ''.join([''.join(x) for x in l_sets])
    for word in words:
        if check_duplicate_helper(word, temp):
            temp_arr.remove(word)
    return temp_arr


def check_duplicate_helper(word: str, l_sets: str) -> bool:
    """Check if any adjacent characters in a string if they are same or not

    Args:
        word (str): string value to be checked
        l_sets (str): letter sets (12 characters)

    Returns:
        bool: Return true if any adjacent characters are same else False
    """
    word = [l_sets.index(x) // 3 for x in word]
    temp = [word[x] == word[x + 1] for x in range(len(word) - 1)]
    return True if True in temp else False


def load_data(filename: str = 'english3.txt') -> str:
    """Load text file and return it as string value

    Args:
        filename (str, optional): filename in string. Defaults to 'english3.txt'.

    Returns:
        str: list of words as string value
    """
    with open(filename, 'r', encoding="utf-8", errors="ignore") as f:
        return f.read()


# def generate_sets():
#     c = 0
#     while c < 2:
#         c = 0
#         temp_sets = generate_sets_helper()
#         for temp in temp_sets:
#             if (t := set(vowels).intersection(set(temp))):
#                 c += len(t)
#     return temp_sets


# def generate_sets_helper():
#     t = alpha
#     return [[t.pop(t.index(choice(t))) for _ in range(3)] for _ in range(4)]


# def generate_pattern(l_sets: list, i: int):
# '''
# Generate pattern FROM '0123' TO [1][023][012][123][012][013]
# '''
#     def h(x): return ''.join(s.rsplit(x))
#     a = [''.join(x) for x in l_sets]
#     s = '0123'
#     start = choice(s)
#     word = '[' + a[int(start)] + ']'
#     temp_word = ''
#     for _ in range(i):
#         se = h(start)
#         start = choice(se)
#         [temp_word := temp_word + ''.join(a[int(i)]) for i in se]
#         word += '[' + temp_word + ']'
#         temp_word = ''
#     return word


if __name__ == "__main__":
    main()
