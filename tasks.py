from invoke import run
from invoke import task

@task
def build(clean=False):
    cmd = "pip install -r requirements.txt"
    result = run(cmd, hide=True, warn=True)
    print(result.ok)

@task
def testAll(ctx):
    ctx.run("python3 -m unittest discover -s ./tests -p 'test*.py'")

