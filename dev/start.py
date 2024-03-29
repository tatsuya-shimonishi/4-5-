from bottle import route, run, template, request
import question as qs
import random_question as rdqs
import answer as ans
import advice as adv

#ホーム画面
@route("/home")
def home():
    return template("home_temp")

#質問画面（順次）
@route("/question")
def question():
    disp_no = 0
    return qs.getQsTemp(disp_no)

#質問画面（順次）※「前の質問」ボタン押下時
@route("/question_back", method="POST")
def do_question():
    disp_no = request.forms.no
    disp_no = int(disp_no)-2
    return qs.getQsTemp(disp_no)

#質問画面（順次）※「次の質問」ボタン押下時
@route("/question_next", method="POST")
def do_question():
    disp_no = request.forms.no
    return qs.getQsTemp(disp_no)

#質問画面（ランダム）
@route("/random")
def randomQuestion():
    return rdqs.getRdTemp()

#質問画面（ランダム）※アドバイス画面からの遷移
@route("/random_advice", method="POST")
def randomQuestion():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return rdqs.getRdAdTemp(disp_no)

#質問画面　※「質問に戻る」ボタン押下時
@route("/question_return", method="POST")
def do_question():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return qs.getQsTemp(disp_no)

#回答画面
@route("/answer", method="POST")
def answer():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return ans.getAnTemp(disp_no)

#回答画面　※ランダム画面からの遷移
@route("/answer_random", method="POST")
def answer():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return ans.getAnRdTemp(disp_no)

#アドバイス画面
@route("/advice", method="POST")
def advice():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return adv.getAdTemp(disp_no)

#アドバイス画面　※ランダム画面からの遷移
@route("/advice_random", method="POST")
def advice():
    disp_no = request.forms.no
    disp_no = int(disp_no)-1
    return adv.getAdRdTemp(disp_no)

#質問内容の登録（画面入力）画面
@route("/input")
def input():
    return "質問内容の登録（画面入力）画面"

#質問内容の登録（Excelアップロード）画面
@route("/upload")
def home():
    return "質問内容の登録（Excelアップロード）画面"

#質問一覧画面
@route("/list")
def home():
    return "質問一覧画面"

run(host="localhost", port=8080, debug=True)
