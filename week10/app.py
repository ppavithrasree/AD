from flask import Flask, render_template,request,redirect,url_for
app = Flask(__name__)
@app.route('/')
def home():
    return render_template("login.html")
@app.route('/success/<name>')
def success(name):
    return f"Welcome {name}"
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method=='POST':
        user=request.form.get('nm')
        return redirect(url_for('success',name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('success',name=user))
if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1',port=5000)
    