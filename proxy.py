from flask import Flask, request, redirect, Response
import requests

app = Flask(__name__)
proxy_url = 'http://10.122.251.51:2019/'

@app.route('/<path:path>', methods=['GET'])
def proxy(path):
    """proxy - returns a proxy to another server behind the firewall"""
    if request.method == 'GET':
        url = f'{proxy_url}{path}'
        resp = requests.get(url)
        excluded_headers = ['content-encoding', 'content-length', 'transfer-encoding', 'connection']
        headers = [(name, value) for (name, value) in resp.raw.headers.items() if name.lower() not in excluded_headers]
        response = Response(resp.content, resp.status_code, headers)
    return response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
