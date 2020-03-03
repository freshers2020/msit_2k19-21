import pandas as pd
from flask import Flask, Markup, render_template, request


app = Flask(__name__)
projectpath=""
af = pd.read_excel('Junior Deatails.xlsx')

print(af)
list_1=af['Roll No']
list_2=af['Name']

@app.route('/')
def home():
    return render_template('initial.html')






@app.route('/handle_data', methods=['POST', "GET"])
def handle_data():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    return render_template('invitationpage.html',  list_1=list_1, list_2=list_2,val=projectpath)






if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
