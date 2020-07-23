# 工厂方法模式：定义了一个创建对象的接口，但由子类决定要实例化的类是哪一个。工厂方法让类把实例化推迟到子类。
# 设计原则：依赖抽象，不要依赖具体类。


# 代码实现
from abc import ABC, abstractmethod


# 披萨店的产品类（接口类）
class Pizza(ABC):
    def __init__(self):
        self.name = ''
        self.dough = ''
        self.sauce = ''
        self.toppings = []

    # 准备工作
    def prepare(self):
        print(f'Preparing {self.name}')
        print(f'Tossing dough...')
        print(f'Adding sauce...')
        print(f'Adding toppings: ')
        for topping in self.toppings:
            print(f'  {topping}')

    # 烘烤
    def bake(self):
        print('Bake for 25 minutes at 350')

    # 切块
    def cut(self):
        print('Cutting the pizza into diagonal slices')

    # 打包
    def box(self):
        print('Place pizza in official PizzaStore box')

    # 获取名称
    def get_name(self):
        return self.name


# 纽约披萨（产品实现类）
class NewYorkStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'NewYork Style Sauce and Cheese Pizza'
        self.dough = 'Thin Crust Dough'
        self.sauce = 'Marinara Sauce'
        self.toppings.append('Grated Reggiano Cheese')


# 芝加哥披萨（产品实现类）
class ChicagoStyleCheesePizza(Pizza):
    def __init__(self):
        super().__init__()
        self.name = 'Chicago Style Deep Dish Cheese Pizza'
        self.dough = 'Extra Tick Crust Dough'
        self.sauce = 'Plum Tomato Sauce'
        self.toppings.append('Shredded Mozzarella Cheese')

    def cut(self):
        print('Cutting the pizza into square slices')


# 披萨店类（接口类）
class PizzaStore(ABC):
    @abstractmethod
    def _create_pizza(self, pizza_type) -> Pizza:
        pass

    def order_pizza(self, pizza_type):
        pizza = self._create_pizza(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


# 纽约披萨店类（实现类）
class NewYorkPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return NewYorkStyleCheesePizza()


# 纽约披萨店类（实现类）
class ChicagoPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type):
        if pizza_type == 'cheese':
            return ChicagoStyleCheesePizza()


if __name__ == '__main__':
    # 纽约店
    newyork_store = NewYorkPizzaStore()
    newyork_store.order_pizza('cheese')
    # 芝加哥店
    chicago_store = ChicagoPizzaStore()
    chicago_store.order_pizza('cheese')
