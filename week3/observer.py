class ObservableEngine(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subscribers = set()

    def subscribe(self, observer):
        self.subscribers.add(observer)
    
    def unsubscribe(self, observer):
        self.subscribers.remove(observer)
    
    def notify(self, observer, achievement):
        if observer in self.subscribers:
            observer.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPriner(AbstractObserver):
    def __init__(self):
        self.achievements = set()
    
    def update(self, achievement):
        self.achievements.add(achievement)


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        if not achievements in self.achievements:
            self.achievements.append(achievement)