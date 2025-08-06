from app import app
from flask import render_template
import os

@app.route('/')
@app.route('/home')
def index():
    return render_template('index.html')

@app.route('/home/lifescience')
def lifescience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "lifescience")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('lifescience.html',items=files)

@app.route('/home/mathematics')
def mathematics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "mathematics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('mathematics.html',items=files)

@app.route('/home/geography')
def geography():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "geography")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('geography.html',items=files)

@app.route('/home/accounting')
def accounting():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "accounting")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('accounting.html',items=files)

@app.route('/home/cat')
def cat():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "cat")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('cat.html',items=files)

@app.route('/home/physicalscience')
def physicalscience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "physicalscience")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('physicalscience.html',items=files)

@app.route('/home/history')
def history():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "history")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('history.html',items=files)

@app.route('/home/mathematicalliteracy')
def mathematicalliteracy():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "mathematicalliteracy")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('mathematicalliteracy.html',items=files)


@app.route('/home/technicalmath')
def technicalmath():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "technicalmath")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('technicalmath.html',items=files)

@app.route('/home/technicalscience')
def technicalscience():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "technicalscience")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('technicalscience.html',items=files)

@app.route('/home/tourism')
def tourism():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "tourism")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('tourism.html',items=files)

@app.route('/home/lifeorientation')
def lifeorientation():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "lifeorientation")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('lifeorientation.html',items=files)

@app.route('/home/egd')
def egd():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "egd")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('egd.html',items=files)

@app.route('/home/economics')
def economics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "eeconomics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('economics.html',items=files)

@app.route('/home/electronics')
def electronics():
    directory_path = os.path.join(os.getcwd(),"app","static", "papers", "electronics")
    contents = os.listdir(directory_path)
    files = [item for item in contents if os.path.isfile(os.path.join(directory_path, item))]
    return render_template('electronics.html',items=files)