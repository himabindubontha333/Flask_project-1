from flask import Flask
FAI=Flask(__name__)

@FAI.route('/wish')

def wish():
    return 'Hello my dear soul'

FAI.run(debug=True)