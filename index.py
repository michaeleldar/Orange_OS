import scratchconnect
from mypass import my_pass
import time

user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677505040)
variables = project.connect_cloud_variables()
variables.get_variable_data(limit=100, offset=0)

if variables.get_cloud_variable_value(variable_name="my variable", limit=1000)[0] == 0:
    print("message from scratch")
    time.sleep(5)
    variables.set_cloud_variable(variable_name="my variable", value=1)