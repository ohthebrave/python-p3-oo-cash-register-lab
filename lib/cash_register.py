#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity = 1):
        self.items.append({'title': title, 'price': price, 'quantity': quantity})
        self.total += price * quantity

    def apply_discount(self):
        if self.total != 0:
          self.total -= self.total * self.discount / 100 
          print(f"After the discount, the total comes to ${self.total:.0f}.")
        else:
            print("There is no discount to apply.")

    def items_list_without_multiples(self):
        titles = set(item['title'] for item in self.items)
        return list(titles)
            
          
        

cash_register = CashRegister(discount=20)
cash_register.add_item("eggs", 10.0, 8)
cash_register.add_item("tomato", 5.0, 2)
cash_register.apply_discount()
print(cash_register.items_list_without_multiples())

# print(cash_register.total)


