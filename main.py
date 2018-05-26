from kivy.base import runTouchApp
from kivy.uix.listview import ListView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

def run():
    layout = MainLayout()
    runTouchApp(layout.layout)

class MainLayout():

    def addListPressed(self, instance):
        list = MainView()
        self.layout.add_widget(list)

    def __init__(self):
        self.layout = BoxLayout(orientation='vertical')
        button = Button(text='Add List')
        list = MainView()
        button.bind(on_press=self.addListPressed)
        self.layout.add_widget(button)
        self.layout.add_widget(list)



class MainView(ListView):
    def __init__(self, **kwargs):
        super(MainView, self).__init__(
            item_strings=[str(index) for index in range(100)]
        )

if __name__ == '__main__':
    run()
