from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup


kv='''

<Login>:
    canvas:
        Color:
            rgba: 0.941, 0.886, 0.835, 1                  #F0E2D5
        Rectangle:
            pos: self.pos
            size: self.size

    Image:
        source:"assets//logo.png"
        size_hint: None, None
        size: 350, 350  # Set the desired size of the image
        pos_hint: {"center_x": .5, "y":.61}
    MDLabel:
        text: "CACAO GUARD"
        font_name: "Raleway-Black.ttf"
        font_size: 25
        halign: "center"
        pos_hint: {"center_y": .61}
        theme_text_color: "Custom"
        text_color: "#A08264"
        # padding:[40,0]
    MDTextField:
        id: username
        mode: "fill"
        hint_text: "Username"
        text_color_focus: "#A08264"
        text_color_normal: "#A08264"
        hint_text_color_normal: "#A08264"
        hint_text_color_focus: "gray"
        fill_color_normal: 1, 1, 1, 1
        # fill_color_focus: 1, 1, 1, 1
        line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
        pos_hint:{"center_x": .5, "center_y": .51}
        radius: [30, 30, 30, 30]
        # adaptive_height: True
        size_hint_x: .8
        # required: True
        write_tab: False
        on_text: self.text = self.text.replace(" ", "")
    MDTextField:
        id: password_input
        mode: "fill"
        hint_text: "Password"
        # icon_right: "eye-off"
        # icon_right_color_focus: "#A08264"
        text_color_focus: "#A08264"
        text_color_normal: "#A08264"
        hint_text_color_normal: "#A08264"
        hint_text_color_focus: "gray"
        fill_color_normal: 1, 1, 1, 1
        # fill_color_focus: 1, 1, 1, 1
        line_color_focus: 0.941, 0.886, 0.835, 1                  #F0E2D5
        radius: [30, 30, 30, 30]
        padding: [40, 0, 0, 0]
        pos_hint: {"center_x": .5, "center_y": .4}
        size_hint_x: .8
        password: True
        # required: True
        write_tab: False
        on_text: self.text = self.text.replace(" ", "")
    MDIconButton:
        id: eye_icon
        icon: "eye-off"
        theme_icon_color: "Custom"
        icon_color: "#A08264"
        pos_hint: {"center_x": .8, "center_y": .4}
        opacity: 1 if password_input.text else 0
        # disabled: not password_input.text or password_input.text.isspace()
        on_press:
            password_input.password = not password_input.password
        on_press:
            eye_icon.icon = "eye" if password_input.password else "eye-off"
    MDTextButton:
        text: "Forgot Password?"
        font_name: "Poppins"
        underline: True
        font_size: "11sp"
        theme_text_color :"Custom"
        text_color: "#A08264"
        pos_hint:{"center_x":.5, "center_y":.28}
    MDRaisedButton:
        text: "Sign In"
        font_size: "15sp"
        font_name: "Raleway-Black.ttf"
        text_color: "white"
        md_bg_color: "#A08264"
        line_color: (0, 0, 0, 0)
        size_hint_x: .5
        pos_hint: {"center_x": .5, "center_y": .2}
        on_release: root.go_to_home_screen()
    MDLabel:
        text: "Don't have an account?"
        font_name: "BPoppins"
        font_size: "11sp"
        halign: "center"
        theme_text_color :"Custom"
        text_color: "#A08264"
        pos_hint: {"center_y":.1}
    MDTextButton:
        text: "Create an account"
        underline: True
        font_name: "Poppins"
        font_size: "11sp"
        theme_text_color :"Custom"
        text_color: "#A08264"
        pos_hint:{ "center_x":.5, "center_y":.07}
        on_release: root.go_to_signup_screen()
        
'''

Builder.load_string(kv)



class Login(Screen):
    def go_to_home_screen(self, *args):
        self.manager.current = "home_screen"

    def go_to_signup_screen(self, *args):
        self.manager.current = "signup_screen"

















    # def validate_password(self):
    #     password = self.root.get_screen("login_screen").ids.password_input.text
    #     error_message = ''

    #     if len(password) < 8:
    #         error_message = 'Password must be at least 8 characters long.'
    #     elif not re.search(r'[a-z]', password):
    #         error_message = 'Password must contain at least one lowercase letter.'
    #     elif not re.search(r'[A-Z]', password):
    #         error_message = 'Password must contain at least one uppercase letter.'
    #     elif not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
    #         error_message = 'Password must contain at least one special character.'

    #     if error_message:
    #         self.root.get_screen("login_screen").ids.password_input.helper_text = error_message
    #         self.root.get_screen("login_screen").ids.password_input.error = True
    #     else:
    #         self.show_success_dialog()

    # def reset_helper_text(self):
    #     screen_manager = self.root
    #     login_screen = screen_manager.get_screen("login_screen")
    #     password_input = login_screen.ids.password_input

    #     password_input.helper_text = ""
    #     password_input.error = False

    # def show_success_dialog(self):
    #     dialog = MDDialog(
    #         text='Password is valid!',
    #         buttons=[
    #             MDFlatButton(
    #                 text='OK',
    #                 on_release=self.dismiss_dialog
    #             )
    #         ]
    #     )
    #     dialog.open()

    # def dismiss_dialog(self, instance):
    #     instance.parent.parent.dismiss()
