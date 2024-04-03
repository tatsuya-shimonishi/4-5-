<html>
    <head>
        <link rel="stylesheet" type="text/css" href="/static/css/style.css">
    </head>
    <body>
        <h1>質問 No.{{output_no}}</h1>
        <div>
            <p>{{output_question}}</p>
        </div>
        <div class="button-container">
            <form method="post" action="/advice_random">
                <button type="submit" name="no" value="{{output_no}}">アドバイス</button>
            </form>
            <form method="post" action="/answer_random">
                <button type="submit" name="no" value="{{output_no}}">自己回答</button>
            </form>
            <button onclick="location.href='random'">次の質問</button>
        </div>
        <div>
            <a href="home">ホーム画面へ</a>
        </div>
    </body>
</html>