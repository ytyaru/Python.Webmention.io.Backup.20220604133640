#!/usr/bin/env python3
# coding: utf8
import os, sys, io, json, time
import requests
import collections
from urllib.parse import urlparse
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
    def target(self): # ページ単位
        print('------------- target -------------')
        with open(os.path.join(os.getcwd(), 'targets.tsv'), 'r', encoding='utf-8') as f:
            for target in f:
                target = target.strip()
                if 0 == len(target): continue
                url = urlparse(target)
                dir_path = os.path.join(os.getcwd(), 'backup', url.netloc).strip('-')
                os.makedirs(dir_path, exist_ok=True)
                file_id = url.path.replace(os.path.sep, '-').strip('-')
                file_name = f"{url.netloc if 0 == len(file_id) else file_id}".strip('-') + '.json'
                file_path = os.path.join(dir_path, file_name)
                print(file_path)
                params = {
                    'target': target,
                    'per-page': sys.maxsize,
                    'page': 0,
                }
                # すでにファイルがある（既存ファイルを開いて最終日時を取得する）
                # まだファイルがない（新規作成）
                j = None
                if os.path.isfile(file_path):
                    with open(file_path, 'r', encoding='utf-8') as f:
                        j = json.load(f)
                        self.since = j[0]['wm-received']
                        self.since_id = j[0]['wm-id']
                        params['since'] = self.since
                else:
                    self.since = None
                    self.since_id = None
                new_json = self.client.jf2(params)
                print('新しいメンションを取得した:', len(new_json['children']))
                if 0 == len(new_json['children']):
                    print('新しいmentionはありません。')
                else:
                    print('新しいmentionがあります。')
                    if j is None:
                        print('------------ 新しいJSONファイルに全件出力する -------------')
                        with open(file_path, 'w', encoding='utf-8') as f: f.write(self._dump(new_json['children']))
                    else:
                        print('------------ 既存JSONファイルの配列の先頭に追記する -------------')
                        j[0:0] = new_json['children']
                        with open(file_path, 'w', encoding='utf-8') as f: f.write(self._dump(j))
                time.sleep(1)
    def domain(self): # ドメイン単位（なぜかページ単位で取得できたメンションが取得できない）
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
        self.since = j[0]['wm-received']
        self.since_id = j[0]['wm-id']
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
    backup.target()
#    backup.domain()

