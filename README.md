# ds-project-template

This repo demonstrates how I like to set up a data science project in Python. There are three top-level folders in the simplest version of this file structure:
- `dev`: (initially) flat directory containing scripts and notebooks in development
- `src`: "production-ready" scripts and notebooks
- `package`: the project package packed with reusable, well-documented code (usually named something project related)

`package` is a collection of Python modules. `package/subpackage` is an example of a subpackage, and the `.py` files in `subpackage` are submodules. Together, packages, modules, subpackages, and submodules let us do stuff like this:

```python
import package
from package import module
import package.subpackage as sp
from package.subpackage import to_uppercase
```

However, the above code won't work without a start up script and some carefully placed `__init__.py` files. 

### Startup Scripts
Startup scripts are useful for just about every project. In this example, sourcing `init.sh` adds the location of `package` to the PYTHONPATH environment variable so that Python knows where to look when it searches for an imported package. A startup script might also activate a virtual environment to keep the team's package versions in sync (super minimal alternative to docker images). 

### __init__.py Files

In order for Python to recognize a folder as package, it must contain an `__init__.py` file. The import statements in an `__init__.py` file affect how modules can be imported. For example, `packages/__init__.py` contains the following code:
```python
from . import module
from . import subpackage
```
These statements let us do this:
```python
import package.module as mod
```
Otherwise, we would only be able to do this:
```python
from package import module
```

The `packages/subpackage/__init__.py` looks like this:
```python
from . import submodule
from .submodule import to_uppercase
```
The first line lets us do this:
```python
import package.subpackage.submodule as sub
```
And the second line lets us do this:
```python
from package.subpackage import to_uppercase
```

With these concepts, you can build a neat little Python package for your project, organized however you like thanks to your new friend, `__init__.py`.


## Getting started with the repo
Follow these steps to clone the repo and start playing with package architectures yourself:

1. Clone the Github repository into your home directory. For OSX and Linux, you can get there `cd ~`.
2. Set up package stuff with `source init.sh` (**repeat each session**)

In this example, the init script adds the location of our package to the PYTHONPATH environment variable. We need to run this code in order to import the project package into a script or notebook. 

If you don't want to put this in your home directory, edit `init.sh` change the PYTHONPATH accordingly.
