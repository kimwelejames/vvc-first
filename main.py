from flask import Flask, render_template

app = Flask(__name__)
app.debug = True


@app.route('/')
def Index():
    return render_template('Index.html')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
