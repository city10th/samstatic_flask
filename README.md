# samstatic_flask
A Flask extension, which can enable the same static url (e.g. `/static`) search multi folders (e.g. `/static`, `/upload`) 

使Falsk支持相同静态文件路径（如：`/static`）搜索不同文件夹（如：`/static`, `/upload`）

Falskに同じ静的ファイルパスをサポートさせる(例:`/static`)異なるフォルダを検索する(例:`/static`, `/upload`)

* author: City10th
* email: city10th@foxmail.com
* url: [github](https://github.com/city10th/samstatic_flask)

# quick start
## method 1

```python
import Flask
from samstatic_flask import SamStatic
app = Flask(__name__)
SamStatic(app)
```
## method 2
```python
from samstatic_flask import FlaskWithSamStatic
app = FlaskWithSamStatic(__name__)
```

# option
## app.config['SAMSTATIC_ENDPOINTS']
### `SameStatic.options.ALL`
- Default. The same as `'ALL'` or `('ALL',)`
- This will search the static endpoint of app and its ALL blueprints
### `SameStatic.options.DEACTIVE`
- The same as `'DEACTIVE'` or `('DEACTIVE',)`
- This will deactivate samstatic_flask.
### `(SameStatic.options.ALLOWED, {'endpoint1', 'endpoint2'})`
- The same as `('DEACTIVE', {'endpoint1', 'endpoint2'})`
- This will ALLOWED only customized endpoints in ALL static endpoints.
### `(SameStatic.options.DISALLOWED, {'endpoint1', 'endpoint2'})`
- The same as `('DISALLOWED', {'endpoint1', 'endpoint2'})`
- This will DISALLOWED customized endpoints from ALL static endpoints.
## app.config['SAMSTATIC_ENDPOINTS_USE_CACHE']
- Defualt True
- This will cache the static endpoint