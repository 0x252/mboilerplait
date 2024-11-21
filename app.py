from flask import Flask, render_template, request, jsonify

def create_app():

    app = Flask(__name__, static_url_path='/static', static_folder='static', template_folder='templates')

    @app.route('/')
    def index():
        return render_template('index.html'), 200

    @app.route('/hello/<who>')
    def who(who):
        return render_template('who.html', who=who), 200

    @app.route('/jsonreceive', methods=['POST'])
    def jsonreceive():
        data = request.json
        return jsonify({"data": data}), 200

    @app.route('/jsonreceive', methods=['GET'])
    def jsongive():
        return jsonify({"data": []})

    return app
