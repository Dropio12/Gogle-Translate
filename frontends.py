from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.menu import MDDropdownMenu


KV = '''
<MDBoxLayout>
    orientation: "vertical"
    md_bg_color: "#FFEFD3"
    MDNavigationLayout:
        ScreenManager:
            Screen:
                MDBoxLayout:
                    orientation: "vertical"
                    MDToolbar:
                        title: "My App"
                        elevation: 10
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                        right_action_items: [["dots-vertical", lambda x: nav_drawer.set_state("open")]]
                        md_bg_color: "#FFEFD3"
                    Widget:
            Screen:
                name: 'LoginScreen'
                username: username
                password: password
                output_label: output_label
                login_button: login_button
                register_button: register_button
                MDButton:
                    id: register_button
                    text: 'Register'
                    on_press: root.manager.current = 'RegisterWindow'
                MDButton:
                    id: login_button
                    text: 'Login'
                    font_size: 30
                    background_color: 0, 0, 1, 1
                    size_hint: 0.5, 0.1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_press: root.confirm()
                Label:
                    text: "Sign In"
                    halign: "center"
                    font_size: "40sp"
                    font_style: "Button"
                    pos_hint: {"center_x": .5, "center_y": .70}
                    font_name: "DejaVuSans.ttf"
                    color: "#FFA500"
                MDTextField:
                    id: password
                    hint_text: 'Enter your password'
                    helper_text: 'Forgot your password?'
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                    size_hint_x: None
                    width: 300
                    icon_right: "account-search"
                    required: True
                MDTextField:
                    id: username
                    hint_text: 'Enter your username'
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.55}
                    size_hint_x: None
                    width: 300
                    required: True
            Screen:
                name: 'RegisterWindow'
                username: username
                password: password
                output_label: output_label
                MDLabel:
                    text: "Register"
                    halign: "center"
                    font_size: "40sp"
                    font_style: "Button"
                    pos_hint: {"center_x": .5, "center_y": .70}
                    font_name: "DejaVuSans.ttf"
                    color: "#FFA500"
                MDTextField:
                    id: password
                    hint_text: 'Enter your password'
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                    size_hint_x: None
                    width: 300
                    icon_right: "account-search"
                    required: True
                MDTextField:
                    id: password_confirmation
                    hint_text: 'Confirm your password'
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                    size_hint_x: None
                    width: 300
                    icon_right: "account-search"
                    required: True
                MDTextField:
                    id: username
                    hint_text: 'Enter your email or username'
                    helper_text_mode: "on_focus"
                    pos_hint: {'center_x': 0.5, 'center_y': 0.55}
                    size_hint_x: None
                    width: 300
                    required: True
                MDButton:
                    id: register_button
                    text: 'Register'
                    font_size: 30
                    background_color: 0, 0, 1, 1
                    size_hint: 0.5, 0.1
                    pos_hint: {'center_x': 0.5, 'center_y': 0.5}
                    on_press: root.register()     
            Screen:
                name: 'HomeScreen'
                MDToolbar:
                    title: "Home"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["dots-vertical", lambda x: nav_drawer.set_state("open")]]
                    md_bg_color: "#FFEFD3"
                Widget:     
            Screen:
                name: 'ProfileScreen'
                MDToolbar:
                    title: "Profile"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["dots-vertical", lambda x: nav_drawer.set_state("open")]]
                    md_bg_color: "#FFEFD3"
                Widget:    
            Screen:
                name: 'Translation'
                GridLayout:
                    cols: 1
                    padding: 10
                    spacing: 10
                    MDToolbar:
                        title: 'Translation'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        elevation: 10
                        pos_hint: {'top': 1}
                    Label:
                        text: 'Translation'
                        halign: 'center'
                        font_style: 'H4'
                        theme_text_color: 'Primary'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDTextField:
                        id: input_text
                        hint_text: 'Enter your text'
                        helper_text_mode: "on_focus"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        size_hint_x: None
                        width: 300
                        icon_right: "account-search"
                        required: True
                    MDTextField:
                        id: output_text
                        hint_text: 'Translated text'
                        helper_text_mode: "on_focus"
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        size_hint_x: None
                        width: 300
                        icon_right: "account-search"
                        required: True
                    MDRaisedButton:
                        text: 'Translate'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        on_press: root.translate()
                    Label:
                        id: output_label
                        text: ''
                        halign: 'center'
                        font_style: 'H4'
                        theme_text_color: 'Primary'
                        size_hint_y: None
                        height: self.texture_size[1]
            Screen:
                    name: 'Camera'
                    MDBottomAppBar:
                        md_bg_color: "#F02D3A"
                        MDTopAppBar:
                            icon: "circle"
                            type: "custom"
                            type: "bottom"
                            icon_color: "#F02D3A"
                            on_action_button: app.camera()
            Screen:
                name: 'Settings'
                MDToolbar:
                    title: "Settings"
                    elevation: 10
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    right_action_items: [["dots-vertical", lambda x: nav_drawer.set_state("open")]]
                    md_bg_color: "#FFEFD3"
                Widget:
            Screen:
                name: 'Home1'
                GridLayout:
                    cols: 1
                    padding: 10
                    spacing: 10
                    MDToolbar:
                        title: 'Home'
                        left_action_items: [['menu', lambda x: nav_drawer.set_state()]]
                        elevation: 10
                        pos_hint: {'top': 1}
                    Label:
                        text: 'Home'
                        halign: 'center'
                        font_style: 'H4'
                        theme_text_color: 'Primary'
                        size_hint_y: None
                        height: self.texture_size[1]
                    MDRaisedButton:
                        text: 'Camera'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        on_press: root.camera()
                    MDRaisedButton:
                        text: 'Dictionary'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        on_press: root.dictionary()
                    MDRaisedButton:
                        text: 'Translation'
                        pos_hint: {'center_x': 0.5, 'center_y': 0.45}
                        on_press: root.translation()
                    MDLabel:
                        id: output_label
                        text: ''
                        halign: 'center'
                        font_style: 'H4'
                        theme_text_color: 'Primary'
                        size_hint_y: None
                        height: self.texture_size[1]
        MDNavigationDrawer:
            id: nav_drawer
            orientation: "vertical"
            padding: "8dp"
            spacing: "8dp"
            MDLabel:
                text: "My App"
                font_style: "Button"
                size_hint_y: None
                height: self.texture_size[1]
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: "Item 1"
                        IconLeftWidget:
                            icon: "android"
                    OneLineIconListItem:
                        text: "Item 2"
                        IconLeftWidget:
                            icon: "apple"
                    OneLineIconListItem:
                        text: "Item 3"
                        IconLeftWidget:
                            icon: "language-python"
                    OneLineIconListItem:
                        text: "Item 4"
                        IconLeftWidget:
                            icon: "language-cpp"
                    OneLineIconListItem:
                        text: "Item 5"
                        IconLeftWidget:
                            icon: "language-csharp"
                    OneLineIconListItem:
                        text: "Item 6"
                        IconLeftWidget:
                            icon: "language-java"
                    OneLineIconListItem:
                        text: "Item 7"
                        IconLeftWidget:
                            icon: "language-javascript"
                    OneLineIconListItem:
                        text: "Item 8"
                        IconLeftWidget:
                            icon: "language-php"
                    OneLineIconListItem:
                        text: "Item 9"
                        IconLeftWidget:
                            icon: "language-ruby"
                    OneLineIconListItem:
                        text: "Item 10"
                        IconLeftWidget:
                            icon: "language-swift"
'''


class CustomOverFlowMenu(MDDropdownMenu):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.register_event_type('on_release')
    pass


def callback(instance_action_top_appbar_button):
    print(instance_action_top_appbar_button)


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
