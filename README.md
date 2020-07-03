# transfer-compressed-data-via-api
Transfer data compressed by lzhw using a REST-ful API built using Flask.

```bash
python app.py
```

```python
import requests
from time import time

start = time()
response = requests.get('http://127.0.0.1:5000/full')
print("time to request full data:", time() - start)
# time to request full data: 0.011967897415161133
```

```python
start = time()
response2 = requests.get('http://127.0.0.1:5000/compressed')
print("time to request compressed data:", time() - start)
# time to request compressed data: 0.0059506893157958984
```

```python
## Length of the full response:
print(len(response.content))
# 500311

## Length of the compressed response
print(len(response2.content))
# 85553
```

```python
## Ratio between Compressed and Full
print(len(response2.content) / len(response.content))
# 0.17099963822502404
```