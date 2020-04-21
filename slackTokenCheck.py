#!/usr/bin/env python
# coding: utf-8
# requests template
# By Leon Johnson - twitter.com/sho_luv

import sys
import json
import argparse
import requests
from pprint import pprint
from termcolor import colored, cprint

# https://help.github.com/en/github/administering-a-repository/about-token-scanning

def check_auth(site):
    request = site
    print("\nchecking ",end='')
    cprint(options.token,'white')
    print("")
    response = requests.get(request)
    value = response.text
    try:
        values = response.json()
        if values['ok']:
            found = colored("[+]", "green")
            print(found,"Found valid token:", options.token)
            #cprint("[+] URL ",'green',end='')
            print(found,"URL: ",end='')
            cprint(values['url'],'white')
            print(found,"Team: ",end='')
            cprint(values['team'],'white')
            print(found,"User: ",end='')
            cprint(values['user'],'white')
            print(found,"Team ID: ",end='')
            cprint(values['team_id'],'white')
            print(found,"User ID: ",end='')
            cprint(values['user_id'],'white')
        else:
            print("I'm sorry try again this token is not valid ",end='')
            cprint("womp womp :(","yellow")
    except ValueError:
        print('Unable to decode JSON')
        exit(1)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This program makes web requests.')
    parser.add_argument('token', action='store', metavar='token',help="token you would like to check")
    #group = parser.add_mutually_exclusive_group()
    #group = parser.add_argument_group('carrier')
    #group.add_argument('-att', action='store_true', help='Send text message to AT&T Wireles')

    if len(sys.argv)==1:
        parser.print_help()
        sys.exit(1)

    options = parser.parse_args()

    auth_test = "https://slack.com/api/auth.test?token="+options.token

    check_auth(auth_test)
