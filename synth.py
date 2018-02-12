from faker import Faker
import random
from babel.dates import format_time
from wordstime import wordstime
from tqdm import tqdm, trange
import traceback
from utils import string_to_int
from keras.utils import to_categorical
import numpy as np

fake = Faker()
fake.seed(12345)
random.seed(12345)

FORMATS = [
    "h 'hours', m 'minutes and' s 'seconds' a",
    "h 'hours', m 'minutes and' s 'secs' a",
    "h 'hours', m 'mins and' s 'seconds' a",
    "H 'hours', m 'minutes and' s 'seconds'",
    "H 'hours', m 'mins and' s 'seconds'",
    "H 'hours', m 'minutes and' s 'secs'",
    'medium',
    'long',
    'full'
]
NOISE_BEFORE = [
    "","","","","","",
    "The time is ",
    "It appears to be ",
    "I guess it's ",
    "The time now is ",
    "Father Time says it's ",
]
NOISE_AFTER = [
    "","","","",
    " exactly",
    " on the dot"
]


def load_time():
    """
        Load fake times
        :returns: tuple containing human readable string, machine readable string, and time object
    """
    dt = fake.time_object()

    try:
        if random.randint(0, 1) == 0:
            human_readable = format_time(dt, format=random.choice(FORMATS),  locale='en')
        else:
            human_readable = wordstime(dt)

        #human_readable = random.choice(NOISE_BEFORE) + human_readable + random.choice(NOISE_AFTER)

        machine_readable = dt.isoformat()

    except:
        traceback.print_exc()
        return None, None, None

    return human_readable, machine_readable, dt

def one_hot(ii, oo, Tx, Ty, input_vocab, output_vocab):
    """
    Convert inputs and outputs to one-hot representations.
    """

    icoded = np.array([string_to_int(i, Tx, input_vocab) for i in ii])
    ocoded = np.array([string_to_int(o, Ty, output_vocab) for o in oo])

    ioh = np.array(list(map(lambda x: to_categorical(x, num_classes=len(input_vocab)), icoded)))
    ooh = np.array(list(map(lambda x: to_categorical(x, num_classes=len(output_vocab)), ocoded)))

    return ioh, ooh

def dataset_generator(Tx, Ty, input_vocab, output_vocab, n_s, batch_size=1000):
    while True:
        ii = []
        oo = []
        for i in range(batch_size):
            i, o, _ = load_time()
            if i is not None:
                ii.append(i)
                oo.append(o)

        ioh, ooh = one_hot(ii, oo, Tx, Ty, input_vocab, output_vocab)
        inputs = [ioh, np.zeros((batch_size, n_s)), np.zeros((batch_size, n_s))]

        # Given our get_model(), we need the "outputs" to be a list of 11 elements
        # of shape (number_of_samples, Ty).
        # So that: outputs[i][0], ..., outputs[i][Ty] represent the true
        # labels (characters) corresponding to the i-th training example (X[i]).
        # More generally, outputs[i][j] is the true label of the j-th character
        # in the i-th training example.
        outputs = list(ooh.swapaxes(0,1))
        
        yield (inputs, outputs)

def load_dataset(m):
    """
        Loads a dataset with m examples and vocabularies
        :m: the number of examples to generate
    """

    human_vocab = set()
    machine_vocab = set()
    dataset = []

    for i in trange(m):
        h, m, _ = load_time()
        if h is not None:
            dataset.append((h, m))
            human_vocab.update(tuple(h))
            machine_vocab.update(tuple(m))
    human = dict(zip(sorted(human_vocab) + ['<unk>', '<pad>'], list(range(len(human_vocab) + 2))))
    inv_machine = dict(enumerate(sorted(machine_vocab)))
    machine = {v:k for k,v in inv_machine.items()}

    return dataset, human, machine, inv_machine
