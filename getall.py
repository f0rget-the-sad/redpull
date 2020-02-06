#!/usr/bin/env python
import os
import sys
from redminelib import Redmine

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import logging
log = logging.getLogger("redmine")
log.setLevel(logging.DEBUG)
log.addHandler(logging.StreamHandler())

REDM_URL = "https://redmine.interfacemasters.com/redmine"
DOWNLOAD_ROOT = "/tmp"

def connect(usr, passwrd):
    log.debug(f"Connecting to: {REDM_URL}")
    redmine = Redmine(REDM_URL, username=usr, password=passwrd, requests={'verify': False})

    log.info(f"Hi, {usr}")
    return redmine

def download_attached(redmine, issue_id):
    issue = redmine.issue.get(issue_id)
    log.debug(issue)
    log.debug(f"Attachments: {[a.filename for a in issue.attachments]}")
    download_dir = f"{DOWNLOAD_ROOT}/{issue_id}/"
    os.makedirs(download_dir,  exist_ok=True)

    log.info("Start downloading...")
    for a in issue.attachments:
        log.info(f"\t* {a.filename}")
        a.download(savepath=download_dir)

    log.info(f"Successfully downloaded {len(issue.attachments)}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        log.error("Wrong number of arguments!")
        log.info(f"Usage {__file__} login password issue_id")
        sys.exit(1)
    download_attached(connect(sys.argv[1], sys.argv[2]), sys.argv[3])
