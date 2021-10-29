from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
from urllib import parse
import json
import mysql.connector
from mysql.connector import Error

class crud:
    def __init__(self):
        print("Iniciando conexion con la base de datos...")
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="db_academica_a2"
        )
        if self.db.is_connected():
            print("Conexion establecida")
        else:
            print("Conexion fallida")

class servidorBasico(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            self.path = "/index.html"
        return SimpleHTTPRequestHandler.do_GET(self)

print("Servidor iniciado")
server = HTTPServer(("localhost", 3000), servidorBasico)
server.serve_forever()