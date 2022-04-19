import scratchconnect
from mypass import my_pass
import time
import os

user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677519831)
variables = project.connect_cloud_variables()


while True:
    buffer_name = print(variables.get_cloud_variable_value("cloud", limit=2))
    buffer_contents = print(variables.get_cloud_variable_value("clou2", limit=2))
    if buffer_name != "" and buffer_contents != "":