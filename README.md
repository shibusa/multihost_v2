# Multihost v2 - Multiple host BASH Query Tool

Rewrite of [multihost](https://github.com/shibusa/multihost).

Improvements:
- Created functions available for import
- Supports multivariable commands
- Supports flexible file names

## Requirements
- Python 2.7 on local system
- BASH on local and remote system
- ssh-key authentication of remote systems for ssh related commands

## Usage
1. Determine if commands will be run remotely or locally. If ssh is required, create a host file with an ip or hostname on each line.
```
fqdn.host.io
192.168.1.25
```
2. Determine command and variables you'll be using
Example:
```
ping -c <pingcount> <hostname>
```
3. Create corresponding command variable file in table delimited format
```
5 google.com
10 yahoo.com
```
### Using imported functions
For SSH:
```
ssh(sshaccount, hostsfile, command, commandvarsfile=None, outputfile="output.txt")
```
For non-SSH:
```
nossh(command, commandvarsfile, outputfile="output.txt")
```

All inputs are strings. Replace command variables in command with `{}`. I.E. `ping -c {} {}`
```
nossh("ping -c {} {}", "commandfile.txt")
```

### Command line usage
#### First run
1. Locate multihost.py file
2. Make script executable
```
chmod +x multihost.py
```
#### Running script
1. Run script.  Similarly to using imported functions, replace command variables in command with `{}`. I.E. `ping -c {} {}`
```
./multihost.py
```
2. Check for outputs in output file
