from flask import Flask, request, jsonify, redirect
import socket
import requests
import base64

app = Flask(__name__)

@app.route('/')
def index():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    x = (s.getsockname()[0])
    s.close()
    return f'''it works {x}
    <form method="POST">
        <input name="url">
        <button>Submit</button>
    </form>
    '''+'''
    <script>
        var url = window.location.href;
        var t = new URL(url);
        if(t.searchParams.get("error")){
            var node = document.createElement("P");
            var text = document.createTextNode(atob(t.searchParams.get("error")));
            node.appendChild(text);
            document.body.appendChild(node);
        }
    </script>
    '''

@app.route('/', methods=['POST'])
def process():
    try:
        url = request.form.get('url')
        url = 'http://'+url if "http" not in url else url
        req = requests.get(url)
    except Exception as e:
        return redirect('/?error='+base64.b64encode(str(e).encode()).decode())
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    x = (s.getsockname()[0])
    s.close()
    return f'''it works {x}
    <form method="POST">
        <input name="url">
        <button>Submit</button>
    </form>
    '''+req.text

if __name__ == "__main__":
    app.run(host="0.0.0.0",port="80")