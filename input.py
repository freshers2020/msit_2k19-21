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
    return render_template('home.html')

@app.route('/example')
def exam():
    return render_template('example.html')

@app.route('/main', methods=['POST'])
def main():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    return render_template('main.html')



@app.route('/handle_data', methods=['POST', "GET"])
def handle_data():
    projectpath = request.form['projectFilepath']
    print(projectpath)
    return render_template('simple.html',  list_1=list_1, list_2=list_2,val=projectpath)





@app.route('/df_to_html', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html',  tables=[af.to_html(classes='data')], titles=af.columns.values,val=projectpath)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
