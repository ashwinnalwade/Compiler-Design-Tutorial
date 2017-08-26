# A lexer is a program that performs lexical analysis.
# Lexical analysis is the process of seperating a stream of characters into different words (called tokens).

import sys
import __builtin__

class Token:
    def __init__(self, name, text = None, priority = None):
        
        self.name = name
        self.text = text
        self.priority = priority
