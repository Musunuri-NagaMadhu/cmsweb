from os import environ
from FlaskWebProject import app

if __name__ == '__main__':
    # Default to 0.0.0.0 so Azure can bind correctly
    host = environ.get('SERVER_HOST', '0.0.0.0')
    try:
        port = int(environ.get('PORT', 5555))  # Azure uses PORT
    except ValueError:
        port = 5555

    # Use SSL only in local dev if you really need HTTPS testing
    use_ssl = environ.get('USE_SSL', 'false').lower() == 'true'
    if use_ssl:
        app.run(host=host, port=port, ssl_context='adhoc', debug=True)
    else:
        app.run(host=host, port=port, debug=True)

