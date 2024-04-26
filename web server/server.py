from flask import Flask, render_template

app = Flask(__name__)
print(__name__)


@app.route('/<string:page>')
def html_page(page =None):
    return render_template(page )





