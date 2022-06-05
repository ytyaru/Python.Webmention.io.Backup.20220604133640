#!/usr/bin/env python3
# coding: utf8
import os
import sys
import json
import requests
import collections
import io
import client
import setting
class Backup:
    def __init__(self):
        self.client = client.Client()
        self.setting = setting.Setting()
        self.since = None
        self.since_id = None
        self.file_num = 0
        self.old_file = None
    def domain(self):
        print('------------- domain -------------')
        print(self.setting.get())
        for setting in self.setting.get():
            file_path, j = self._get_last_file()
            params = {
                'token': setting[0],
                'domain': setting[1],
#                'token': self.client.params['token'],
#                'domain': self.client.params['domain'],
            }
            if self.since is not None: params['since'] = self.since
            new_json = self.client.jf2(params)
            print('新しいメンションを取得した:', len(new_json['children']))
            if 0 == len(new_json['children']):
                print('新しいmentionはありません。')
            else:
                print('新しいmentionがあります。')
                if j is None:
                    tails = list(collections.deque(new_json['children'], self.client.params['per-page']))
                    print('------------ 空のfileに20件だけそのまま書く -------------')
                    print(tails)
                    print('------------ こんな書式。これJSON形式じゃないと怒られる-------------')
                    print(json.dumps(tails, ensure_ascii=False))
                    with open(file_path, 'w', encoding='utf-8') as f: f.write(self._dump(tails))
                    new_json['children'] = new_json['children'][:(self.client.params['per-page']*-1)]
                    print('------------ 残りJSON -------------', len(new_json['children']))
                    print(new_json['children'])
                else:
                    print('------------ 既存JSONファイルに追記：20件以内に収める -------------')
                    l = self.client.params['per-page'] - len(j)
                    tails = list(collections.deque(new_json['children'], l))
                    print(tails)
                    print(len(j))
                    j[0:0] = tails
                    print(len(j))
                    new_json['children'] = new_json['children'][:(l*-1)]
                    with open(file_path, 'w', encoding='utf-8') as f: f.write(self._dump(j))
                if 0 < len(new_json['children']):
                    self._filing(new_json)
    def _get_json_file_num(self):
        dir_path = os.path.join(os.getcwd(), self.client.params['domain'])
        print(dir_path)
        if not os.path.isdir(dir_path):
            os.makedirs(dir_path, exist_ok=True)
        self.file_num = sum(os.path.isfile(os.path.join(dir_path, name)) for name in os.listdir(dir_path))
        return self.file_num
    def _get_last_file_path(self):
        dir_path = os.path.join(os.getcwd(), self.client.params['domain'])
        return os.path.join(dir_path, f'{0 if self.file_num <= 0 else self.file_num - 1}.json')
    def _get_last_file(self):
        self._get_json_file_num()
        file_path = self._get_last_file_path()
        if 0 == self.file_num: return file_path, None
        with open(file_path, 'r', encoding='utf-8') as f: j = json.load(f)
        self.since = j[0]['wm-id']
        self.since_id = j[0]['wm-received']
        if len(j) < self.client.params['per-page']: return file_path, j
#        else: return self._get_next_file_path(), None
        else:
            self.file_num += 1
            return self._get_last_file_path(), None
    def _get_next_file_path(self):
        self.file_num += 1
        dir_path = os.path.join(os.getcwd(), self.client.params['domain'])
        return os.path.join(dir_path, f'{self.file_num}.json')
        #return os.path.join(dir_path, f'{self.file_num - 1}.json')
    def _filing(self, j):
        file_path = self._get_next_file_path()
        with open(file_path, 'w', encoding='utf-8') as f: f.write(self._dump(j['children']))
        j['children'] = j['children'][:(self.client.params['per-page']*-1)]
        if 0 < len(j['children']):
            return self._filing(j)
    def _dump(self, j):
        return json.dumps(j, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    backup = Backup()
    backup.domain()

