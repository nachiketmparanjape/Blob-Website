from flask import Flask

app = Flask(__name__) # '__main__'

@app.route('/')
def hello_method():
    #return ("Hello, world!")
    i = input("Type Something - ")
    return(i)

if __name__ == '__main__':
    app.run(port=5000)

