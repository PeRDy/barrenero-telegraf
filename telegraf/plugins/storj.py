#!/usr/bin/env python3
import sys
from configparser import ConfigParser
from json import JSONDecodeError

import requests

OUTPUT = '{},host={},id={} ' \
         'allocs={},peers={},restarts={},shared={},shared_percent={},contracts={},delta={},status="{}",uptime="{}",' \
         'response_time={},reputation={},version="{}"'

SIZE = {
    'MB': 1,
    'GB': 1024,
    'TB': 1024 ** 2,
    'PB': 1024 ** 3,
    'HB': 1024 ** 4,
}

API_RESOURCE = 'storj'


def storj_status(api_url, token):
    url = '{}/{}/'.format(api_url, API_RESOURCE)
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
                'allocs': node['allocs'],
                'data_received': node['data_received'] if node['data_received'] is not None else -1,
                'delta': abs(node['delta']) if node['delta'] is not None else -1,
                'shared': shared,
                'shared_percent': node['shared_percent'] if node['shared_percent'] is not None else -1,
                'response_time': node['response_time'] if node['response_time'] is not None else -1,
                'reputation': node['reputation'] if node['reputation'] is not None else -1,
                'version': node['version'] if node['version'] is not None else 'None',
            }
    except (JSONDecodeError, requests.HTTPError):
        pass


def main():
    config = ConfigParser()
    config.read('setup.cfg')
    api_url = config.get('api', 'url') + '/api/v1'
    token = config.get('api', 'token')
    database = config.get('influxdb', 'database')

    for status in storj_status(api_url, token):
        print(OUTPUT.format(database, 'barrenero', status['id'], status['allocs'], status['peers'], status['restarts'],
                            status['shared'], status['shared_percent'], status['data_received'], status['delta'],
                            status['status'], status['uptime'], status['response_time'], status['reputation'],
                            status['version']))


if __name__ == '__main__':
    sys.exit(main())
