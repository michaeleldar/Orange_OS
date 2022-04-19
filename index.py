from django.db import connection
from requests import session
from scratchclient import ScratchSession
from mypass import my_pass
import time
session = ScratchSession("applejuice_alt", my_pass)
connection = session.create_cloud_connection(677505040)
time.sleep(5)
connection.set_cloud_variable("my variable", 5000)