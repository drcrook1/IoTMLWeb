'''
Author: David Crook
Copyright: Microsoft Corporation 2018
'''
from app import create_app

app = create_app()

app.run(host='0.0.0.0', port=80)
