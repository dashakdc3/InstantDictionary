import justpy as jp
from justpy import tailwind
from examples.definition import Definition


class Dictionary:
    path = "/dictionary"

    @classmethod
    def serve(cls, rqs):
        wp = jp.QuasarPage(tailwind=True)
        div = jp.Div(a=wp, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="Instatnt English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the defenition of any English word instatntly as you type.",
               classes="text-lg m-2")
        div2 = jp.Div(a=div, classes="grid grid-cols-2")
        output_div = jp.Div(
            a=div, text="", classes="text-lg border-2 m-2 p-2 h-40")
        input1 = jp.Input(a=div2, placeholder="Type in a word here...", output=output_div,
                          classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:outline-none focus:bg-white focus:border-purple-500 py-2 px-4",
                          )
        input1.on(event_type="input", func=cls.get_def)
        # for button event_type = "click"
        # each time, when input1 is working, function doest too
        return wp

    @staticmethod
    def get_def(widget, msg):
        d = Definition(term=widget.value)
        widget.output.text = ";".join(d.get())
