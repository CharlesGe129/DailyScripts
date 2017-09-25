import requests
requests.adapters.DEFAULT_RETRIES = 10

session_requests = requests.session()
session_requests.keep_alive = False

payload = {
    'username': 'yge7',
    'password': 'Sal1129alwfor#',
}
login_url = 'https://usfcas.usfca.edu/cas/login?service=https%3A%2F%2Fmyusf.usfca.edu%2Fuser%2F47227%2Fview'
result = session_requests.post(
    login_url,
    data=payload,
    headers=dict(referer=login_url)
)
url = 'https://myusf.usfca.eud/user/47227/view'
result = session_requests.get(
    url,
    headers=dict(referer=url)
)
print(123)