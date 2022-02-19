from kivy.lang import Builder  # Builder necessário para utilizar o Builder.load_string
from kivy.metrics import dp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu

# Nesse caso, as classes devem estender Screen


class CustomerScreen(Screen):
    def to_worker(self):
        self.manager.current = "worker_screen"


class WorkerScreen(Screen):
    # Chama outra tela que contém o menu e uma imagem do logotipo
    def to_customer(self):
        self.manager.current = "customer_screen"


class MyScreenManager(ScreenManager):
    pass


class App(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.kv = Builder.load_file("ui.kv")
        menu_items = [
            {
                "text": f"Item {i}",
                "viewclass": "OneLineListItem",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            }
            for i in range(5)
        ]
        self.menu = MDDropdownMenu(
            caller=CustomerScreen().ids.drop,
            items=menu_items,
            width_mult=4,
        )

    def menu_callback(self, text_item):
        print(text_item)

    def build(self):
        return self.kv


App().run()
