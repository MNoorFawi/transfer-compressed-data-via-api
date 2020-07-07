# transfer-compressed-data-via-api
Transfer data compressed by lzhw using a REST-ful API built using Flask.

###### Data used can be downloaded from [here](http://eforexcel.com/wp/downloads-18-sample-csv-files-data-sets-for-testing-sales/)

```bash
python app.py
```

```python
import requests
from time import time

start = time()
response = requests.get("http://127.0.0.1:5000/full?col=0")
print("time to request full data:", time() - start)
# time to request full data: 0.5261921882629395
```

```python
start = time()
response2 = requests.get("http://127.0.0.1:5000/compressed?col=0")
print("time to request compressed data:", time() - start)
# time to request compressed data: 0.05910205841064453
```

```python
## Length of the full response:
print(len(response.content))
# 42152700

## Length of the compressed response
print(len(response2.content))
# 6681639
```

```python
## Ratio between Compressed and Full
print(len(response2.content) / len(response.content))
# 0.1585103445330904
```

```python
start = time()
response = requests.get("http://127.0.0.1:5000/full?col=1")
print("time to request full data:", time() - start)
# time to request full data: 0.457775354385376

start = time()
response2 = requests.get("http://127.0.0.1:5000/compressed?col=1")
print("time to request compressed data:", time() - start)
# time to request compressed data: 0.11768484115600586

print(len(response2.content) / len(response.content))
# 0.441538985771116
```
