#Python 3.12.3
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.app import runTouchApp
from kivy.lang import Builder
from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.uix.dropdown import DropDown
from kivy.uix.spinner import Spinner
from kivy.utils import platform
from kivy.properties import StringProperty
from pathlib import Path
import json
from kivy.storage.jsonstore import JsonStore
import os
import shutil

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])

Window.clearcolor = (50/255.0, 134/255.0, 230/255.0, 0.8)

# KV-Code
Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Label:
            text: "Gym-Notiz"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint: None, 0.3
            pos_hint: {"center_x":0.5}
            
        Image:
            source: "logo.png"

        Spinner:
            id: spinner
            size_hint: None, None
            font_size: 40
            width: 490
            pos_hint: {"center_x":0.5}
            text: "Trainingsgerät auswählen"
            values: "Bankdrücken", "Schrägbankdrücken (Kurzhanteln)", "Brustpresse", "Bizepsmaschine", "Butterfly", "Fahrradtrainer", "Beinpresse", "Laufen"
            on_text:
                root.manager.current = self.text
            on_press:
                root.manager.transition.direction = "left"

        Button:
            text: "   ...\\nMehr"
            id: test
            size_hint: None, 0.2
            font_size: 40
            width: 40
            height: 40
            color: 0, 0, 0, 0.67
            pos_hint: {"center_x":0.5}
            background_color: 0, 0, 0, 0
            on_press:
                root.manager.current = "mehr"
                root.manager.transition.direction = "left"

#--------------------------------------------------------

