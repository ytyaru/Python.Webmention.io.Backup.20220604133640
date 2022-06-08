#!/usr/bin/env python3
# coding: utf8
import requests
import json
import time
class Client:
    def __init__(self):
        self.site = None
        self.site = 'https://ytyaru.github.io/'
        self.base = 'https://webmention.io/api/'
        self.endpoints = [
            'mentions',       # site単位（JSON）
            #'mentions.html', # site単位
            #'mentions.atom', # site単位
            'mentions.jf2',   # ページ単位（JSON）
            'count',          # ページ単位（JSON）
        ]
        self.params = {
            'token': 'z2Au0h3SRuqTfGv1ge7z8w',
            'domain': 'ytyaru.github.io',
            'target': 'https://ytyaru.github.io/MonaCoin.Icon.20220521092535/',
            'since': '2022-05-24T02:53:19+00:00', # 最初のメンション
            'since_id': 1403323,                  # 最初のメンション
            'per-page': 20,                       # デフォルト値（25KB程度）
            'page': 0,
        }
    def jf2(self, params):
        url = self.base + 'mentions.jf2'
        datas = {
            'params': params
        }
        return self._get_all_page('GET', url, datas)
    def _get_all_page(self, method, url, datas, jsons=None):
        print('_get_all_page', method, url, datas)
        #print(datas)
        #print('params' in datas)
        #print(datas['params'])
        res = requests.request(method, url, **datas)
        j = res.json()
        print(res)
        #print(j)
        per = datas['params']['per-page'] if 'per-page' in datas['params'] else 20
        #print(len(j['children']), per)
        if jsons is None: jsons = j
        else: jsons['children'].extend(j['children'])
        if len(j['children']) < per:
            #print('最後にここを通る')
            return jsons
        else:
            #print('次回のリクエストをする')
            time.sleep(2)
            if 'params' not in datas:
                datas['params'] = {'page': 0}
            if 'page' not in datas['params']:
                datas['params']['page'] = 0
            #print(datas['params'])
            datas['params']['page'] += 1
            #print('next_page:', datas['params']['page'])
            return self._get_all_page(method, url, datas, jsons);
        #print('ここにはこないはず')
        return jsons

    '''
    def mentions(self, page):#アカウント単位
        url = self.base + 'mentions'
        datas = {
            'params': params
        }
        return self._get_all_page('GET', url, datas)
    def page(self):
        'mentions.js2?target=指定ページURL'
    def count(self, target='https://ytyaru.github.io/'): #指定ページ単位でしか取得できない
        res = requests.get(self.base + 'count', params={'target': target})
        print(res)
        j = res.json()
        print(j)
        return j
    '''

if __name__ == "__main__":
    client = Client()
    client.jf2()

