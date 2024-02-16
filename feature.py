from flask import Flask

FAI = Flask(__name__)

@FAI.route('/stringResponse')
def stringResponse():
    return 'This is first string response'

@FAI.route('/SecondstringResponse')
def secondStringResponse():
    return 'This is second string response'


if __name__ =='__main__':
    FAI.run(debug=True)


