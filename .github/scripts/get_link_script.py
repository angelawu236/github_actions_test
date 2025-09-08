import os

# This script just adds/sets a GITHUB_ACTIONS paramenter "body" to a link 

link = "https://github.com/codemagic-ci-cd/cli-tools"

with open(os.environ['GITHUB_OUTPUT'], 'a') as fh:
    fh.write(f"body={link}\n")


