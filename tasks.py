from invoke import task

import os


@task
def build(c, docs=False):
    c.run('poetry install')
    c.run('poetry run pycodestyle contentscanner tests')
    c.run('poetry run coverage run -m pytest contentscanner tests')
    c.run('poetry build')
    if not os.path.exists('wordlist.txt'):
        print('No wordlist.txt found.')
    elif not os.path.exists('dist'):
        print('No dist/ found.')
    elif not os.listdir('dist'):
        print('No .whl or .gz found.')
    else:
        c.run('docker rm -f contentscanner')
        c.run('docker build -t contentscanner_img .')
        c.run('docker container create -i -t --name contentscanner contentscanner_img')
