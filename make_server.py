from flask import Flask
app = Flask(__name__)

#http://localhost:5000/ 페이지
@app.route('/')
def home():
   return 'This is Home!'

if __name__ == '__main__':
   app.run('0.0.0.0',port=5000,debug=True)



---

#http://localhost:5000/mypage 페이지
@app.route('/mypage')
def mypage():
   return 'This is Mypage!'
