# 抽象工厂模式：提供一个接口，用于创建相关或依赖对象的家族，而不需要明确指定具体类。


# 代码实现
from abc import ABC, abstractmethod


# 面团（接口类）
class Dough(ABC):
    def __init__(self):
        self.name = ''

    def get(self):
        return self.name


# 厚披萨面团（实现类）
class ThickCrustDough(Dough):
    def __init__(self):
        self.name = 'Thick Crust Dough'


# 薄披萨面团（实现类）
class ThinCrustDough(Dough):
    def __init__(self):
        self.name = 'Thin Crust Dough'


# 酱汁（接口类）
class Sauce(ABC):
    def __init__(self):
        self.name = ''

    def get(self):
        return self.name


# 李子番茄酱（实现类）
class PlumTomatoSauce(Sauce):
    def __init__(self):
        self.name = 'Plum Tomato Sauce'


# 海员式沙司酱（实现类）
class MarinaraSauce(Sauce):
    def __init__(self):
        self.name = 'Marinara Sauce'


# 蛤蜊（接口类）
class Clam(ABC):
    def __init__(self):
        self.name = ''

    def get(self):
        return self.name


# 冰冻蛤蜊（实现类）
class FrozenClam(Clam):
    def __init__(self):
        self.name = 'Frozen Clam'


# 新鲜蛤蜊（实现类）
class FreshClam(Clam):
    def __init__(self):
        self.name = 'Fresh Clam'


# 芝士（接口类）
class Cheese(ABC):
    def __init__(self):
        self.name = ''

    def get(self):
        return self.name


# 马苏里拉芝士（实现类）
class MozzarellaCheese(Cheese):
    def __init__(self):
        self.name = 'Mozzarella Cheese'


# 巴马干酪芝士（实现类）
class ReggianoCheese(Cheese):
    def __init__(self):
        self.name = 'Reggiano Cheese'


# 披萨原料工厂类（接口类）
class PizzaIngredientFactory(ABC):
    @abstractmethod
    def create_dough(self):
        pass

    @abstractmethod
    def create_sauce(self):
        pass

    @abstractmethod
    def create_cheese(self):
        pass

    @abstractmethod
    def create_veggies(self):
        pass

    @abstractmethod
    def create_pepperoni(self):
        pass

    @abstractmethod
    def create_clam(self):
        pass


# 纽约披萨原料工厂类（实现类）
class NewYorkPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThinCrustDough().get()

    def create_sauce(self):
        return MarinaraSauce().get()

    def create_cheese(self):
        return ReggianoCheese().get()

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        return FreshClam().get()


# 芝加哥披萨原料工厂类（实现类）
class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self):
        return ThickCrustDough().get()

    def create_sauce(self):
        return PlumTomatoSauce().get()

    def create_cheese(self):
        return MozzarellaCheese().get()

    def create_veggies(self):
        pass

    def create_pepperoni(self):
        pass

    def create_clam(self):
        return FrozenClam().get()


# 披萨店的产品类（接口类）
class Pizza(ABC):
    def __init__(self):
        self.name = ''
        self.dough = ''  # 面团
        self.sauce = ''  # 酱汁
        self.veggies = []  # 蔬菜
        self.cheese = ''  # 芝士
        self.pepperoni = ''  # 香肠
        self.clam = ''  # 蛤蜊

    # 准备工作（注意：这里变了）
    @abstractmethod
    def prepare(self):
        pass

    # 烘烤
    def bake(self):
        print('Bake for 25 minutes at 350')

    # 切块
    def cut(self):
        print('Cutting the pizza into diagonal slices')

    # 打包
    def box(self):
        print('Place pizza in official PizzaStore box')

    # 设置名称
    def set_name(self, name):
        self.name = name

    # 获取名称
    def get_name(self):
        return self.name


# 芝士披萨（实现类）
class CheesePizza(Pizza):
    def __init__(self, pizza_ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.pizza_ingredient_factory = pizza_ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.pizza_ingredient_factory.create_dough()
        print(f'Tossing {self.dough}')
        self.sauce = self.pizza_ingredient_factory.create_sauce()
        print(f'Adding {self.sauce}')
        self.cheese = self.pizza_ingredient_factory.create_cheese()
        print(f'Adding {self.cheese}')


# 蛤蜊披萨（实现类）
class ClamPizza(Pizza):
    def __init__(self, pizza_ingredient_factory: PizzaIngredientFactory):
        super().__init__()
        self.pizza_ingredient_factory = pizza_ingredient_factory

    def prepare(self):
        print(f'Preparing {self.name}')
        self.dough = self.pizza_ingredient_factory.create_dough()
        print(f'Tossing {self.dough}')
        self.sauce = self.pizza_ingredient_factory.create_sauce()
        print(f'Adding {self.sauce}')
        self.cheese = self.pizza_ingredient_factory.create_cheese()
        print(f'Adding {self.cheese}')
        self.clam = self.pizza_ingredient_factory.create_clam()
        print(f'Adding {self.clam}')


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


# 纽约披萨店（实现类）
class NewYorkPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type) -> Pizza:
        ingredient_factory = NewYorkPizzaIngredientFactory()
        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('New York Style Cheese Pizza')
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('New York Style Clam Pizza')

        return pizza


# 芝加哥披萨店（实现类）
class ChicagoPizzaStore(PizzaStore):
    def _create_pizza(self, pizza_type) -> Pizza:
        ingredient_factory = ChicagoPizzaIngredientFactory()
        if pizza_type == 'cheese':
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name('Chicago Style Cheese Pizza')
        elif pizza_type == 'clam':
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name('Chicago Style Clam Pizza')

        return pizza


if __name__ == '__main__':
    newyork_store = NewYorkPizzaStore()
    newyork_store.order_pizza('cheese')

    chicago_store = ChicagoPizzaStore()
    chicago_store.order_pizza('cheese')
