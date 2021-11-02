import justpy as jp
from examples.layout import DefaultLayout
from examples.page import Page


class Home(Page):
    path = "/"

    @classmethod
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)
        lay = DefaultLayout(a=wp)
        container = jp.QPageContainer(a=lay)
        div = jp.Div(a=container, classes="bg-gray-200 h-screen")
        jp.Div(a=div, text="This is the Home Page!", classes="text-4xl m-2")
        jp.Div(a=div, text="""
                Quasar’s motto is: write code once and simultaneously deploy it as a website, a Mobile App and/or an Electron App.
                Yes, one codebase for all of them, helping you develop an app in record time by using a state-of-the-art CLI and backed by best-practice, 
                blazing fast Quasar web components.
                When using Quasar, you won’t need additional heavy libraries like Hammer.js, Moment.js or Bootstrap. 
                It’s got those needs covered internally, and all with a small footprint! 
                """, classes="text-lg p-2")

        return wp
