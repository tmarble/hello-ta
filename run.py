#!/usr/bin/env python3
"Simple Technical Agility Web Server"

import logging
import http.server
import socketserver

class TechnicalAgilityHandler(http.server.SimpleHTTPRequestHandler):
    "Specialized version of the web server"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory='./resources/public')

def main():
    "The main method"

    port = 8000
    Handler = TechnicalAgilityHandler
    with socketserver.TCPServer(("", port), Handler) as httpd:
        msg = f"Starting Technical Agility on {port=}"
        logging.warning(msg)
        httpd.serve_forever()

if __name__ == '__main__':
    main()
