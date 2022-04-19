import scratchconnect
from mypass import my_pass
import time
import os

user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677519831)
variables = project.connect_cloud_variables()
variables.get_variable_data(limit=100, offset=0)
while True:
    if os.path.isdir("./" + variables.client_username) == True:
        pass
    else:
        os.mkdir("./" + variables.client_username)