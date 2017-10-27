#!/usr/bin/env python3
import json
import os
import sys
from configparser import ConfigParser
from json import JSONDecodeError

import requests

OUTPUT = 'storj,host={},id={} ' \
         'offers={},peers={},restarts={},shared={},shared_percent={},contracts={},delta={},status="{}",uptime="{}"'

SIZE = {
    'MB': 1,
    'GB': 1024,
    'TB': 1024 ** 2,
    'PB': 1024 ** 3,
    'HB': 1024 ** 4,
}

API_RESOURCE = 'storj'


def storj_status(api_url, token):
    url = '{}/{}'.format(api_url, API_RESOURCE)
    response = requests.get(url, headers={'Authorization': 'Token {}'.format(token)})
    try:
        response.raise_for_status()

        for node in response.json():
            if node['shared'] is None:
                shared = -1
            else:
                try:
                    shared = float(node['shared'][:-2]) * SIZE[node['shared'][-2:]]
                except KeyError:
                    shared = -2

            yield {
                'id': node['id'],
                'status': node['status'],
                'uptime': node['uptime'],
                'restarts': node['restarts'],
                'peers': node['peers'],
                'offers': node['offers'],
                'data_received': node['data_received'] if node['data_received'] is not None else -1,
                'delta': abs(node['delta']) if node['delta'] is not None else -1,
                'shared': shared,
                'shared_percent': node['shared_percent'] if node['shared_percent'] is not None else -1,
            }
    except (JSONDecodeError, requests.HTTPError):
        pass


def main():
    config = ConfigParser()
    config.read('setup.cfg')
    api_url = config.get('api', 'url') + '/api/v1'
    token = config.get('api', 'token')

    for status in storj_status(api_url, token):
        print(OUTPUT.format('barrenero', status['id'], status['offers'], status['peers'], status['restarts'],
                            status['shared'], status['shared_percent'], status['data_received'], status['delta'],
                            status['status'], status['uptime']))


if __name__ == '__main__':
    sys.exit(main())
