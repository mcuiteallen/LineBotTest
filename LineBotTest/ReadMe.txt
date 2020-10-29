git init
heroku git:remote -a allen-test-bot
heroku config:set DISABLE_COLLECTSTATIC=1
git add .
git commit -am "make it better"
git push heroku master