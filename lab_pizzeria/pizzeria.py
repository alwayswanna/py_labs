import uuid


class Pizza:

    def __init__(self, name, dough, sauce, filling, price):
        self.name = name
        self.dough = dough
        self.sauce = sauce
        self.filling = filling
        self.price = price

    def __str__(self):
        result = 'Object of class Pizza or ? extends Pizza.class \n'
        result += "id: " + self.id.name + ", ordersList: " + self.dough + '\n'
        result += "id: " + self.id.sauce + ", ordersList: " + self.filling.__str__() + '\n'
        result += "id: " + self.id.price + '\n'
        return result

    def prepare(self):
        srt = ' '
        for value in self.filling:
            srt += value.__str__() + ' '
        print("Prepare pizza: " + self.name)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
        print("Prepare filling: " + srt)
        print("Prepare sauce: " + self.sauce)
        print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")

    def bake(self):
        print("Bake pizza: " + self.name)

    def cut(self):
        print("Cut pizza: " + self.name)

    def wrap(self):
        print("Wrap pizza: " + self.name)


class PeperoniPizza(Pizza):
    def __init__(self):
        super().__init__(
            "Peperoni",
            "Puff pastry",
            "Tomato",
            ["Peperoni", "Cheese", "Tomato", "Pepper"],
            560.0)


class BBQPizza(Pizza):
    def __init__(self):
        super().__init__(
            "BBQPizza",
            "Yeast dough",
            "BBQ",
            ["Peperoni", "Chicken", "Olives", "Cheese", "Tomato"],
            750.0)


class SeaFoodPizza(Pizza):
    def __init__(self):
        super().__init__(
            "SeaFood",
            "Puff pastry",
            "Creamy",
            ["Salmon", "Shrimps", "Cheese", "Olives", "Squid"],
            900.0)


class Order:
    def __init__(self):
        self.id = uuid.uuid1()
        self.ordersList = list()

    def add(self, obj):
        self.ordersList.append(obj)

    def __str__(self):
        result = 'Object of class Order \n'
        order_str_list = ' '
        for value in self.ordersList:
            order_str_list += value.name + ' '
        result += "id: " + self.id.__str__() + ", ordersList: " + order_str_list + '\n'
        return result

    def summary(self):
        total = 0
        for v in self.ordersList:
            total += v.price
        return total

    def execute(self):
        values_order = self.ordersList
        for i in values_order:
            i.prepare()
            i.bake()
            i.cut()
            i.wrap()
        print('Execute order with id: ' + self.id.__str__())


class Terminal:
    _about_code = 0
    _show_menu_code = 5
    _add_pep_code = 1
    _add_bbq_code = 2
    _add_sea_code = 3
    _show_order_code = 4
    _payment_code = 6
    _cancel_order_code = 9

    def __init__(self):
        self.menu = [PeperoniPizza(), BBQPizza(), SeaFoodPizza()]
        self.order = Order()
        self.is_need_to_show = True

    def __str__(self):
        result = 'Object of class Terminal \n'
        result += "menu: " + self.menu.__str__() + '\n'
        result += "id: " + self.order.__str__() + '\n'
        result += "show menu: " + self.is_need_to_show.__str__() + '\n'
        return result

    def show_menu(self):
        self.is_need_to_show = True
        print("Menu: " + '\n')
        pos = 1
        for i in self.menu:
            print(pos.__str__() + " " + i.name)
            pos += 1
        print('[1 - 3] Select pizza, [4] - show current order, [5] - show menu code, [6] - make pay, [9] - cancel '
              'current order, [0] - show info about company')

    def proceed_input(self, input_command):
        try:
            input_value = int(input_command)
            if input_value == Terminal._about_code:
                print("Company Pizza-Delivery-Bro will deliver pizza to your home. \n")
                print('"Pizza-Delivery-Bro", pi_bro_home@example.com, 8-900-000-00-01' + '\n')
            elif input_value == Terminal._show_menu_code:
                self.show_menu
            elif input_value == Terminal._add_pep_code:
                self.order.add(obj=PeperoniPizza())
                print("PeperoniPizza added successfully")
            elif input_value == Terminal._add_bbq_code:
                self.order.add(obj=BBQPizza())
                print("BBQPizza added successfully")
            elif input_value == Terminal._add_sea_code:
                self.order.add(obj=SeaFoodPizza())
                print("SeaFoodPizza added successfully")
            elif input_value == Terminal._show_order_code:
                str_result = 'Your oder is: '
                print(str_result + self.order.__str__())
                print('Total price is: ' + self.order.summary().__str__())
            elif input_value == Terminal._payment_code:
                self.payment()
            elif input_value == Terminal._cancel_order_code:
                self.order.ordersList = list()
                print("Order cancelled")
            else:
                raise ValueError
        except ValueError:
            print("Is incorrect input value")
        except ZeroDivisionError:
            print("Order list is empty, please select product or cancel order")

    def payment(self):
        self.is_need_to_show = False
        if self.order.summary() == 0.0:
            raise ZeroDivisionError
            return
        print('Order start cooking please charge a fee ...' + self.order.summary().__str__())
        sum_order = input()
        if sum_order != self.order.summary().__str__():
            raise ValueError
            return
        self.order.execute()
        self.order.ordersList = list()

# end
# Author: https://github.com/alwayswanna
