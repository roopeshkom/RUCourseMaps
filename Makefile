m = "adds a makefile to auto-push to git"

build:
	git add *
	git commit -m $(m)
	git pull origin master
	git push origin master
