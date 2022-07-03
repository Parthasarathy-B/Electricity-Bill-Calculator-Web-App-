from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/result",methods = ['POST','GET'])
def result():
    output = request.form.to_dict()
    name = output["name"]
    n=name
    n=int(n)
    if (n<=100):
        f=0
    
    elif (n>100 and n<=200):
        f=((n-100)*1.50)+20
    
    elif (n>200 and n<=500):
        f=((n-200)*3)+230
        
    else:
        f=((n-500)*6.60)+1780
    
    f=int(f)
    if(f<1):
        f='0'
    return render_template("index.html",name = f)

if __name__ == '__main__':
    app.run(debug=True,port=5001)
