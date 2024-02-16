from flask import Flask

FAI=Flask(__name__)

@FAI.route('/stringresponse')
def stringresponse():
    return 'hey guys these is my first flask project'

if __name__=='__main__':
    FAI.run(debug=True)