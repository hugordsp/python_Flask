# coding: utf-8
import os
os.system('cls')

from flask import Flask, render_template
app = Flask("projeto")

@app.route ("/")
def ola_mundo ():
    nome= "Hugo Rodrigues"
    return render_template("alo.html", n=nome), 200

app.run()