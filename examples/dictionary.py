import justpy as jp
from justpy import tailwind
from examples.layout import DefaultLayout
from examples.definition import Definition
from examples.page import Page


class Dictionary(Page):
    path = "/dictionary"

    @classmethod
    def serve(cls, rqs):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instatnt English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the defenition of any English word instatntly as you type.",
               classes="text-lg m-2")
        div2 = jp.Div(a=div, classes="grid grid-cols-2")
        input = jp.Input(a=div2, placeholder="Type in a word here...",
                         classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:outline-none focus:bg-white focus:border-purple-500 py-2 px-4")
        output_div = jp.Div(
            a=div, text="", classes="text-lg border-2 m-2 p-2 h-40")
        jp.Button(a=div2, text="Get the definition",
                  classes="m-2 p-2 text-lg border-2 h-20", click=cls.get_def, output=output_div, input1=input)
        return wp

    @staticmethod
    def get_def(widget, msg):
        d = Definition(term=widget.input1.value)
        # gets term from input and refers it to class
        widget.output.text = ";".join(d.get())
        # gets a tuple before adding .join
        # calls function 'get' of a class and changes an empty output field to the result of get function

    # widget.input1.value - value gets the info from jp.Input
    # d = Definition(term=widget.input1.value).get() OR! widget.output.text = d.get()

    #widget.output.text = ";".join(d.get())
    # ";".join is a method of stings
