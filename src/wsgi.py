from waitress import serve      #? Handles running flask app, just like unicorn.
from uafxml import web_app      #? Import main directory from root.

#? Entry point
if __name__ == '__main__':
    serve(
        web_app,
        host='127.0.0.1',
        port=5002,
        threads=2
    )
