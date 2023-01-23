from bottle import route, run, template
from dep import sum


@route('/add/<a>/<b>')
def index(a, b):
    return template('<p>{ \'result\': {{res}} }</p>', res=sum(a, b))


run(host='localhost', port=8080, reloader=True)
