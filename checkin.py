import os
import requests
import json
from datetime import datetime, timezone
def checkin():
    cookie_uid = os.environ.get('COOKIE_UID')
    cookie_email = os.environ.get('COOKIE_EMAIL')
    cookie_key = os.environ.get('COOKIE_KEY')
    cookie_ip = os.environ.get('COOKIE_IP')
    cookie_expire = os.environ.get('COOKIE_EXPIRE')
    cookie = f"uid={cookie_uid}; email={cookie_email}; key={cookie_key}; ip={cookie_ip}; expire_in={cookie_expire}"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
        'Origin': 'https://ikuuu.win',
        'Referer': 'https://ikuuu.win/user',
        'X-Requested-With': 'XMLHttpRequest',
        'Cookie': cookie,
        'Content-Length': '0',
    }
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    print(f"[{now}] Starting ikuuu checkin...")
    try:
        resp = requests.post('https://ikuuu.win/user/checkin', headers=headers, timeout=30)
        print(f"Status: {resp.status_code}")
        print(f"Response: {resp.text}")
        try:
            data = resp.json()
            print(f"Result: {data}")
            if data.get('ret') == 0:
                msg = data.get('msg', '')
                if '已签到' in msg or '签到过' in msg:
                    print("Already checked in today")
                else:
                    print(f"Checkin successful! {msg}")
            else:
                print(f"Checkin failed: {data}")
        except json.JSONDecodeError:
            print("Response is not JSON")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        raise
if __name__ == '__main__':
    checkin()
