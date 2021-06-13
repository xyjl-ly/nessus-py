import requests
import json
import time
import urllib3.packages
from urllib3.exceptions import InsecureRequestWarning

urllib3.disable_warnings(InsecureRequestWarning)

ip = "127.0.0.1"
port = "8834"
accessKey = "6b306e97194a7c5df0ff75f1a4fe51384b604041dae0385b44efa56481d30132"
secretKey = "bdd66cb6ae57f7dca0a6921a6988e37c1c8fd472bd103bec7c2db0024d9c36ce"
header = {
    'X-ApiKeys': f'accessKey={accessKey};secretKey={secretKey}',
    'Content-type': 'application/json',
    'Accept': 'text/plain'
}


def get_scan_list():
    ids = []
    api = f"https://{ip}:{port}/scans"
    if api:
        response = requests.get(api, headers=header, verify=False)
        res = response.json()['scans']
        try:
            for re in res:
                nid = re['id']
                ids.append(nid)
                return ids
        except TypeError:
            print("没有任务在运行")
    else:
        print("请确认自己的api是否正确")


def stop_all():
    try:
        for scan_id in get_scan_list():
            api = f"https://{ip}:{port}/scans/{scan_id}/stop"
            response = requests.post(api, headers=header, verify=False)
            if response.status_code == 200 or response.status_code == 409:
                print("stop all ok")
            else:
                print("stop all error")
                print(response.text)
    except TypeError:
        print("程序已经结束")
        exit()


def del_all():
    try:
        for scan_id in get_scan_list():
            api = f"https://{ip}:{port}/scans/{scan_id}"
            if api:
                response = requests.delete(api, headers=header, verify=False)
                if response.status_code == 200:
                    print("delete all ok")
                else:
                    print("delete all error!!!!")
                    print(f"{response.text}")
    except TypeError:
        exit()


if __name__ == '__main__':
    stop_all()
    print("请等待，任务停止需要冷却20s")
    time.sleep(20)
    del_all()
