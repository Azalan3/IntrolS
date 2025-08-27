def add_prefix_un(word):
    return 'un' + word

print(add_prefix_un('happy'))
print(add_prefix_un('manageable'))


def make_word_groups(vocab_words):
    prefix = vocab_words[0]
    make_word_prefix = [prefix + word for word in vocab_words[1:]]
    return ' :: '.join([prefix] + make_word_prefix)

print(make_word_groups(['en', 'close', 'joy', 'lighten']))
print(make_word_groups(['pre', 'serve', 'dispose', 'position']))
print(make_word_groups(['auto', 'didactic', 'graph', 'mate']))
print(make_word_groups(['inter', 'twine', 'connected', 'dependent']))


def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith('i'):
        root = root[:-1] + 'y'
    return root

print(remove_suffix_ness('heaviness'))
print(remove_suffix_ness('sadness'))


def adjective_to_verb(sentence, index):
    word = sentence.split()[index]
    if word.endswith('.'):
        word = word[:-1]
    return word + 'en'

print(adjective_to_verb('I need to make that bright.', -1))
print(adjective_to_verb('It got dark as the sun set.', 2))