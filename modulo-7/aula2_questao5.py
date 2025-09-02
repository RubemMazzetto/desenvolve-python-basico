import random

def shuffle_inner_letters(phrase):
    """Embaralha as letras internas de cada palavra, mantendo primeiro e último caractere."""
    words = phrase.split()
    return ' '.join(''.join(c[0] + ''.join(random.sample(c[1:-1], len(c[1:-1]))) + c[-1] 
                      if len(c) > 2 else c for c in words))

sentence = "Python é uma linguagem de programação"
result = shuffle_inner_letters(sentence)
print(result)