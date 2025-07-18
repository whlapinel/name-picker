class MenuItem:
    def __init__(self, num: int, callback, text: str):
        self.num = num
        self.callback = callback
        self.text = text

class Menu:
    def __init__(self, items: list[MenuItem]):
        self.items = items

    def display(self):
        for item in self.items:
            print(item.num, item.text)

    def get_choice(self)->MenuItem:
        found = False
        chosen: MenuItem = None
        while not found:
            choice = int(input("Enter choice: "))
            for item in self.items:
                if choice == item.num:
                    return item
            print("Invalid choice.")                    

    def execute_choice(self, item: MenuItem):
        item.callback()  

def print_hello():
    print('hello')

def load_menu()->Menu:

    return Menu(
        [
            MenuItem(1, print_hello, "Say Hello"),
         ]
    )


def main():
    menu = load_menu()
    while True:
        menu.display()
        choice = menu.get_choice()
        menu.execute_choice(choice)

if __name__ == "__main__":
    main()
