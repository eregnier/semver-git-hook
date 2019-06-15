.PHONY: build push clean deploy

build-standalone:
	nuitka3 --standalone --recurse-all semver_git_hook.py
	@echo "\t + Build completed, check semver_git_hook.dist for portable executable."

build:
	pipenv run python setup.py sdist
	pipenv run python setup.py bdist_wheel

push: build
	pipenv run twine upload dist/*

clean:
	rm -rf build dist q.egg-info
	find -name *.pyc -delete
	@- git status

deploy: push clean
