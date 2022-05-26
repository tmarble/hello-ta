#!/usr/bin/env python3

import os
import logging
import http.server
import socketserver

PORT = 8000

class TechnicalAgilityHandler(http.server.SimpleHTTPRequestHandler):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='./resources/public')

Handler = TechnicalAgilityHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    logging.warning("Starting Technical Agility on port %d" % PORT)
    httpd.serve_forever()

    
