from xml.dom.minidom import TypeInfo
import scratchconnect
from mypass import my_pass
import time
import os
user = scratchconnect.ScratchConnect("applejuice_alt", my_pass)
project = user.connect_project(project_id=677519831)
variables = project.connect_cloud_variables()
print(variables.get_cloud_variable_value("user", limit=2)[0])


def decode_username(username):
    print(type(username))
    chars = ["", "", "", "", "", "", "", "", "", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "~", "`", "|", "\\", "/", "", ".", "<", ">", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    decoded = ""
    i = 1
    for x in range(len(username)):
        decoded = decoded + chars[(username[i] + username[i + 1]) + 1]
        i += 2
print(decode_username(variables.get_cloud_variable_value("user", limit=2)[0]))


while True:
    buffer_name = variables.get_cloud_variable_value("cloud", limit=2)
    buffer_contents = variables.get_cloud_variable_value("clou2", limit=2)
    buffer_sender = variables.get_cloud_variable_value("user", limit=2)

    if buffer_name == []:
        buffer_name = ""
    else:
        buffer_name = variables.get_cloud_variable_value("cloud", limit=2)[0]
    if buffer_contents == []:
        buffer_contents = ""
    else:
        buffer_contents = variables.get_cloud_variable_value("clou2", limit=2)[0]
    if buffer_sender == []:
        buffer_sender = ""
    else:
        buffer_sender = variables.get_cloud_variable_value("user", limit=2)[0]
    if buffer_name != " " and buffer_contents != "" and buffer_sender != "":
        variables.set_cloud_variable("cloud", "")
        variables.set_cloud_variable("clou2", "")
        variables.set_cloud_variable("user", "")
        try:
            os.mkdir(str(buffer_sender))
        except:
            pass
        file = open(str(buffer_sender) + str(buffer_name), 'w')
        file.write(str(buffer_contents))
        
