# 单例模式：确保一个类只有一个实例，并提供全局访问点。
import time
import threading


# 代码实现
# 单例类装饰器
def SingletonDecorator(cls):
    _instances = {}

    def _singleton(*args, **kwargs):
        if cls not in _instances:
            _instances[cls] = cls(*args, **kwargs)
        return _instances[cls]

    return _singleton


# 单例类装饰器测试
@SingletonDecorator
class SingletonDecoratorTest:
    def __init__(self):
        self._connector_pool = 5  # 初始化5个连接器的连接池

    def get_connector(self):
        if self._connector_pool > 0:
            connector = self._connector_pool
            self._connector_pool -= 1  # 连接池中的连接器-1
            return connector  # 返回连接器
        else:
            return -1


# 单例类 - 懒汉
class SingletonClass1:
    def __init__(self, *args, **kwargs):
        time.sleep(1)  # 没有延迟，执行速度快，出现错误几率很低，但如果__init__中有阻塞就非常明显
        pass

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # 利用反射，查看类有没有_instance属性
        if not hasattr(cls, '_instance'):
            cls._instance = SingletonClass1(*args, **kwargs)

        return cls._instance


# 单例类 - 饿汉
class SingletonClass2:
    def __init__(self, *args, **kwargs):
        time.sleep(1)  # 没有延迟，执行速度快，出现错误几率很低，但如果__init__中有阻塞就非常明显
        pass

    def __new__(cls):
        # 如果类没有实例属性，进行实例化，否则返回实例
        if not hasattr(cls, '_instance'):
            cls._instance = super(SingletonClass2, cls).__new__(cls)
        return cls._instance


# 多线程单例类
class MultiThreadSingletonClass1:
    _instance_lock = threading.Lock()  # 采用加锁，来解决阻塞出现“多实例”的问题

    def __init__(self, *args, **kwargs):
        time.sleep(1)

    @classmethod
    def get_instance(cls, *args, **kwargs):
        # 利用反射，查看类有没有_instance属性
        if not hasattr(cls, '_instance'):  # 第一次查询
            with MultiThreadSingletonClass1._instance_lock:  # 加锁
                if not hasattr(cls, '_instance'):  # 第二次查询
                    MultiThreadSingletonClass1._instance = MultiThreadSingletonClass1(*args, **kwargs)

        return MultiThreadSingletonClass1._instance


# 多线程单例类 - 利用__new__方法实现
class MultiThreadSingletonClass2:
    _instance_lock = threading.Lock()

    def __init__(self, *args, **kwargs):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            with MultiThreadSingletonClass2._instance_lock:
                if not hasattr(cls, '_instance'):
                    MultiThreadSingletonClass2._instance = super().__new__(cls)

        return MultiThreadSingletonClass2._instance


if __name__ == '__main__':
    # 单例类装饰器
    # test = SingletonDecoratorTest()
    # for i in range(5):
    #     print(test.get_connector())

    # 单例类 - 多线程懒汉（不适合多线程）
    # def task(arg):
    #     obj = SingletonClass1.get_instance(arg)
    #     print(obj)
    #
    #
    # for i in range(10):
    #     t = threading.Thread(target=task, args=[i, ])
    #     t.start()

    # 单例类 - 多线程饿汉
    # def task():
    #     obj = SingletonClass2()
    #     print(obj)
    #
    #
    # for i in range(10):
    #     t = threading.Thread(target=task)
    #     t.start()

    # 多线程单例类1
    # def task1(arg):
    #     obj = MultiThreadSingletonClass1.get_instance(arg)
    #     print(obj)
    #
    #
    # for i in range(10):
    #     t = threading.Thread(target=task1, args=[i, ])
    #     t.start()

    # 多线程单例类2 - 存在问题，还未解决
    def task2():
        obj = MultiThreadSingletonClass2()
        print(obj)


    for i in range(10):
        t = threading.Thread(target=task2)
        t.start()
    pass
