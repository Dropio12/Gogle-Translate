from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
Builder.load_string('''
<CameraClick>:
    orientation: 'vertical'
    Camera:
        id: camera
        resolution: (640, 480)
        play: False
    ToggleButton:
        text: 'Play'
        on_press: camera.play = not camera.play
        size_hint_y: None
        height: '48dp'
    Button:
        text: 'Capture'
        size_hint_y: None
        height: '48dp'
        pos_hint: {'center_x': .5}
        icon: "circle"
        type: "custom"
        on_press: root.capture() 
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        camera.export_to_png("IMG.png")
        print("Captured")
        self.manager.current = 'second'


class TestCamera(App):

    def build(self):
        return CameraClick()


TestCamera().run()