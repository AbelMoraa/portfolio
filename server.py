from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)
print(__name__)

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n{email}, {subject}, {message}')
    return None

def write_to_csv(data):
    with open('database.csv', mode='a', newline='') as database2:
        writer = csv.writer(database2, delimiter=',')
        email = data['email']
        subject = data['subject']
        message = data['message']
        writer.writerow([email, subject, message])
    return None

@app.route('/summit_form', methods=['POST', 'GET'])
def summit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('thanks.html')
        except:
            return 'Did not save to database'
    else:
        return 'something went wrong'