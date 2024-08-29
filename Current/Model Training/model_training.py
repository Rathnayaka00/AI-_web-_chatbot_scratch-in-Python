import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

import random
import pickle
import json

import numpy as numpy
import nltk
from nltk.stem import WordNetLrmmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import SGD

lemmatizer = WordNetLrmmatizer()

intents = json.load(open('intents.json'))

words = []
classes = []
documents = []
ignore_letters = ['?','!','.',',']