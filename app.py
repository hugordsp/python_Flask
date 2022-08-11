# coding: utf-8
import os
os.system('cls')

from flask import Flask
app = Flask("projeto")

@app.route ("/")
def ola_mundo ():
    return "Olá mundo! Esse é meu primeiro projeto Flask!!", 200

app.run()