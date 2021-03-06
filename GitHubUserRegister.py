#!/usr/bin/python3
#!python3
#encoding:utf-8
import sys
import os.path
import subprocess
import configparser
import argparse
import web.service.github.api.v3.Client
import database.src.Create
import cui.uploader.Main
import cui.register.Main

class Main:
    def __init__(self):
        pass

    def Run(self):
        parser = argparse.ArgumentParser(
            description='GitHub User Resist CUI.',
        )
        sub_parser = parser.add_subparsers()

        # insertサブコマンド
        parser_insert = sub_parser.add_parser('insert', help='see `insert -h`')
        parser_insert.add_argument('-u', '--username', '--user')
        parser_insert.add_argument('-p', '--password', '--pass')
        parser_insert.add_argument('-m', '--mailaddress', '--mail')
        parser_insert.add_argument('-s', '--ssh-public-key-file-path', '--ssh')
        parser_insert.add_argument('-t', '--two-factor-secret-key', '--two')
        parser_insert.add_argument('-r', '--two-factor-recovery-code-file-path', '--recovery')
        parser_insert.add_argument('-a', '--auto', default=False)
        parser_insert.set_defaults(handler=self.__insert)

        # updateサブコマンド
        parser_update = sub_parser.add_parser('update', help='see `update -h`')
        parser_update.add_argument('-u', '--username', '--user')
        parser_update.add_argument('-p', '--password', '--pass')
        parser_update.add_argument('-m', '--mailaddress', '--mail')
        parser_update.add_argument('-s', '--ssh-public-key-file-path', '--ssh')
        parser_update.add_argument('-t', '--two-factor-secret-key', '--two')
        parser_update.add_argument('-r', '--two-factor-recovery-code-file-path', '--recovery')
        parser_update.add_argument('-a', '--auto', default=False)
        parser_update.set_defaults(handler=self.__update)

        # deleteサブコマンド
        parser_delete = sub_parser.add_parser('delete', help='see `delete -h`')
        parser_delete.add_argument('-u', '--username', '--user')
        parser_delete.add_argument('-a', '--auto', default=False)
        parser_delete.set_defaults(handler=self.__delete)

        # tsvサブコマンド
        parser_delete = sub_parser.add_parser('tsv', help='see `tsv -h`')
        parser_delete.add_argument('path_file_tsv')
        parser_delete.add_argument('-m', '--method', '--marge', default=[], choices=['insert','update','delete'], action='append')        
        parser_delete.set_defaults(handler=self.__tsv)
        
        # コマンドライン引数をパースして対応するハンドラ関数を実行
        args = parser.parse_args()
        if hasattr(args, 'handler'):
            args.handler(args)
        else:
            # 未知のサブコマンドの場合はヘルプを表示
            parser.print_help()

    def __insert(self, args):
        main = cui.register.Main.Main()
        main.Insert(args)

    def __delete(self, args):
        main = cui.register.Main.Main()
        main.Delete(args)

    def __update(self, args):
        main = cui.register.Main.Main()
        main.Update(args)

    def __tsv(self, args):
        main = cui.register.Main.Main()
        main.Tsv(args)


if __name__ == '__main__':
    main = Main()
    main.Run()
