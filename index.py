from django.db import connection
from requests import session
from scratchclient import ScratchSession
from mypass import my_pass
session = ScratchSession("applejuice_alt", my_pass)
connection = session.create_cloud_connection(677505040)
connection.set_cloud_variable("my variable", 5000)