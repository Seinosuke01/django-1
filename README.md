# 稗田さんが作ってくれたレポジトリをクローンする
`git clone https://github.com/naoyahieda/django-baby.git`

# django-baby に移動
`cd django-baby`
# プロジェクトを作成する
`docker compose run --rm web django-admin startproject config .`
# アプリを１つ作成する(ここではtodoアプリ)
`docker compose run --rm web python manage.py startapp todo`
# 起動する
`docker compose up`

# rest_framework, cors_headersのinstall
`pip install djangorestrestframework`
`pip install django-cors-headers`

# settings.pyの編集
・Language_codeをjaにする
・Time_zoneをAsia/Tokyoにする
・INSTALLED_APPSにrest＿framework, corsheadersを追加
・MIDDLEWAREにcorsheaders.middleware.CorsMiddlewareを追加
・CORS_ORIGIN_ALLOW_ALL = Trueを追加

# requirements.txtの編集
djangorestframework
django-cors-headers
と書く
`docker compose up --build`

# models.pyを変更した後
`python manage.py makemigrations todo`
`python manage.py migrate`

# admin画面の管理者登録
`python manage.py createsuperuser`


