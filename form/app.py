from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    form_data = request.form
    print(form_data)  #(JUST TO CHECK IF DATA IS SAVING..TERMINAL THO) Debugging: See the received data in terminal
    return render_template('thank_you.html', name=form_data.get('full_name', 'User'))


if __name__ == '__main__':
    app.run(debug=True)
