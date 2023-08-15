# pip install kivy
import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

# Class for the grid layout of app
class LibraryGrid(GridLayout):
    
    def __init__(self, **kwargs):
        super(LibraryGrid, self).__init__()
        self.cols = 5
        
        # 1st row for name addition
        self.add_widget(Label(text="Student Name"))
        self.add_name = TextInput()
        self.add_widget(self.add_name)
        
        # 2nd row for books borrowed
        self.add_widget(Label(text="Name of Book"))
        self.add_book = TextInput()
        self.add_widget(self.add_book)

        # 3rd row for book issue date
        self.add_widget(Label(text="Issue date of Book"))
        self.add_isdt = TextInput()
        self.add_widget(self.add_isdt)
        
        # 4th row for book return date
        self.add_widget(Label(text="Return date of Book"))
        self.add_rtndt = TextInput()
        self.add_widget(self.add_rtndt)
        
        # 5th row for book fine
        self.add_widget(Label(text="Book Fine"))
        self.add_bkfine = TextInput()
        self.add_widget(self.add_bkfine)
        
        # Button for extra information
        self.pressBtn = Button(text="Click to get Information")
        self.pressBtn.bind(on_press = self.click_me)
        self.add_widget(self.pressBtn)
        
    def click_me(self, instance):
        print("Name of the student : ")
        print(self.add_name.text)
        print("Name of the book : ")
        print(self.add_book.text)
        print("Issue date of the book : ")
        print(self.add_isdt.text)
        print("Return date of the book : ")
        print(self.add_rtndt.text)
        print("Fine for the book : ")
        print(self.add_bkfine.text)
        

# Main App class
class ClgLibraryApp(App):
    def build(self):
        return LibraryGrid()
    
    
# main function
if __name__ == "__main__":
    ClgLibraryApp().run()