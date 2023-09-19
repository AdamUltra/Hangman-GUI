from random import *
word_library = ['laptop', 'pig', 'great', 'life', 'sun', 'tower', 'cloak', 'cola', 'oil', 'blood', 'touch', 'grew',
                'cent', 'mix', 'team', 'wire', 'cost', 'lost', 'brown', 'wear', 'garden', 'equal', 'sent', 'choose',
                'fell', 'fit', 'flow', 'fair', 'bank', 'save', 'gentle', 'woman', 'doctor', 'please', 'noon', 'whose',
                'locate', 'ring', 'insect', 'caught', 'period', 'radio', 'spoke', 'atom', 'human', 'effect', 'expect',
                'crop', 'modern', 'hit', 'corner', 'party', 'supply', 'bone', 'rail', 'agree', 'thus', "won't", 'chair',
                'danger', 'fruit', 'rich', 'thick', 'guess', 'sharp', 'wing', 'create', 'wash', 'bat', 'rather', 'crowd',
                'corn', 'poem', 'string', 'bell', 'depend', 'meat', 'rub', 'tube', 'famous', 'dollar', 'stream', 'fear',
                'sight', 'thin', 'planet', 'hurry', 'chief', 'colony', 'clock', 'mine', 'tie', 'enter', 'major', 'fresh',
                'search', 'send', 'yellow', 'gun', 'allow', 'print', 'dead', 'spot', 'desert', 'suit', 'lift', 'rose',
                'block', 'chart', 'hat', 'sell', 'event', 'deal', 'swim', 'term', 'wife', 'shoe', 'spread', 'camp',
                'invent', 'cotton', 'born', 'quart', 'nine', 'truck', 'noise', 'level', 'chance', 'gather', 'shop',
                'throw', 'shine', 'column', 'select', 'wrong', 'gray', 'repeat', 'broad', 'salt', 'nose', 'plural',
                'anger', 'claim', 'oxygen', 'sugar', 'death', 'pretty', 'skill', 'women', 'season', 'magnet', 'silver',
                'thank', 'branch', 'match', 'suffix', 'fig', 'afraid', 'huge', 'sister', 'steel', 'guide', 'score',
                'apple', 'bought', 'led', 'pitch', 'coat', 'mass', 'card', 'band', 'rope', 'slip', 'win', 'dream',
                'feed', 'tool', 'total', 'basic', 'smell', 'valley', 'nor', 'double', 'seat', 'arrive', 'master',
                'track', 'parent', 'shore', 'sheet', 'favor', 'post', 'spend', 'chord', 'fat', 'glad', 'share', 'dad',
                'bread', 'charge', 'proper', 'bar', 'offer', 'slave', 'duck', 'market', 'degree', 'chick', 'dear',
                'enemy', 'reply', 'drink', 'occur', 'speech', 'nature', 'range', 'steam', 'motion', 'path', 'liquid',
                'log', 'meant', 'teeth', 'shell', 'neck']


class Word:
    def __init__(self):
        self.library = word_library
        self.word = ""

    def choose_word(self):
        self.word = choice(self.library)
        return self.word
