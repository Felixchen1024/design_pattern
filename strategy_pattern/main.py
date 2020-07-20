# 策略模式：定义算法族，分别封装起来，让它们之间可以互相替换，此模式让算法的编号独立于使用算法的客户。
# 面向对象（OO）基础：抽象、封装、多态、继承
# 设计原则：封装变化。
# 设计原则：多用组合，少用继承。
# 设计原则：针对接口编程，而不是针对实现编程。

# 代码实现
from abc import ABC, abstractmethod


# 飞行行为（接口类）
class IFlyBehavior(ABC):
    @abstractmethod
    def fly(self):
        pass


# 飞行行为 - 有翅膀飞行（实现类）
class FlyWithWings(IFlyBehavior):
    def fly(self):
        print('用翅膀飞')


# 飞行行为 - 不会飞（实现类）
class FlyNoWay(IFlyBehavior):
    def fly(self):
        print('不会飞')


# 叫的行为（接口类）
class IQuackBehavior(ABC):
    @abstractmethod
    def quack(self):
        pass


# 叫的行为 - 呱呱叫（实现类）
class Quack(IQuackBehavior):
    def quack(self):
        print('呱呱叫')


# 叫的行为 - 吱吱叫（实现类）
class Squeak(IQuackBehavior):
    def quack(self):
        print('吱吱叫')


# 鸭子类
class Duck:
    def __init__(self):
        self.display_name = '鸭子'
        self.fly_behavior = IFlyBehavior()
        self.quack_behavior = IQuackBehavior()

    def display(self):
        print(self.display_name)

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


# 野鸭
class MallardDuck(Duck):
    def __init__(self):
        self.display_name = '野鸭'
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()


if __name__ == '__main__':
    md = MallardDuck()
    md.display()
    md.perform_fly()
    md.perform_quack()
