from flask import Flask, render_template, request, redirect

app = Flask(__name__)
print(__name__)


@app.route('/<string:page>')
def html_page(page =None):
    return render_template(page )


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('thankyou.html')
    else:
        return 'wrong'


def write_to_file(data):
    # with open('database.txt', 'a') as database:
    #     email = data['email']
    #     subject = data['subject']
    #     message = data['message']
    #     print(f'\n{email},{subject}{message}')
    #     file = database.write(f'{email},{subject},{message}')
    with open('data.txt', 'a+') as file:
        print(f'\n a2')
        file.write('Appended text\n')
