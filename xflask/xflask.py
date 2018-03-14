from flask import Flask
from flask import request

Application = Flask(__name__)
def main():
    Application.run()

@Application.route('/curd', methods=['POST', 'GET'])
def CurdHandler():
    if request.method == 'GET':
        return 'this get handler'
    elif request.method == 'POST':
        return 'this post handler'
    else:
        return 'error'


if __name__ == "__main__":
    main()