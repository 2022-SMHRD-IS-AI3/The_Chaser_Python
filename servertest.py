# !pip install Flask
from flask import Flask
app = Flask(__name__)
@app.route('/')
def home() :
    return 'Hello, World'

if __name__ == '__main__':
    app.run()


# !pip install cx_Oracle --upgrade
# !pip install oracledb --upgrade
import cx_Oracle as cx
conn = cx.connect("campus_c_230531_3","smhrd3","project-db-stu.smhrd.com:1524/XE",encoding="UTF-8")
    