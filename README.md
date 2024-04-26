# Python

Web Server in Python Using Flask

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
mkdir myproject
cd myproject
py -3 -m venv venv
venv\Scripts\activate
pip install Flask
```

## Run Server

```bash
C:\path\to\app>set FLASK_APP=hello.py

flask run --debug
```

## Usage

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
