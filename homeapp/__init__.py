#!/usr/bin/python
import os
from flask import Flask

cwd = os.path.dirname(os.path.realpath(__file__))
print cwd

app = Flask(__name__)
app.config['DEBUG'] = True

from homeapp.views import *
from homeapp.pwgen.views import *
from homeapp.music.views import *

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
