from flask import Flask

app = Flask('test')

@app.route('/dualipa', methods=['GET'])
def dualipa():
    return 'Dua is the Lipa'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9696)