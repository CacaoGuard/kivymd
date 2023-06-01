from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder
from kivymd.app import MDApp

import firebase_auth

import firebase_admin 
from firebase_admin import credentials
from firebase_admin import firestore
from firebase_admin import authentication
from google.cloud import firestore

cred=credentials.Certificate('../gpt_venv/assets/gpt-venv-cacao-559d6ada3d0b.json')
firebase_admin.initialize_app(cred)
db=firestore.client()




KV='''

<Signup>:
    canvas:
        Color:
            rgba: 0.941, 0.886, 0.835, 1                  #F0E2D5
        Rectangle:
            pos: self.pos
            size: self.size
    ScrollView:
        MDGridLayout:
            cols: 1
            adaptive_height: True
            # padding: dp(16)
            spacing: dp(25)
            padding: [30, 0, 30, 50]
            MDLabel:
                text: '   '
                font_size: 5
                adaptive_height: True
            MDLabel:
                text: 'CREATE AN ACCOUNT'
                font_name: "Raleway-Black.ttf"
                halign: 'center'
                theme_text_color: "Custom"
                text_color: "#A08264"
                font_size: 32
                adaptive_height: True
            MDTextField:
                id: full_name
                hint_text: "Full Name"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                # line_color_normal: "#A08264"
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
            MDTextField:
                id: phone_number
                hint_text: "Phone Number"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
                # size_hint_x: .8
            MDTextField:
                id: email
                hint_text: "Email Address"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
                # size_hint_x: .8
                # size_hint_y: .1
            MDTextField:
                id: username
                hint_text: "Username"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
                # size_hint_x: .8
                # size_hint_y: .1
            MDTextField:
                id: password
                hint_text: "Password"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
                # size_hint_x: .8
                # size_hint_y: .1
            MDTextField:
                id: re_enterpassword
                hint_text: "Re-enter Password"
                mode: "fill"
                text_color_focus: "#A08264"
                text_color_normal: 1, 1, 1, 1
                hint_text_color_normal: 1, 1, 1, 1
                hint_text_color_focus: "gray"
                fill_color_normal: "#E5BD94"
                fill_color_focus: 1, 1, 1, 1
                line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
                radius: [30, 30, 30, 30]
                write_tab: False
                adaptive_height: True
                on_text: self.text = self.text.replace(" ", "")
                # size_hint_x: .8
                # size_hint_y: .1
            MDLabel:
                text: "     "
                font_size: 10
                adaptive_height: True
            MDBoxLayout:
                orientation: "vertical"
                adaptive_height: True
                MDLabel:
                    text: "Your privacy is important and safe to us. The collection, use, and disclosure of your personal data shall be in accordance with RA 10173 - Data Privacy Act of 2012."
                    font_name: "Poppins"
                    font_size: 14
                    halign: "center"
                    adaptive_height: True
                    theme_text_color: "Custom"
                    text_color: "#A08264"
                    padding:[20, 0, 20, 20]
                MDRaisedButton:
                    text: "Sign Up"
                    font_size: "15sp"
                    font_name: "Poppins"
                    text_color: "white"
                    md_bg_color: "#A08264"
                    line_color: (0, 0, 0, 0)
                    size_hint_x: .5
                    pos_hint: {"center_x": .5}
                    adaptive_height: True
                    on_release: root.signup()
                MDLabel:
                    text: "     "
                    font_size: 50
                    adaptive_height: True
                MDLabel:
                    text: "Already have an account?"
                    font_name: "BPoppins"
                    font_size: "11sp"
                    halign: "center"
                    theme_text_color :"Custom"
                    text_color: "#A08264"
                    # pos_hint: {"center_y":.07}
                    adaptive_height: True
                MDTextButton:
                    text: "Sign In"
                    underline: True
                    font_name: "Poppins"
                    font_size: "11sp"
                    theme_text_color :"Custom"
                    text_color: "#A08264"
                    pos_hint:{ "center_x":.5}
                    adaptive_height: True
                    on_release: root.go_to_login_screen()
                    
# <SuccessScreen>:
#     Label: 
#         text: 'Signup Successful'
# <ScreenManager>:
#     Signup:
#         name:'signup'
#     SuccessScreen:
#         name: 'success'
           

                

'''

Builder.load_string(KV)

class SignUp(Screen):
    def go_to_login_screen(self, *args):
        self.manager.current = "login_screen"

    # def go_to_home_screen(self, *args):
    #     self.manager.current = "home_screen"
        
    def signup(self):
        fullname=self.ids.full_name.text
        phonenumber=self.ids.phone_number.text
        email=self.ids.email.text
        username=self.ids.username.text
        password=self.ids.password.text
        reenter=self.ids.re_enterpassword.text
        
        try:
            user=firebase_auth.authentication.create_user_with_email_and_password(
                email=email,
                password=password
            )
            
            #Store data
            
            collection=db.collection('users')
            user_data={
                'fullname': fullname,
                'phonenumber': phonenumber,
                'email': email,
                'username': username,
                'reenterpassword': reenter,
                'uid': user['localId']
            }
            
            collection.document(user['localId']).set(user_data)
            
            self.manager.current='success'
            self.clear_inputs()
            
        except Exception as e:
            print('Signup Error:', e)
        
    def clear_inputs(self):
        self.ids.full_name.text=''
        self.ids.phone_number.text=''
        self.ids.email.text=''
        self.ids.username.text=''
        self.ids.password.text=''
        self.ids.re_enterpassword.text=''
        
# class SuccessScreen(Screen):
#     pass

# class MyApp(MDApp):
#     def build(self):
        
#         sm=ScreenManager()
#         sm.add_widget(SignUp())
#         sm.add_widget(SuccessScreen())
#         return sm
    
# if __name__ == '__main__':
#     MyApp().run()
            
            
            
