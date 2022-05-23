import json
import requests
from IPython.display import display
import ipywidgets as widgets
from trading_utils import *
from order_executer import Order_Executor

class Trading_Gui:
    def __init__(self, host, port, name='', password=''):
        self.exec = Order_Executor(host, port, name, password)
        self.url = f"http://{host}:{port}/"

        self.prod = widgets.Text(placeholder='product', description='ID')
        self.side = widgets.Dropdown(options=['BUY', 'SELL'], description='Side',)
        self.type = widgets.Dropdown(options=['Limit', 'Market'], description='Type',)
        self.price = widgets.FloatText(value=0, description='Price')
        self.volume = widgets.FloatText(value=0, description='Volume')

        self.place_order = widgets.Button(description='Place Order', button_style='', tooltip='Click me', icon='')

        def place_order(button):
            if self.prod.value and self.price.value and self.volume.value:
                self.exec.make_order(self.prod.value, self.side.value, self.type.value, self.price.value, self.volume.value)

        self.place_order.on_click(place_order)

        self.active_orders = widgets.Textarea(value='Active Orders', disabled=True, layout={'height': '70%'})
        self.owner_info = widgets.Textarea(value='Positions: 0', disabled=True, layout={'height': '20%'})

        self.ladder = widgets.Textarea(
            value='Asks:\n\nBids:\n\n',
            placeholder='',
            description='Order Book',
            disabled=True,
            layout={'height': '80%'}
        )
        self.delete_all_orders = widgets.Button(description='Delete All Orders', icon='') 
        self.order_id = widgets.Text(value='', placeholder='', description='Delete by Order ID')
        self.delete_order = widgets.Button(description='Delete Order', icon='') 

        self.make_order = widgets.VBox([self.prod, self.side, self.type, self.price, self.volume, self.place_order])
        self.own_orders = widgets.VBox([self.active_orders, self.owner_info])
        self.snapshot = widgets.VBox([self.ladder, self.delete_all_orders, self.order_id, self.delete_order])

        self.gui = widgets.HBox([self.make_order, self.own_orders, self.snapshot])


    def show(self):
        display(self.gui)

        while True:
            ladder = requests.get(self.url + 'ladder').json()
            logs = requests.get(self.url + 'logs').json()
            active_orders = get_active_orders(ladder, self.name)
            active_orders_str = ""
            for order in active_orders:

            self.active_orders.value = active_orders_str
            break
                