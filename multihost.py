#!/usr/bin/env python

from sys import argv
from subprocess import check_output
from os.path import isfile
from os import remove

def ssh(sshaccount, hostsfile, command, commandvarsfile=None, outputfile="output.txt"):
    hostsfile = open(hostsfile, 'r')
    if commandvarsfile:
        commandvarsfile = open(commandvarsfile, 'r')
    if isfile(outputfile):
        remove(outputfile)
    outputfile = open(outputfile, 'w+')

    for line in hostsfile:
        if commandvarsfile:
            try:
                currentlinedata = commandvarsfile.readline()
                vararr = currentlinedata.strip().split(" ")
            except:
                pass
        else:
            vararr = []
        commandarr = ["ssh", "{}@{}".format(sshaccount, line.strip()), command.format(*vararr)]
        issuecommand(commandarr, outputfile)

    hostsfile.close()
    if commandvarsfile:
        commandvarsfile.close()
    outputfile.close()
    exit()

def nossh(command, commandvarsfile, outputfile="output.txt"):
    commandvarsfile = open(commandvarsfile, 'r')
    if isfile(outputfile):
        remove(outputfile)
    outputfile = open(outputfile, 'w+')

    for line in commandvarsfile:
        vararr = line.strip().split(" ")
        commandarr = command.format(*vararr).split(" ")
        issuecommand(commandarr, outputfile)

    commandvarsfile.close()
    outputfile.close()
    exit()

def issuecommand(commandarr, file):
    try:
        output = check_output(commandarr)
        file.write("-"*50 + "\n{}\n".format(" ".join(map (str, commandarr))) + "-"*50 + "\n{}".format(output))
    except OSError:
        print "Unable to run command"
        file.close()
        exit()

if __name__ == '__main__':
    comm = raw_input("BASH Command: ")
    commarr = raw_input("BASH Variable File: ")
    output = raw_input("Output file (Default outputs.txt):")
    valid = ["yes", "y", "no", "n"]
    sshcheck = ""
    while sshcheck not in valid:
        sshcheck = raw_input("SSH to remote hosts?: ")
    if sshcheck in valid[0:2]:
        sshaccount = raw_input("Account: ")
        sshhosts = raw_input("SSH hosts file: ")
        if isfile(output):
            ssh(sshaccount, sshhosts, comm, commarr, output)
        else:
            ssh(sshaccount, sshhosts, comm, commarr)
    elif sshcheck in valid[2:]:
        if isfile(output):
            nossh(comm, commarr, output)
        else:
            nossh(comm, commarr)
