from flask import Flask, request, Response


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
    if xfw == "":
        xfw = request.environ.get('HTTP_X_FORWARDED_FOR')
        if xfw == "":
            xfw = request.remote_addr
    return xfw


# -- Main function
if __name__ == '__main__':
    # Run Flask
    app.run(debug=True, host='0.0.0.0', port=int("5000"))
