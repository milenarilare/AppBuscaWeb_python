from kivy import Config
Config.set('graphics', 'multisamples', '0')
import os
os.environ['KIVY_GL_BACKEND'] = 'angle_sdl2'
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.behaviors.button import ButtonBehavior
from kivy.properties import ListProperty
from kivy.uix.label import Label
from kivy.graphics import Color, Ellipse, Rectangle


class FirstLayout(BoxLayout):
  pass

class Menu(Screen):
    pass

class Botao(ButtonBehavior,Label):
    def __init__(self,**kwargs):
        super(Botao,self).__init__(**kwargs)
        self.atualizar()

    def on_pos(self,*args):
        self.atualizar()

    def on_size(self,*args):
        self.atualizar()

    def atualizar(self,*args):
        with self.canvas.before:
            Color(rgba=(0.1,0.5,0.7,1))
            Ellipse(size=(self.height,self.height),
                    pos=self.pos)
            Ellipse(size=(self.height,self.height),
                    pos=(self.x+self.width-self.height,self.y))
            Rectangle(size=(self.width-self.height,self.height),
                      pos=(self.x+self.height/2.0,self.y))

class Botao(ButtonBehavior, Label):
   cor = ListProperty([0.1,0.5,0.7,1])
   cor2 = ListProperty([0.1,0,1,0.1,1])

class Test(App):
    def build(self):
        layout = GridLayout(cols=2, row_force_default=True, row_default_height=40,
                            spacing=10,padding=20)
        value = TextInput(text='')
        self.weight = TextInput(text='')
        submit = Button(text='Buscar', on_press=self.submit)
        layout.add_widget(self.weight)
        layout.add_widget(submit)

        return layout
    def submit(self,obj):
        print("weight: " + self.weight.text)
Test().run()