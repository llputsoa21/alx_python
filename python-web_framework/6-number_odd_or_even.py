'''script that creates web application using flask'''

    
'''importing flask'''
from flask import Flask, render_template

'''creates the variable application name'''
app = Flask(__name__)

'''retrieving route response'''
@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'

'''retrieving route response'''
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

'''retrieving route response'''
@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    return 'C ' + text.replace('_', ' ')

'''retrieving route response'''
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def python_text(text='is cool'):
    return 'Python ' + text.replace('_', ' ')

'''retrieving route response'''
@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return '{} is a number'.format(n)
    if not n:
        return 404

'''retrieving route response'''   
@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    return render_template('5-number.html', n=n)

'''retrieving route response'''
@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_template(n):
    '''checks if n is perfectly divisible by 2'''
    
    if n % 2 == 0:
        return render_template('6-number_odd_or_even.html', n=n, x='even')
    else:
        return render_template('6-number_odd_or_even.html', n=n, x='odd')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)