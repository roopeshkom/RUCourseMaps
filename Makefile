MESSAGE = "adds a makeifle to auto-push to git"

build:
	git add *
	git commit -m $(MESSAGE)
	git pull origin master
	git push origin master
