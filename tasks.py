from invoke import run
cmd = "pip install -r requirements.txt"
result = run(cmd, hide=True, warn=True)
print(result.ok)
