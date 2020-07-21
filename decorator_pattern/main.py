# 装饰者模式：动态地将责任附加到对象上。想要扩展功能，装饰者提供有别于继承的另一种选择。
# 设计原则：应该对扩展开放，对修改关闭。（开闭原则）

# 代码实现
from abc import ABC, abstractmethod


# 饮料（抽象类）
class Beverage(ABC):
    def __init__(self):
        self.description = 'Unknown Beverage'

    def get_description(self):
        return self.description

    @abstractmethod
    def cost(self):
        pass


# 具体组件 - HouseBlend
class HouseBlend(Beverage):
    def __init__(self):
        self.description = 'HouseBlend'

    def cost(self):
        return 1.0


# 具体组件 - Espresso
class Espresso(Beverage):
    def __init__(self):
        self.description = 'Espresso'

    def cost(self):
        return 1.5


# 具体组件 - DarkRoast
class DarkRoast(Beverage):
    def __init__(self):
        self.description = 'DarkRoast'

    def cost(self):
        return 1.2


# 调味装饰者（抽象类）
class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass


# 具体调味装饰者 - Milk
class Milk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.description = 'Milk'
        self.beverage = beverage

    def get_description(self):
        return f"{self.beverage.get_description()}, {self.description}"

    def cost(self):
        return self.beverage.cost() + 0.5


# 具体调味装饰者 - Mocha
class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.description = 'Mocha'
        self.beverage = beverage

    def get_description(self):
        return f"{self.beverage.get_description()}, {self.description}"

    def cost(self):
        return self.beverage.cost() + 0.8


# 具体调味装饰者 - Soy
class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self.description = 'Soy'
        self.beverage = beverage

    def get_description(self):
        return f"{self.beverage.get_description()}, {self.description}"

    def cost(self):
        return self.beverage.cost() + 0.3


if __name__ == '__main__':
    beverage = Espresso()
    beverage = Mocha(beverage)
    beverage = Soy(beverage)
    print(f"{beverage.get_description()} ¥{round(beverage.cost(), 2)}")
