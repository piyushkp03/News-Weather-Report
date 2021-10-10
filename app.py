from flask import Flask, render_template,request,url_for
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy
from werkzeug.utils import redirect, send_file
import weather
import news
from datetime import datetime

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///mydb.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)

class Datas(db.Model):
    sno=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(200),nullable=False)
    date=db.Column(db.DateTime, default=datetime.now)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"


@app.route('/detail/<string:data>',methods=['GET','POST'])
def detail(data):
    print("The data returned from the link of the url is:",data)
    return redirect(data)

@app.route('/', methods=['GET','POST'])
def helloworld():
    lnews=[]
    weatherdesc=[]
    city=''
   
    if request.method=='POST':
        city=request.form['newcity']
        weatherdesc=weather.weath(city)
        category=request.form['radioval']
        #print("The category of the news is: ",category)
        tnews=news.thenews('India',category)
        lnews=[[article['title'],article['content'] ,article['url']] for article in tnews]

        #ldesc=[article['title'] for article in desc]
        #print(lnews,desc)

    return  render_template('index.html',city=city,lnews=lnews,weatherdesc=weatherdesc)


        





    """ datas=Datas(title="datas")
    db.session.add(datas)

    db.session.commit() """



    
@app.route('/piyush', methods=['GET','POST'])
def helloworld2():
    """datas1=Datas(title="object1")
    datas2=Datas(title="object2")
    db.session.add(datas1)
    db.session.commit()
    db.session.add(datas2)
    db.session.commit() 
    alldatas1=Datas.query.all()
    print("alldatas1:",alldatas1)
    print("alldatas2:",alldatas1) """

    return 'Hello piyush!'

    


if __name__=="__main__":
    app.run(debug=True)


