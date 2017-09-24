from homeapp import app
from homeapp.music.helpers import getmusic
from flask import render_template


@app.route('/music', methods=['GET'])
def music():
    musicfolder = app.static_folder + '/music/'
    musicfiles = getmusic(musicfolder)
    return render_template('music.html', musicfiles=musicfiles)
