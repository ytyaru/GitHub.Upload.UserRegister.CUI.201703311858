#!/usr/bin/python3
#!python3
#encoding:utf-8
import os.path
import subprocess

class Main:
    def __init__(self):
        pass
        """
    def __init__(self, data, client):
        self.data = data
        self.client = client
        data = database.src.Data.Data(args.path_dir_pj, path_dir_db, args.username, args.description, args.homepage)
        client = web.service.github.api.v3.Client.Client(data)
        """

    def Insert(self, args):
        print('Account.Insert')
        print(args)
        print('-u: {0}'.format(args.username))
        print('-p: {0}'.format(args.password))
        print('-m: {0}'.format(args.mailaddress))
        print('-s: {0}'.format(args.ssh_public_key_file_path))
        print('-t: {0}'.format(args.two_factor_secret_key))
        print('-r: {0}'.format(args.two_factor_recovery_code_file_path))
        print('--auto: {0}'.format(args.auto))

    def Update(self, args):
        print('Account.Update')
        print(args)
        print('-u: {0}'.format(args.username))
        print('-p: {0}'.format(args.password))
        print('-m: {0}'.format(args.mailaddress))
        print('-s: {0}'.format(args.ssh_public_key_file_path))
        print('-t: {0}'.format(args.two_factor_secret_key))
        print('-r: {0}'.format(args.two_factor_recovery_code_file_path))
        print('--auto: {0}'.format(args.auto))

    def Delete(self, args):
        print('Account.Delete')
        print(args)
        print('-u: {0}'.format(args.username))
        print('--auto: {0}'.format(args.auto))

    def Tsv(self, args):
        print('Account.Tsv')
        print(args)
        print('path_file_tsv: {0}'.format(args.path_file_tsv))
        print('--method: {0}'.format(args.method))

