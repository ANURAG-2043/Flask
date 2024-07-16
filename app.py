from flask import Flask,render_template, request, redirect ,url_for,jsonify

app=Flask(__name__)  #entry point of the program

#url flask app routing
@app.route("/",methods=["GET"])
def welcome():
    return "<h1>welcome to the home page.</h1>"

@app.route("/index",methods=["GET"])
def index():
    return "<h4>welcome to the index page.</h4>"

#variable rule parameters are passed here
@app.route("/success/<int:score>")
def success(score):
    return "success! score:" +str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "fail! score:" +str(score)


@app.route('/form', methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        english=float(request.form["english"])
        
        avg_marks= (maths+science+english)/3
        
       # return render_template('form.html',score=avg_marks)

        res=""
        if avg_marks>=50:
            res="success"
        else:
            res="fail"

        return redirect(url_for(res,score = avg_marks))


@app.route('/api',methods=['POST'])
def calculate_sum():
    data=request.get_json()         #json format ko dictioinary mein convert karenge
    a_val=float(dict(data)['a'])    #string value ko float mein convert kiya
    b_val=float(dict(data)['b']) 

    return jsonify(a_val+b_val)


if __name__ == '__main__':  #entry point
    app.run(debug= True)



