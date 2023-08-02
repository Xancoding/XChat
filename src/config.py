import os

# OpenAI API_KEY
API_KEY = "YOUR_OPENAI_API_KEY"

# 是否使用代理
USE_PROXY = True
if USE_PROXY:
    proxies = {
        "http": "http://127.0.0.1:7890",
        "https": "http://127.0.0.1:7890",
    }
    os.environ['http_proxy'] = proxies['http']
    os.environ['https_proxy'] = proxies['https']
else:
    proxies = None
