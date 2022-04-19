import scratchconnect
from mypass import my_pass
import time
import os

user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677519831)
variables = project.connect_cloud_variables()
while True:
    print(variables.client_username)
    if os.path.isdir("./" + variables.client_username) == True:
        pass
    else:
        os.mkdir("./" + variables.client_username)
        time.sleep(0.5)
    while variables.get_cloud_variable_value(variable_name="clou2")[0] == "0" or variables.get_cloud_variable_value(variable_name="clou2")[0] == 0:
        continue
    file = open("./" + variables.client_username + "/" + str(variables.get_cloud_variable_value(variable_name="cloud")[0]), 'w')
    print(str(variables.get_cloud_variable_value(variable_name="clou2")[0]))
    file.write(str(variables.get_cloud_variable_value(variable_name="clou2")[0]))
    variables.set_cloud_variable(variable_name="cloud", value=0)
    time.sleep(0.2)
    variables.set_cloud_variable(variable_name="clou2", value=0)
    time.sleep(0.8)