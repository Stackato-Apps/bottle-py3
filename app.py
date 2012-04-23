import os
import sys
from bottle import route, run

@route('/')
def index():
    pyver = '.'.join(map(str, tuple(sys.version_info)[:3]))
    return 'Hello World! (from <b>Python %s</b>)' % (pyver,)


if __name__ == '__main__':
    port = int(os.getenv('PORT', '8000'))
    run(host='0.0.0.0', port=port)

