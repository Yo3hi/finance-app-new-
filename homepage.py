import kivy
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput 
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.uix.button import Button 
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp
kivy.require('1.9.0')



class homepage(Screen):
    
    
    def __init__(self):
        super(homepage, self).__init__()




class sign_in_page(Screen):

    def __init__(self):
        super(sign_in_page, self).__init__()
    
        self.add_widget(Label(text="Username: ")) 

        #adding widget 

        self.username = TextInput(multiline=False) 

        #adding input box  

        self.add_widget(self.username) 
        
        #adding widget 

    

        self.add_widget(Label(text="password: ")) 

        self.password = TextInput(multiline=False) 

        self.add_widget(self.password) 

    

        self.submit = Button(text = "Submit", font_size = 32) 

        self.submit.bind(on_press=self.press) 

        self.add_widget(self.submit) 

 

    def press(self, instance): 

        #values gotten from the textinputs 

        username = self.username.text 

        password = self.password.text 

        print("hello " + username + " are you a sigma and is your password " + password + "?") 

    
        



    

class financeapp(App):

    
        
    def build(self):
        sm = ScreenManager()
        sm.add_widget(homepage(name='homepagescreen'))
        sm.add_widget(sign_in_page(name='signinscreen'))
        
        return homepage
        
    


financeapp().run()
