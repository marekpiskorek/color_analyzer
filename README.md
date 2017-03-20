# COLOR ANALYZER

Allows to get the 3 most dominant "dummy" colors from image files in given directory.
"Dummy" means one of following: black, red, yellow, green, cyan, blue, magenta, white.

This script uses [fengsp's Color Thief](https://github.com/fengsp/color-thief-py) as image color analyzing tool and [Flask](http://flask.pocoo.org/docs/0.12/) as a simple HTTP API server. [py.test](http://doc.pytest.org/en/latest/) is used as a test runner.

## Implementation:

### Script:
Color Thief's API is used in this script by calling `color_thief.get_palette` on each file. Returned color palette is used as a base for presenting the result of 3 "dummy" colors most dominant in this file. Of course, two or more colors from Color Thief's palette can represent the same "dummy" color, therefore `get_palette` is called with argument `color_count` equal to `10` - from 10 top colors we try to find 3 unique "dummy" colors.
#####Caution: in some cases (E.g. black and white pictures) only 2 results are expected.#####

### API:
The simplest way to provide a simple API endpoint was to use Flask. One small file with one function is enough to have a valid API endpoint and that's all that was needed.

## Installation:

`pip install -r requirements.txt`

## Usage:

### Script:

```
python analyzer.py
>>> There are no image files!
```
Ooops!
```
python analyzer.py path-to-image-directory
>>> data/magical.png:
> red
> black
> white
>>> data/all-the-sweaters.jpg:
> white
> black
> red
```

### API:

```
export FLASK_APP=endpoint.py
flask run -p 8000
curl -F "file=@data/magical.png" 127.0.0.1:8000/find_colors.json
{"colors": ["red", "black", "white"]}
```

### Test:

```
pip install -r requirements_test.txt
pytest test.py
```

Also, there are two example image files in `data` directory.


## Possible improvements:
Images could be analyzed asynchronously using Gevent or Celery which would significantly improve runtime and stability, but that wouldn't count as "an easy script".
