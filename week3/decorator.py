from hero import *
from abc import ABC, abstractmethod

class AbstractEffect(ABC):
    pass

class AbstractPositive(AbstractEffect):
    pass

class AbstractNegative(AbstractEffect):
    pass

class Berserk(AbstractPositive):
    pass

class Blessing(AbstractPositive):
    pass

class Weakness(AbstractNegative):
    pass

class EvilEye(AbstractNegative):
    pass

class Curse(AbstractNegative):
    pass