from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.carousel import Carousel
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivymd.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.button import MDFlatButton
from stem import Stem
from diagnose import Diagnose
from vascular import Vascular
from blackcanker import BlackCanker
from leaf import Leaf
from fruit import Fruit
from login import Login
from start import Start
from signup import SignUp
from home import Home
from vascularleaf import VascularLeaf
from blackpod import BlackPod



from kivy.core.window import Window
Window.size = (350,600)

class MyApp(MDApp):
    def build(self):
        sm = ScreenManager(transition=FadeTransition())
        sm.add_widget(Start(name="start_screen"))
        sm.add_widget(Login(name="login_screen"))
        sm.add_widget(SignUp(name="signup_screen"))
        sm.add_widget(Home(name="home_screen"))
        sm.add_widget(Diagnose(name="diagnose_screen"))
        sm.add_widget(Stem(name="stem_screen"))
        sm.add_widget(Vascular(name="vascular_screen"))
        sm.add_widget(BlackCanker(name="blackcanker_screen"))
        sm.add_widget(Leaf(name="leaf_screen"))
        sm.add_widget(VascularLeaf(name="vascularleaf_screen"))
        sm.add_widget(Fruit(name="fruit_screen"))
        sm.add_widget(BlackPod(name="blackpod_screen"))
        

        return sm

if __name__ == "__main__":
    LabelBase.register(name="Poppins",fn_regular="Raleway-Black.ttf")
    LabelBase.register(name="BPoppins",fn_regular="Raleway-Bold.ttf")
    MyApp().run()

















