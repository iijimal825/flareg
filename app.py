from flask import Flask, render_template, url_for, request, redirect
from models.models import MemberContent
from models.database import db_session
from datetime import datetime


# Flask object の生成
app = Flask(__name__)


# リクエストの最後に、セッションの後片付けをする必要がある
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


# "/"へアクセス時、"/get"へリダイレクト
@app.route("/")
def top():
    return redirect(url_for('get'))


@app.route("/get")
def get():
    '''
    登録ページ
    '''
    return render_template('get.html')


@app.route("/confilm", methods=["POST"])
def confilm():
    '''
    確認ページ
    '''
    name = request.form.get('name')
    email = request.form.get('email')
    birthday = request.form.get('birthday')
    return render_template('confilm.html', name=name, email=email, birthday=birthday)


@app.route("/complete", methods=["POST"])
def complete():
    '''
    完了ページ
    '''
    name = request.form.get('name')
    email = request.form.get('email')
    birthday = datetime.strptime(request.form.get('birthday'), '%Y-%m-%d')
    content = MemberContent(name, email, birthday)
    db_session.add(content)
    db_session.commit()
    return render_template('complete.html')
    

@app.route("/index")
def index():
    '''
    DB閲覧ページ（debug）
    '''
    all_member = MemberContent.query.all()
    return render_template("index.html", dblist=all_member)


# debugありで起動
if __name__ == "__main__":
    app.run(debug=True)
