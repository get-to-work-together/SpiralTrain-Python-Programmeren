
class Button:

    def __init__(self, button_type):
        self.button_type = button_type

    def get_html(self):
        if self.button_type == 'image':
            return "<img></img>"
        elif self.button_type == 'input':
            return "<input></input>"
        elif self.button_type == 'div':
            return "<div></div>"


btn1 = Button('image')
print(btn1.get_html())

btn1 = Button('input')
print(btn1.get_html())


class Button(object):
    html = ""
    def get_html(self):
        return self.html

class Image(Button):
    html = "<img></img>"

class Input(Button):
    html = "<input></input>"

class Div(Button):
    html = "<div></div>"


btn1 = Image()
print(btn1.get_html())

btn1 = Input()
print(btn1.get_html())



# class ButtonFactory():
#     def create_button(self, button_type):
#         targetclass = button_type.capitalize()
#         return globals()[targetclass]()

# for button_type in ['image', 'input', 'div'] :
#     button = ButtonFactory.create_button(button_type)
#     print(button.get_html())
