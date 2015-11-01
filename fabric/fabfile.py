from fabric.api import run, env
from fabric.operations import sudo
import logging
import ConfigParser
import os
import sys


def readconf(dirname,filename):
    config = ConfigParser.ConfigParser()
    try:
        config.readfp(open(os.path.join(dirname, filename)))
    except IOError as (errno, strerror):
        print "Cannot read the config file:", strerror
        sys.exit(1)
    sections = dict(config._sections)
    logging.info("Settings")
    logging.info(sections)
    return sections


def Hosts(name):
    dirname="/home/raju/scriptsPractise/fabric"
    filename="fab.cfg"
    settings=readconf(dirname,filename)
    data = settings[name]['host']
    hostslist=[]
    host=[]
    hostslist=data.split(',');
    length=len(hostslist)
    i=0
    for line in hostslist:
        if i < length:
           host.insert(i,line)
           i=i+1
    return host

def Passwords(name):
    hostlist = []
    hostlist = Hosts(name)
    dirname="/home/raju/scriptsPractise/fabric"
    filename="fab.cfg"
    settings=readconf(dirname,filename)
    data = settings[name]['password']
    passwordlist=[]
    password= {}
    passwordlist=data.split(',');
    length=len(passwordlist)
    i=0
    for line in passwordlist:
        if i < length:
           password[hostlist[i]]=line
           i=i+1
    return password

def ofHost(name):
    env.hosts=Hosts(name)
    env.passwords=Passwords(name)
 


def connect():
    run('ls')

def rootLogin():
    sudo('su')   



