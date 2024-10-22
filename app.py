from flask import Flask,render_template,request

app=Flask(__name__)

@app.route('/')
@app.route('/register')
def homepage():
    return render_template('register.html')

@app.route("/confrm",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n=request.form.get('Name')
        a = request.form.get('Email')
        c = request.form.get('Age')
        return render_template('confrm.html',Name=n,Email=a,Age=c)

if __name__=="__main__":
    app.run(debug=True)