<Bankdrücken>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Bankdrücken"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 3
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilo / LBS"
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            font_size: 45
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: bankdruecken_textfeld_1
            font_size: 45
            height: 65
            size_hint: 1, None
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('bankdruecken')['bankruecken_kg'] if root.stored_data.exists('bankdruecken') else ""

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
 
        TextInput:
            id: bankdruecken_textfeld_2
            font_size: 45
            height: 65
            size_hint: 1, None
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('bankdruecken')['bankruecken_wiederholungen'] if root.stored_data.exists('bankdruecken') else ""
            input_filter: "int" 
                        
        AsyncImage:
            size_hint_y: 10
            source: "bankdruecken.png"
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if bankdruecken_textfeld_1.text == '' or bankdruecken_textfeld_2.text == '' else False
            on_release:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                bankdruecken_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('bankdruecken', bankruecken_kg=bankdruecken_textfeld_1.text, bankruecken_wiederholungen=bankdruecken_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Schrägbankdrücken>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Schrägbankdrücken (Kurzhanteln)"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 6
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilo / LBS"
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            font_size: 45
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: schraegbankdruecken_textfeld_1
            font_size: 45
            height: 65
            size_hint: 1, None
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('schraegbankdruecken')['text'] if root.stored_data.exists('schraegbankdruecken') else ""

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            height: 65
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: schraegbankdruecken_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('schraegbankdruecken')['text2'] if root.stored_data.exists('schraegbankdruecken') else ""
            input_filter: "int"

        AsyncImage:
            size_hint_y: 15
            source: "schraegbankdruecken_(kurzhanteln).png"
            height: 100
            width: 150
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if schraegbankdruecken_textfeld_1.text == '' or schraegbankdruecken_textfeld_2.text == '' else False
            on_release:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                schraegbankdruecken_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('schraegbankdruecken', text=schraegbankdruecken_textfeld_1.text, text2=schraegbankdruecken_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Bizepsmaschine>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Bizepsmaschine"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 4
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilo / LBS"
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            font_size: 45
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: bizepsmaschine_textfeld_1
            font_size: 45
            height: 65
            size_hint: 1, None
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('bizepsmaschine')['text'] if root.stored_data.exists('bizepsmaschine') else ""

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: bizepsmaschine_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('bizepsmaschine')['text2'] if root.stored_data.exists('bizepsmaschine') else ""
            input_filter: "int"

        AsyncImage:
            size_hint_y: 15
            source: "bizepsmaschine.png"
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if bizepsmaschine_textfeld_1.text == '' or bizepsmaschine_textfeld_2.text == '' else False
            on_press:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                bizepsmaschine_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('bizepsmaschine', text=bizepsmaschine_textfeld_1.text, text2=bizepsmaschine_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_press:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Brustpresse>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Brustpresse"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 4
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilo / LBS"
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: brustpresse_textfeld_1
            font_size: 45
            height: 65
            size_hint: 1, None
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('brustpresse')['text'] if root.stored_data.exists('brustpresse') else ""

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: brustpresse_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('brustpresse')['text2'] if root.stored_data.exists('brustpresse') else ""
            input_filter: "int"

        AsyncImage:
            size_hint_y: 15
            source: "brustpresse.png"
            height: 100
            width: 150
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if brustpresse_textfeld_1.text == '' or brustpresse_textfeld_2.text == '' else False
            on_press:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                brustpresse_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('brustpresse', text=brustpresse_textfeld_1.text, text2=brustpresse_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_press:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Butterfly>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Butterfly"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 3
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: ""
            size_hint: None, 0.8

        Label:
            text: "Kilo / LBS"
            size_hint: 1, None
            font_size: 45
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: butterfly_textfeld_1
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('butterfly')['text'] if root.stored_data.exists('butterfly') else ""
    
            on_text_validate: 
                if self.text: root.create_a_button(self.text)

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: butterfly_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('butterfly')['text2'] if root.stored_data.exists('butterfly') else ""
            input_filter: "int"

        AsyncImage:
            size_hint_y: 15
            source: "butterfly.png"
            height: 100
            width: 150
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if butterfly_textfeld_1.text == '' or butterfly_textfeld_2.text == '' else False
            on_release:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                butterfly_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('butterfly', text=butterfly_textfeld_1.text, text2=butterfly_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Fahrradtrainer>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Fahrradtrainer"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 4
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilometer / Mile"
            size_hint: 1, None
            font_size: 45
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67

        TextInput:
            id: fahrradtrainer_textfeld_1
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('fahrradtrainer')['text'] if root.stored_data.exists('fahrradtrainer') else ""

        Label:
            text: "Zeit (Stunden : Minuten : Sekunden)"
            padding: 0, 20, 0, 0
            font_size: 40
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: fahrradtrainer_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('fahrradtrainer')['text2'] if root.stored_data.exists('fahrradtrainer') else ""

        AsyncImage:
            size_hint_y: 15
            source: "fahrradtrainer.png"
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if fahrradtrainer_textfeld_1.text == '' or fahrradtrainer_textfeld_2.text == '' else False
            on_press:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                fahrradtrainer_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('fahrradtrainer', text=fahrradtrainer_textfeld_1.text, text2=fahrradtrainer_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_press:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                

#--------------------------------------------------------

<Beinpresse>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Beinpresse"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 4
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilo / LBS"
            size_hint: 1, None
            font_size: 45
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: beinpresse_textfeld_1
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('beinpresse')['text'] if root.stored_data.exists('beinpresse') else ""
    
            on_text_validate: 
                if self.text: root.create_a_button(self.text)

        Label:
            text: "Wiederholungen"
            padding: 0, 20, 0, 0
            font_size: 45
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: beinpresse_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('beinpresse')['text2'] if root.stored_data.exists('beinpresse') else ""
            input_filter: "int"

        AsyncImage:
            size_hint_y: 15
            source: "beinpresse.png"
            height: 100
            width: 150
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if beinpresse_textfeld_1.text == '' or beinpresse_textfeld_2.text == '' else False
            on_release:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                beinpresse_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('beinpresse', text=beinpresse_textfeld_1.text, text2=beinpresse_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_release:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"

#--------------------------------------------------------

<Laufen>:
    BoxLayout:
        orientation: "vertical"
        padding: 40,0,40,20

        Label:
            text: "Laufen"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 4
            height: self.texture_size[1]
            text_size: self.width, None

        Label:
            text: "Kilometer / Mile"
            size_hint: 1, None
            font_size: 45
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67

        TextInput:
            id: laufen_textfeld_1
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            input_filter: "float"
            text: root.stored_data.get('laufen')['text'] if root.stored_data.exists('laufen') else ""

        Label:
            text: "Zeit (Stunden : Minuten : Sekunden)"
            padding: 0, 20, 0, 0
            font_size: 40
            size_hint: 1, None
            text_size: self.width, None
            height: self.texture_size[1]
            color: 0, 0, 0, 0.67
            
        TextInput:
            id: laufen_textfeld_2
            font_size: 45
            size_hint: 1, None
            height: 65
            pos_hint: {"center_x":0.5}
            text: root.stored_data.get('laufen')['text2'] if root.stored_data.exists('laufen') else ""

        AsyncImage:
            size_hint_y: 15
            source: "laufen.png"
            height: 100
            width: 150
            allow_stretch: True

        Button:
            id: button_speichern
            text: "Speichern"
            pos_hint: {"center_x":0.5}
            size_hint: 0, None
            font_size: 45
            width: 250
            height: 60
            disabled: True if laufen_textfeld_1.text == '' or laufen_textfeld_2.text == '' else False
            on_press:
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"
                laufen_textfeld_1.focus = True
                root.manager.transition.direction = "right"
                root.stored_data.put('laufen', text=laufen_textfeld_1.text, text2=laufen_textfeld_2.text)

        Button:
            text: "< Zurück"
            size_hint: 0.3, None
            font_size: 40
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_press:
                root.manager.transition.direction = "right"
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.get_screen("Trainingsgerät auswählen").ids.spinner.text = "Trainingsgerät auswählen"


<mehr>:
    BoxLayout:
        orientation: "vertical"
        spacing: 10
        padding: 20

        Label:
            text: "Was ist Gym-Notiz?"
            font_size: 70
            color: 0, 0, 0, 0.67
            size_hint_y: 0.8
            height: self.texture_size[1]
            padding: 20, 20, 0, 0
            text_size: self.width, None

        Label:
            text: "Gym-Notiz ist eine App mit der man schnell und einfach das Rekordgewicht und Wiederholungen von verschiedenen Fitnessgeräten speichern und abrufen kann."
            text_size: self.width, None
            height: self.texture_size[1]
            padding: 30, 20, 40, 0
            font_size: 45
            color: 0, 0, 0, 0.67

        Label:
            text: " "
            size_hint_y: 2.5
            font_size: 18
            color: 0, 0, 0, 0.67

        Label:
            text: "Version 1.0\\ncreated by P A G O O K"
            size_hint: 1.5, None
            font_size: 25
            color: 0, 0, 0, 0.67

        Button:
            text: "< Zurück"
            size_hint: 0.4, None
            size_hint_y: 0.4
            font_size: 50
            width: 130
            height: 50
            background_color: 0, 0, 0, 0
            color: 0, 0, 0, 0.67
            on_press:
                root.manager.current = "Trainingsgerät auswählen"
                root.manager.transition.direction = "right"
""")

class MenuScreen(Screen):
    pass

class Bankdrücken(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/bankdruecken.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/bankdruecken.json")


class Schrägbankdrücken(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/schraegbankdruecken.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/schraegbankdruecken.json")
    
class Bizepsmaschine(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/bizepsmaschine.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/bizepsmaschine.json")

class Brustpresse(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/brustpresse.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/brustpresse.json")
    
class Beinpresse(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/beinpresse.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/beinpresse.json")

class Laufen(Screen):
    path_specified = "/storage/emulated/0/gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/laufen.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/laufen.json")

class Fahrradtrainer(Screen):
    path_specified = "gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/fahrradtrainer.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/fahrradtrainer.json")

class Butterfly(Screen):
    path_specified = "gym_notiz"
    if not os.path.exists(path_specified):
            os.makedirs(path_specified)
    else:
            pass
    stored_data = JsonStore("/storage/emulated/0/gym_notiz/butterfly.json")
def __init__(self, *args, **kwargs):
    super(BoxLayout, self).__init__(*args, **kwargs)
    self.stored_data = JsonStore("/storage/emulated/0/gym_notiz/butterfly.json")

class mehr(Screen):
    pass

class MainApp(App):
    def build(self):
        self.icon = r'icon.png'
        layout_vertical = BoxLayout(orientation="vertical", spacing=10, padding=20)

        sm = ScreenManager()
        sm.add_widget(MenuScreen(name="Trainingsgerät auswählen"))
        sm.add_widget(Bankdrücken(name="Bankdrücken"))
        sm.add_widget(Schrägbankdrücken(name="Schrägbankdrücken (Kurzhanteln)"))
        sm.add_widget(Brustpresse(name="Brustpresse"))
        sm.add_widget(Bizepsmaschine(name="Bizepsmaschine"))
        sm.add_widget(Butterfly(name="Butterfly"))
        sm.add_widget(Fahrradtrainer(name="Fahrradtrainer"))
        sm.add_widget(Beinpresse(name="Beinpresse"))
        sm.add_widget(Laufen(name="Laufen"))
        sm.add_widget(mehr(name="mehr"))
        return sm
        return layout_vertical

if __name__ == "__main__":
    MainApp().run()
