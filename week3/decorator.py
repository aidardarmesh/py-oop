from abc import ABC, abstractmethod

class AbstractEffect(ABC, Hero):
    def __init__(self, base):
        self.base = base
    
    @abstractmethod
    def get_stats(self):
        pass
    
    def get_positive_effects(self):
        return self.base.get_positive_effects()
    
    def get_negative_effects(self):
        return self.base.get_negative_effects()

class AbstractPositive(AbstractEffect):
    @abstractmethod
    def get_positive_effects(self):
        pass
y
class AbstractNegative(AbstractEffect):
    @abstractmethod
    def get_negative_effects(self):
        pass

class Berserk(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['HP'] += 50
        stats['Strength'] += 7
        stats['Perception'] -= 3
        stats['Endurance'] += 7
        stats['Charisma'] -= 3
        stats['Intelligence'] -= 3
        stats['Agility'] += 7
        stats['Luck'] += 7
        return stats
    
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Berserk')
        return effects

class Blessing(AbstractPositive):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] += 2
        stats['Perception'] += 2
        stats['Endurance'] += 2
        stats['Charisma'] += 2
        stats['Intelligence'] += 2
        stats['Agility'] += 2
        stats['Luck'] += 2
        return stats
    
    def get_positive_effects(self):
        effects = self.base.get_positive_effects()
        effects.append('Blessing')
        return effects

class Weakness(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 4
        stats['Endurance'] -= 4
        stats['Agility'] -= 4
        return stats

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Weakness')
        return effects

class EvilEye(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Luck'] -= 10
        return stats

    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('EvilEye')
        return effects

class Curse(AbstractNegative):
    def get_stats(self):
        stats = self.base.get_stats()
        stats['Strength'] -= 2
        stats['Perception'] -= 2
        stats['Endurance'] -= 2
        stats['Charisma'] -= 2
        stats['Intelligence'] -= 2
        stats['Agility'] -= 2
        stats['Luck'] -= 2
        return stats
    
    def get_negative_effects(self):
        effects = self.base.get_negative_effects()
        effects.append('Curse')
        return effects