import re
from app import app
from flask import render_template, redirect, url_for, flash, request
app.secret_key = "SEGREDO!!!!!!!!!!!!!!!!!!"

@app.route('/')
@app.route('/entrada')
def entrada():
    return render_template("entrada.html")

@app.route('/regex', methods = ['POST', 'GET'])
def regex():
    if request.method == "POST":
        #region REGEX
        email = request.form['email']
        password = request.form['password']
        regexemail = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        regexpassword = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"

        if re.match(regexemail, email):
            if re.match(regexpassword, password):
                flash("Email e passoword aceites")
                return render_template("regex.html")
            else:
                flash("Password tem que ter no minimo 8 caracteres e pelo menos uma letra e um numero.")
                return render_template("regex.html")
        else:
            flash('Email nao foi aceite')
            return render_template("regex.html")
        #endregion
    else:
        return render_template("regex.html")

@app.route('/automatofin', methods = ['POST', 'GET'])
def automatofin():
    if request.method == "POST":
        #region AUTOMATO
        comb = request.form['comb']

        estadof = {"d"}
        aceitavel={"0","1"}
        estadoi = "a"
        automato={ 
                    ("a","0"):"e",("a","1"):"b",
                    ("b","0"):"f",("b","1"):"c",
                    ("c","0"):"g",("c","1"):"d",
                    ("d","0"):"h",("d","1"):"b",
                    ("e","0"):"a",("e","1"):"f",
                    ("f","0"):"b",("f","1"):"g",
                    ("g","0"):"c",("g","1"):"h",
                    ("h","0"):"d",("h","1"):"f",
                }

        #while True :
        seq=comb

        estadoatual = estadoi

        for i in seq:
            if (i not in aceitavel):
                flash("ERRO, insira apenas 0's e 1's")
                return render_template("automatofin.html")

            estadoatual = automato[(estadoatual,i)]
        if(estadoatual not in estadof):
            flash('Sequencia não aceite')
            return render_template("automatofin.html")
        else:
            flash("Sequencia aceite!")
            return render_template("automatofin.html")
        #endregion
    else:
        return render_template("automatofin.html")

@app.route('/automatopilha',  methods = ['POST', 'GET'])
def automatopilha():
    if request.method == "POST":
        #region AUTOMATO COM PILHA
        stack = []
        stack.append('$')
        num = request.form['comb']

        for i in num:
            if i == "0":
                stack.append(i)
                stack.append(i)
            elif i == "1" and stack == ["$"]:
                stack.append(i)
                break
            elif i == "1" and stack != ["$"]:
                stack.pop()
            else:
                stack.append(i)
            
        
        if stack == ["$"]:
            flash("Codigo aceite")
            return render_template("automatopilha.html")
        else:
            flash("codigo nao aceite")
            return render_template("automatopilha.html")
            
        #endregion
    else:
        return render_template("automatopilha.html")
