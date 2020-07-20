# 观察者模式：在对象之间定义一对多的依赖，这样一来，当一个对象改变状态，依赖它的对象都会受到通知，并自动更新。
# Poll模型实现
# 设计原则：为了交互对象之间的松耦合设计而努力。

# 代码实现
from abc import ABC, abstractmethod


# 主题（接口类）
# Poll模型
class ISubject(ABC):
    @abstractmethod
    def register(self, observer):
        pass

    @abstractmethod
    def remove(self, observer):
        pass

    # Poll模型中，只通知观察者有新信息，并不发送信息
    @abstractmethod
    def notify(self):
        pass

    # Poll模型中，由观察者主动向主题获取新信息
    @abstractmethod
    def get_message(self):
        pass


# 观察者（接口类）
class IObserver(ABC):

    def __init__(self, subject):
        self.subject = subject
        self.subject.register(self)

    @abstractmethod
    def display(self):
        pass

    @abstractmethod
    def update(self):
        pass


# 主题 - 天气气象站（实现类）
class WeatherData(ISubject):
    def __init__(self):
        self.observers = []
        self.message = ''

    def register(self, observer: IObserver):
        self.observers.append(observer)

    def remove(self, observer: IObserver):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update()

    def update_message(self, message):
        self.message = message

    def get_message(self):
        return self.message


# 观察者 - 当前观测值（实现类）
class CurrentConditionsDisplay(IObserver):
    def display(self):
        print('显示当前观测值')

    def update(self):
        # 这里简化了对接收信息的处理
        print(f"CurrentConditionsDisplay: {self.subject.get_message()}")


# 观察者 - 最小、平均、最大观测值（实现类）
class StatisticsDisplay(IObserver):
    def display(self):
        print('显示最小、平均、最大观测值')

    def update(self):
        # 这里简化了对接收信息的处理
        print(f"StatisticsDisplay: {self.subject.get_message()}")


if __name__ == '__main__':
    wd = WeatherData()
    cur = CurrentConditionsDisplay(wd)
    sta = StatisticsDisplay(wd)

    wd.update_message('今天天气晴')
    wd.notify()
