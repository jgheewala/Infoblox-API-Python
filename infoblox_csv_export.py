#!/usr/bin/python
import infoblox
from sys import exit

if __name__ == '__main__':
    iba_api = infoblox.Infoblox('10.10.20.32', 'admin', 'secret', '1.6', 'internal', 'default')

    try:
        ip_json_result = iba_api.get_all_ipv4_address()
    except Exception as e:
        print e
        exit()
    #todo: need to convert the json data to csv data
    #x = json.loads(x)
    #f = csv.writer(open("test.csv", "wb+"))