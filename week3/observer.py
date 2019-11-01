class ObservableEngine(Engine):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.subscribers = set()

    def subscribe(self, observer):
        self.subscribers.add(observer)
    
    def unsubscribe(self, observer):
        self.subscribers.remove(observer)
    
    def notify(self, achievement, observer):
        if observer in self.subscribers:
            observer.update(achievement)


class AbstractObserver(ABC):
    @abstractmethod
    def update(self, achievement):
        pass


class ShortNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = set()
    
    def update(self, achievement):
        if 'title' in achievement:
            self.achievements.add(achievement['title'])


class FullNotificationPrinter(AbstractObserver):
    def __init__(self):
        self.achievements = []

    def update(self, achievement):
        if not achievement in self.achievements:
            self.achievements.append(achievement)