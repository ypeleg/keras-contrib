from __future__ import absolute_import

from . import backend as K
from keras.utils.generic_utils import get_from_module

from keras.objectives import *


def get(identifier):
    return get_from_module(identifier, globals(), 'objective')
