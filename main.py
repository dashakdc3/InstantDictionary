import justpy as jp
from examples.home import Home
from examples.about import About
from examples.dictionary1 import Dictionary
# you can also try examples.dictionary

# it needs 2 parameters: path, and a function, that creates page
jp.Route(path=Home.path, func_to_run=Home.serve)
jp.Route(path=Dictionary.path, func_to_run=Dictionary.serve)
jp.Route(path=About.path, func_to_run=About.serve)

jp.justpy(port=8001)
# port-optional
