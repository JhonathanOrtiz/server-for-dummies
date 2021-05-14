from typing import Tuple
import json
import requests

PROXY_ROTATOR_API_KEY="dRDJk45FE3poyuNBPqrTaAVC8HYL9hzm"
PROXY_ROTATOR_URL="http://falcon.proxyrotator.com:51337"

def get_proxy() -> Tuple[str, str]:
    """Get a proxy and user agent from proxyrotator.

    Returns:
        Tuple[str, str]: proxy and user agent.
    """
    params = dict(
        apiKey=PROXY_ROTATOR_API_KEY,
        connectionType="Residential",
        country="US",
    )

    resp = requests.get(url=PROXY_ROTATOR_URL, params=params)
    data = json.loads(resp.text)
    CACHED_PROXY = f"http://{data['proxy']}", data
    return CACHED_PROXY
_, proxy = get_proxy()

url ="http://127.0.0.1:8000/"
headers = {"X-Forwarded-For": proxy["proxy"], "user-agent": proxy["randomUserAgent"]}
print(proxy["proxy"], proxy["randomUserAgent"])
print(" ")
print(requests.get(url, headers=headers).content)