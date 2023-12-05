#!/usr/bin/python3

import json
import os
import sys
import logging
import shlex
from subprocess import check_output

logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
log = logging.getLogger('main')

MAIN_PR_URL= os.getenv('PR_URL')
cmd_ = f"gh pr view {MAIN_PR_URL} --json body,comments"
cmd = shlex.split(cmd_)

r = check_output(cmd)

d = json.loads(r.decode())
PR_BODY:str = d['body']

for SUBMODULE_PR_URL in PR_BODY.splitlines():
    repo = SUBMODULE_PR_URL.split('/')[-3]
    log.debug(repo)
    # cd repo && gh pr checkout URL
    cmd = f'gh pr checkout {SUBMODULE_PR_URL}'
    r = check_output(shlex.split(cmd), cwd=repo)
    log.debug(r)