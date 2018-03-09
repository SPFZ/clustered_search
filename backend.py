from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/search", methods=['GET'])
def hello():
    search_string = request.args.get('search_string', '')
    print('Backend received search request: '+ search_string)
    result = do_search(search_string)
    return jsonify(result)

def do_search(search_string):
    result = {
        'search_string' : search_string,
        'results' : ['asdasd', 'Asdasd']
    }
    return result

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5001)