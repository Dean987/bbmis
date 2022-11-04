import firebase_admin
from firebase_admin import credentials, firestore
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def index():
    homepage = "<h1>陳俊祥的選單網頁</h1>"
    homepage += "<a href=/I>關於俊祥</a><br>"
    homepage += "<a href=/L>應徵的公司資訊</a><br>"
    homepage += "<a href=/O>履歷</a><br>"
    homepage += "<br><a href=/read>讀取Firestore資料</a><br>"
    return homepage


@app.route("/I")
def aboutme():
 return render_template("aboutme.html")

@app.route("/L")
def company():
 return render_template("company.html")

@app.route("/O")
def test():
 return render_template("test.html") 


@app.route("/read")
def read():
    Result = ""     
    collection_ref = db.collection("1111")    
    docs = collection_ref.order_by("mail", direction=firestore.Query.DESCENDING).get()    
    for doc in docs:         
        Result += "文件內容：{}".format(doc.to_dict()) + "<br>"    
    return Result


#if __name__ == "__main__":
    #app.run()
