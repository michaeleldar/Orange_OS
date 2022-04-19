import scratchconnect
from mypass import my_pass
import time
import os

user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677519831)
variables = project.connect_cloud_variables()
print(variables.get_cloud_variable_value("cloud", limit=2))


while True:
    buffer_name = variables.get_cloud_variable_value("cloud", limit=2)
    buffer_contents = variables.get_cloud_variable_value("clou2", limit=2)
    buffer_sender = variables.get_cloud_variable_value("user", limit=2)
    if buffer_name != "" and buffer_contents != "" and buffer_sender != "":
        variables.set_cloud_variable("cloud", "")
        variables.set_cloud_variable("clou2", "")
        variables.set_cloud_variable("user", "")
        
