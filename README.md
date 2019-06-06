# Test base.

## Build and install
Build using
```
python setup.py sdist
```

and then install by doing:

```
pip install . --user
```


## Running.

Run the code using following commands:

```
import Point
new_point = point.Point(2, 3)
new_point.show_point()
```


## How it works.

### Modules / package
Not entirly sure. __init__.py needed so that python knows it is a module. This needs to contain
```
from point import Point
```
otherwise to run the code you need:

```
from point.point import Point
a = Point(2, 3)
```
or
```
import point
point.point.Point()
```

### setup.py

