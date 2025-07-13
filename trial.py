from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.clock import Clock
import random

Window.size = (400, 600)

KV = '''
Screen:
    MDNavigationLayout:

        ScreenManager:
            id: screen_manager

            MainScreen:
            SOCScreen:
            CurrentScreen:
            VoltageScreen:
            InfoScreen:

        MDNavigationDrawer:
            id: nav_drawer
            drawer_width: 240

            BoxLayout:
                orientation: 'vertical'
                padding: '10dp'
                spacing: '10dp'

                MDLabel:
                    text: 'Information Menu'
                    font_style: 'H6'
                    size_hint_y: None
                    height: self.texture_size[1]
                    halign: 'center'

                ScrollView:
                    MDList:
                        id: drawer_list

                        OneLineIconListItem:
                            text: 'SOC of the battery'
                            on_release:
                                app.root.ids.screen_manager.transition.direction = 'left'
                                screen_manager.current = 'soc'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'battery-charging'

                        OneLineIconListItem:
                            text: 'Input current'
                            on_release:
                                app.root.ids.screen_manager.transition.direction = 'left'
                                screen_manager.current = 'current'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'current-ac'

                        OneLineIconListItem:
                            text: 'Input voltage'
                            on_release:
                                app.root.ids.screen_manager.transition.direction = 'left'
                                screen_manager.current = 'voltage'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'flash'

                        OneLineIconListItem:
                            text: 'Battery info'
                            on_release:
                                app.root.ids.screen_manager.transition.direction = 'left'
                                screen_manager.current = 'info'
                                nav_drawer.set_state("close")
                            IconLeftWidget:
                                icon: 'information'

<MainScreen>:
    name: 'main'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Battery Monitor"
            left_action_items: [["menu", lambda x: app.root.ids.nav_drawer.set_state("toggle")]]
            elevation: 3

        ScrollView:
            BoxLayout:
                orientation: 'vertical'
                padding: '20dp'
                spacing: '20dp'
                size_hint_y: None
                height: self.minimum_height
                pos_hint: {'top': 1}

                MDRectangleFlatButton:
                    text: "Check SOC of the battery"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "60dp"
                    on_release:
                        app.root.ids.screen_manager.transition.direction = 'left'
                        root.manager.current = 'soc'

                MDRectangleFlatButton:
                    text: "Check input current of the battery"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "60dp"
                    on_release:
                        app.root.ids.screen_manager.transition.direction = 'left'
                        root.manager.current = 'current'

                MDRectangleFlatButton:
                    text: "Check the voltage of the battery"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "60dp"
                    on_release:
                        app.root.ids.screen_manager.transition.direction = 'left'
                        root.manager.current = 'voltage'

                MDRectangleFlatButton:
                    text: "View the information of the battery"
                    size_hint_x: 1
                    size_hint_y: None
                    height: "60dp"
                    on_release:
                        app.root.ids.screen_manager.transition.direction = 'left'
                        root.manager.current = 'info'

<SOCScreen>:
    name: 'soc'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "SOC Screen"
            left_action_items: [["arrow-left", lambda x: setattr(app.root.ids.screen_manager.transition, "direction", "right") or setattr(root.manager, "current", "main")]]
            elevation: 6

        MDLabel:
            id: soc_label
            text: "SOC: 0%"
            halign: "center"
            font_style: "H5"

<CurrentScreen>:
    name: 'current'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Current Screen"
            left_action_items: [["arrow-left", lambda x: setattr(app.root.ids.screen_manager.transition, "direction", "right") or setattr(root.manager, "current", "main")]]
            elevation: 6

        MDLabel:
            id: current_label
            text: "Current: 0 A"
            halign: "center"
            font_style: "H5"

<VoltageScreen>:
    name: 'voltage'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Voltage Screen"
            left_action_items: [["arrow-left", lambda x: setattr(app.root.ids.screen_manager.transition, "direction", "right") or setattr(root.manager, "current", "main")]]
            elevation: 6

        MDLabel:
            id: voltage_label
            text: "Voltage: 0 V"
            halign: "center"
            font_style: "H5"

<InfoScreen>:
    name: 'info'
    BoxLayout:
        orientation: 'vertical'

        MDTopAppBar:
            title: "Battery Info"
            left_action_items: [["arrow-left", lambda x: setattr(app.root.ids.screen_manager.transition, "direction", "right") or setattr(root.manager, "current", "main")]]
            elevation: 6

        MDLabel:
            text: "Battery Details Here"
            halign: "center"
            font_style: "H5"
'''

class MainScreen(Screen): pass
class SOCScreen(Screen): pass
class CurrentScreen(Screen): pass
class VoltageScreen(Screen): pass
class InfoScreen(Screen): pass

class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        root = Builder.load_string(KV)
        Clock.schedule_interval(self.update_values, 1)
        return root

    def update_values(self, dt):
        soc = random.randint(0, 100)
        current = round(random.uniform(0.0, 10.0), 2)
        voltage = round(random.uniform(10.0, 14.0), 2)

        
        self.root.ids.screen_manager.get_screen('soc').ids.soc_label.text = f"SOC: {soc} %"
        self.root.ids.screen_manager.get_screen('current').ids.current_label.text = f"Current: {current} A"
        self.root.ids.screen_manager.get_screen('voltage').ids.voltage_label.text = f"Voltage: {voltage} V"
        

MyApp().run()
