import requests
import json
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


def get_ness_template_uuid(template_name='advanced'):
    api = f"https://{ip}:{port}/editor/scan/templates"
    response = requests.get(api, headers=header, verify=False)
    ts = response.json()
    templates = ts['templates']
    for template in templates:
        if template['name'] == template_name:
            print(f"高级扫描：{template['name']} {template['uuid']}")
            return template['uuid']


def new_scan(name, hosts):
    uuid = get_ness_template_uuid()
    api = f"https://{ip}:{port}/scans"
    data = {"uuid": uuid,
            "settings":
                {
                    "name": name,
                    "text_targets": hosts
                }
            }
    response = requests.post(api, headers=header, data=json.dumps(data, ensure_ascii=False).encode("utf-8"), verify=False)
    if response.status_code == 200:
        data = json.loads(response.text)
        scan = data['scan']
        return scan['id']


def start():
    api = f"https://{ip}:{port}/scans/{scan_id}/launch"
    response = requests.post(api, headers=header, verify=False)
    if response.status_code == 200:
        return 'ok'
    else:
        return 'no'


if __name__ == '__main__':
    with open('ip.txt', 'r', encoding='utf-8') as f:
        targets = f.readlines()
    for target in targets:
        target = target.strip()
        scan_id = new_scan(target, target)
        if start() == 'ok':
            print(f"{target} 任务建立成功")
        else:
            print(f"{target} 任务建立失败")
