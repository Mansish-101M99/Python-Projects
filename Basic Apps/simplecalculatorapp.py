# pip install kivy
from kivy.app import App
from kivy.uix.button import Button 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label 

# Class for the grid layout and basic look for app
class Calculator(App):
    def build(self):
        root_widget = BoxLayout(orientation = "vertical")
        output_label = Label(size_hint_y = 0.75, font_size = 50)
        
        # Buttons over the layout
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '*',
                          '.', '0', '/', '=')
        
        # Setting the layout for buttons
        button_grid = GridLayout(cols = 4, size_hint_y = 2)
        for smb in button_symbols:
            button_grid.add_widget(Button(text = smb))
            
        # CLEAR button
        clear_btn = Button(text = "CLEAR", size_hint_y = None, height = 100)
        
        # Printing the text from buttonpad
        def print_button_text(instance):
            output_label.text += instance.text
            
        for btn in button_grid.children[1:]:
            btn.bind(on_press = print_button_text) 
            
        # Height of numbers
        def resize_label_text(label, new_height):
            label.fontsize = 0.5 * label.height
        output_label.bind(height = resize_label_text)
        
        # Figuring out the result
        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = "Python Syntax Error"
        button_grid.children[0].bind(on_press = evaluate_result)
        
        def clear_label(instance):
            output_label.text = " "
        clear_btn.bind(on_press = clear_label)
        
        # Adding all the elements into the layout
        root_widget.add_widget(output_label)
        root_widget.add_widget(button_grid)
        root_widget.add_widget(clear_btn)
        return root_widget
                

# main function
if __name__ == "__main__":
    Calculator().run()
