# flake8-raise-httpexceptions

Report any HTTPExceptions that are returned instead of raised. Plugin for
`flake8`, the Python code checker.


> This module is based on [flake8-fixme](https://github.com/tommilligan/flake8-fixme)

## Installation

Install with pip (not yet):

```bash
pip install flake8-raise-httpexceptions
```
or

```bash
python setup.py install
```

The plugin officially supports Python `>= 3.6` and `flake8 >= 3.7`.
You may find other Python 3 versions work as well.

```bash
flake8 --version
3.7.7 (flake8-raise-httpexceptions: 1.0.0, mccabe: 0.6.1, pycodestyle: 2.5.0, pyflakes: 2.1.1)
```

## Usage

The plugin finds HTTPExceptions that are returned instead of raised:

```python
return exception_response(
    409, json_body="User account not yet created, please retry."
)
```

```log
./file.py:1:0: X100 httpexception found (return exception_response)
```

Each return HTTPException has a seperate warning.

## Changelog

### 1.0.0

Initial code
