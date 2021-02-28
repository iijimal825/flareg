from flask import Flask, render_template, url_for, request, redirect, session, flash
from models.models import MemberContent
from models.database import db_session
import datetime


# Flask object の生成
app = Flask(__name__)
# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'\x88{{\x81-@\xbb\x072\x8f#\xb6\xf1*\xd5\xb7'

# リクエストの最後に、セッションの後片付けをする必要がある
@app.teardown_request
def shutdown_session(exception=None):
    db_session.remove()


# "/"へアクセス時、"/get"へリダイレクト
@app.route("/")
def top():          
    return redirect(url_for('get'))


@app.route("/get", methods=['GET', 'POST'])
def get():
    '''
    登録ページ
    '''
    if request.method == "GET":
        today = datetime.date.today()
        return render_template('get.html', today=today)
    else:
        session['name'] = request.form.get('name')
        session['email'] = request.form.get('email')
        session['birthday'] = request.form.get('birthday')
        return redirect(url_for('confilm'))


@app.route("/confilm", methods=['GET', 'POST'])
def confilm():
    '''
    確認ページ
    '''
    if request.method == "GET":
        return render_template('confilm.html', session=session)
    else:
        # name が unique かチェック
        name = session.get('name')
        member_name = MemberContent.query.filter_by(name=name).first()
        if member_name:
            return redirect(url_for('complete', status='user_notunique'))
        # email が unique かチェック
        email = session.get('email')
        member_email = MemberContent.query.filter_by(email=email).first()
        if member_email:
            return redirect(url_for('complete', status='email_notunique'))
        # birthdayの取得
        birthday = datetime.datetime.strptime(session.get('birthday'), '%Y-%m-%d')
        # DBへ登録
        try:
            content = MemberContent(name, email, birthday)
            db_session.add(content)
            db_session.commit()
            return redirect(url_for('complete', status='success'))
        except Exception as e:
            return redirect(url_for('complete', status='dbcommit_failed'))



@app.route("/complete")
def complete():
    '''
    完了ページ
    '''
    status = request.args.get('status')
    session.clear()
    return render_template('complete.html', status=status)
    

@app.route("/index")
def index():
    '''
    DB閲覧ページ（debug）
    '''
    # Seesionを使ってるように見えないが内部的に使っている
    all_member = MemberContent.query.all()
    return render_template("index.html", dblist=all_member)


# debugありで起動
if __name__ == "__main__":
    app.run(debug=True)
