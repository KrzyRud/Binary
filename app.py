from crypt import methods
from flask import Flask, render_template, request, redirect

app = Flask(__name__)  # Flask standard line


@app.route("/", methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        
        nn=8
        aa = []

        bb1=request.args.get("0", 0)
        bb2=request.args.get("1", 0)
        bb3=request.args.get("2", 0)
        bb4=request.args.get("3", 0)
        bb5=request.args.get("4", 0)
        bb6=request.args.get("5", 0)
        bb7=request.args.get("6", 0)
        bb8=request.args.get("7", 0)

        bbs=[bb1, bb2, bb3, bb4, bb5, bb6, bb7, bb8]
        binaryNumber=[]
        wynik=0

        for i in bbs:
            if i == "nill":
                continue
            else:
                binaryNumber.append(i)

        binaryNumber.reverse()

        for n in range(0, int(nn)):
            a = int(int(binaryNumber[n])*(2**n))
            aa.append(a)
            wynik = wynik + int(a)
            
        return render_template("index.html", binaryNumber=binaryNumber, wynik=wynik, aa=aa)
    else:
        return render_template("index.html")
    


    
    
    
    
   