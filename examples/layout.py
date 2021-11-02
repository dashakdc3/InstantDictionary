import justpy as jp


class DefaultLayout(jp.QLayout):
    def __init__(self, view="hHh lpR fFf", **kwargs):
        super().__init__(view=view, **kwargs)
        # =jp.QLayout.__init__(**kwargs) по смыслу равны
        # in this case we need __init__,
        # because later we will need to initilise this class in home/dictionary/about(like clients of DefaultLayout) classes.
        # view=view. View 1 from __init__ and it is equal to View 2 from first __init__
        header = jp.QHeader(a=self, classes="bg-primary text-white")
        toolbar = jp.QToolbar(a=header)
        drawer = jp.QDrawer(a=self, show_if_above=True,
                            v_model="leftDrawerOpen", side="left", bordered=True)
        scrollarea = jp.QScrollArea(
            a=drawer, classes="fit")
        qlist = jp.QList(a=scrollarea)
        a_classes = "p-2 m-2  font-serif text-lg text-blue-400 hover:text-blue-700"
        jp.A(a=qlist, text="Home", href="/", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="Dictionary", href="/dictionary", classes=a_classes)
        jp.Br(a=qlist)
        jp.A(a=qlist, text="About", href="/about", classes=a_classes)
        button = jp.QBtn(a=toolbar, dense=True, flat=True, round=True,
                         icon="menu", click=self.move_drower, drawer1=drawer)
        jp.QToolbarTitle(a=toolbar, text="Instatnt Dictionary")

    @staticmethod
    def move_drower(widget, msg):
        if widget.drawer1.value:
            widget.drawer1.value = False
        else:
            widget.drawer1.value = True
