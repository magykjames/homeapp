from homeapp import app
from homeapp.pwgen.helpers import genrandom
from flask import render_template, request


@app.route('/pwgen', methods=['GET', 'POST'])
def pwgen():
    pwd = None
    length = 8
    defchecked = False
    if request.method == 'GET':
        defchecked = True
    upperletters = True if request.form.get('upperletters') else defchecked
    lowerletters = True if request.form.get('lowerletters') else defchecked
    numbers = True if request.form.get('numbers') else defchecked
    special = True if request.form.get('special') else defchecked
    safe = True if request.form.get('safespecial') else defchecked
    print upperletters, lowerletters, numbers, special
    summary = ('Passwords are guaranteed to have at least one uppercase, ' +
               'one lowercase, a number, and a special character. We will ' +
               'also repeat characters as rarely as possible. Minimum ' +
               'password length: 8 characters.')
    if request.method == 'POST':
        length = request.form['length']
        if length:
            length = int(length)
            if length < 6:
                length = 6
            pwd, summary = genrandom(
                length, upperletters, lowerletters, numbers, special, safe)
    return render_template('pwgen.html',
                           pwd=pwd,
                           summary=summary,
                           length=length,
                           upperletters=upperletters,
                           lowerletters=lowerletters,
                           numbers=numbers,
                           special=special,
                           safe=safe)
