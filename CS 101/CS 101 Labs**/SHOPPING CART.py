menu = 'MENU\na - Add item to cart\nr - Remove item from cart\nc - Change item quantity\ni - Output items\' descriptions\no - Output shopping cart\nq - Quit'


class ItemToPurchase: 
    def __init__(self, user_string = 'None', user_float = 0, user_int = 0, user_description = 'none'):
        self.item_name = user_string
        self.item_price = user_float
        self.item_quantity = user_int
        self.item_description = user_description
        
    def print_item_cost(self):
        print('{} {} @ ${} = ${}'.format(self.item_name, int(self.item_quantity), int(self.item_price), int((self.item_price * self.item_quantity))))
    def print_item_description(self):
        print('{}: {}'.format(self.item_name, self.item_description))
    
class ShoppingCart:
    def __init__(self, user_name = 'none', date = 'January 1, 2016'):
        self.customer_name = user_name
        self.current_date = date
        self.cart_items = []
    
    def add_item(self, ItemToPurchase):
        self.cart_items.append(ItemToPurchase)
    def remove_item(self, thing):
        if thing in self.cart_items:
            self.cart_items.remove(thing)
        else:
            print('\nItem not found in cart. Nothing removed.')
    def modify_items(self, ItemToPurchase):
        pass
    def get_num_items_in_cart(self):
        total = 0
        for item in self.cart_items:
            total += item.item_quantity
        return total
    def get_cost_of_cart(self):
        total_cost = 0
        for item in self.cart_items:
            total_cost += item.item_price *item.item_quantity
        return total_cost
    def print_total(self):
        print('{}\'s Shopping Cart - {}'.format(self.customer_name, self.current_date))
        print('Number of Items: {}\n'.format(self.get_num_items_in_cart()))
        total_amount = 0
        for item in self.cart_items:
            item.print_item_cost()
            total_amount += 1
        if total_amount == 0:
            print('SHOPPING CART IS EMPTY\n')
            print('Total: $0')
        else:
            print('\nTotal: ${}'.format(int(self.get_cost_of_cart())))
        
    def print_descriptions(self):
        print('\nItem Descriptions')
        for item in self.cart_items:
            print('{}: {}'.format(item.item_name, item.item_description))
    
def print_menu(ShoppingCart):
    print('\n' + menu)
    user_input = input('\nChoose an option:')
    if user_input not in 'arcioq':
        user_input = input('\nChoose an option:')
        
    while user_input != 'q':
        if user_input == 'o':
            print('\nOUTPUT SHOPPING CART')
            ShoppingCart.print_total()
            print('\n' + menu)
        if user_input == 'i':
            print('\nOUTPUT ITEMS\' DESCRIPTIONS')
            print('{}\'s Shopping Cart - {}'.format(ShoppingCart.customer_name, ShoppingCart.current_date))
            ShoppingCart.print_descriptions()
            print('\n' + menu)
        if user_input == 'a':
            print('\nADD ITEM TO CART')
            item_name = input('Enter the item name:')
            item_description = input('\nEnter the item description:')
            item_price = float(input('\nEnter the item price:'))
            item_quantity = int(input('\nEnter the item quantity:'))
            new_item = ItemToPurchase(item_name, item_price, item_quantity, item_description)
            ShoppingCart.add_item(new_item)
            print('\n\n' + menu)
        if user_input == 'r':
            print('\nREMOVE ITEM FROM CART')
            usr_str = str(input('Enter name of item to remove:'))
            ShoppingCart.remove_item(usr_str)
            print('\n' + menu)
        if user_input == 'c':
            print('c')
            print('\n' + menu)
        user_input = input('\nChoose an option:')
    print()



if __name__ == "__main__":
    user_name = input('Enter customer\'s name:')
    date = input('\nEnter today\'s date:') 
    userCart = ShoppingCart(user_name, date)
    print()
    print('\nCustomer name: {}\nToday\'s date: {}'.format(user_name, date))
    print_menu(userCart)
  
