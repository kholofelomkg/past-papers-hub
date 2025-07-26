from app import app
from flask import render_template
import os

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/home/lifescience')
def lifescience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Life Science")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('lifescience.html',items=files)

@app.route('/home/mathematics')
def mathematics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Mathematics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('mathematics.html',items=files)

@app.route('/home/geography')
def geography():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Geography")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Geography.html',items=files)

@app.route('/home/accounting')
def accounting():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Accounting")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Accounting.html',items=files)

@app.route('/home/cat')
def cat():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "CAT")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('CAT.html',items=files)

@app.route('/home/physicalscience')
def physicalscience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Physical Science")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Physical Science.html',items=files)

@app.route('/home/history')
def history():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "History")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('History.html',items=files)

@app.route('/home/mathematicalliteracy')
def mathematicalliteracy():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Mathematical Literacy")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('MathematicalLiteracy.html',items=files)


@app.route('/home/technicalmath')
def technicalmath():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Technical Math")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Technical Math.html',items=files)

@app.route('/home/technicalscience')
def technicalscience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Technical Science")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Technical Science.html',items=files)

@app.route('/home/tourism')
def tourism():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Tourism")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Tourism.html',items=files)

@app.route('/home/lifeorientation')
def lifeorientation():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Life Orientation")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Life Orientation.html',items=files)

@app.route('/home/egd')
def egd():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "EGD")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('EGD.html',items=files)

@app.route('/home/economics')
def economics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "Economics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Economics.html',items=files)

@app.route('/home/electronics')
def electrics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "electrics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('Electrics.html',items=files)