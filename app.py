import os
import sys
from bottle import route, run

@route('/')
def index():
    pyver = '.'.join(map(str, tuple(sys.version_info)[:3]))
    return 'Hello World! (from <b>Python %s</b>)' % (pyver,)


if __name__ == '__main__':
    port = int(os.getenv('VCAP_APP_PORT', '8000'))
    host = os.getenv('VCAP_APP_HOST', '0.0.0.0')
    run(host=host, port=port)

