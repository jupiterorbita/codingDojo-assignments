from flask import Flask, session, redirect, render_template
app=Flask(__name__)
app.secret_key="9824hfiuwenfiwenfoe"
print('\n','= = = starting server = = =')

@app.route('/')
def index():
    print('-=-=--=-=-=-= in index =-=-=-=-=-=- ')
    return render_template('index.html')

@app.route('/process', methods=['post'])
def process():
    print('\n','-=-=--=- in /process -=-=-=-=-=')
    print('@ @ @ got form info', request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)