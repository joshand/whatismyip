from flask import Flask, request, Response
import json


# -- Application Setup
app = Flask(__name__)


# -- Add default route (/) for basic health check
@app.route('/', methods=['GET'])
def return_blank():
    return ""


# -- Add route to GET status for a task
@app.route('/api/v0/whatismyip', methods=['GET'])
def get_ip():
    print("GET /api/v0/whatismyip")

    xfw = request.environ.get('HTTP_X_REAL_IP')
    if not xfw:
        xfw = request.environ.get('HTTP_X_FORWARDED_FOR')
        if not xfw:
            xfw = request.remote_addr

    if not xfw:
        xfw = ""

    return xfw


# -- Add route to GET status for a task
@app.route('/api/v1/whatismyip', methods=['GET'])
def get_ip_v2():
    print("GET /api/v1/whatismyip")

    x_remaddr = request.remote_addr
    x_env = request.environ
    x_env["REMOTE_ADDR"] = x_remaddr
    del x_env["wsgi.input"]
    del x_env["wsgi.errors"]
    del x_env["werkzeug.server.shutdown"]
    del x_env["werkzeug.request"]
    print(x_env)

    return json.dumps(x_env)


# -- Main function
if __name__ == '__main__':
    # Run Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
