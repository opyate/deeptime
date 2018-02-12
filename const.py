# Constants and other hyperparameters.

# We cap the input at (or pad it to) 128 characters
Tx = 128
# a time 'hh:mm:ss' is 8 characters
Ty = 8

n_a = 64
n_s = 128

import string

def get_input_vocab():
    """
    Simply generate a complete input vocabulary from everything we know
    the input can contain
    """
    vocab = set()
    vocab.update(list(string.ascii_letters))
    vocab.update(list(string.digits))
    vocab.update(list(string.punctuation))
    vocab.update(list(string.whitespace))
    vocab.update(['<unk>', '<pad>'])
    return dict(zip(sorted(vocab), list(range(len(vocab)))))

def get_output_vocab():
    """
    Simply generate a complete output vocabulary from everything we know
    the prediction can contain
    """
    vocab = set(list(string.digits) + [':'])

    inv = dict(enumerate(sorted(vocab)))
    output = {v:k for k,v in inv.items()}
    return output, inv

input_vocab = get_input_vocab()
output_vocab, output_vocab_inv = get_output_vocab()
