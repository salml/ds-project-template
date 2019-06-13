# ds-project-template

This repo demonstrates how I like to set up a data science project in Python. There are three top-level folders in the simplest version of this file structure:
- `notebooks`: (initially) flat directory of notebooks
- `scripts`: (intitially) flat directory fo scripts
- `pkg`: folder containing the project's internal package

`pkg` is wrapper fold that contains the package itself and a `setup.py` file that allows us to install the package via

```bash
pip install -e pkg
```
