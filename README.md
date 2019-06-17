# ds-project-template

This repo demonstrates how I like to set up a data science project in Python. There are three top-level folders in the simplest version of this file structure:
- `notebooks`: (initially) flat directory of notebooks
- `scripts`: (intitially) flat directory fo scripts
- `pkg`: folder containing the project's internal package

## Environment Control
`conda` is where it's at for making sure you can replicate your environments over time and across projects. Plus, it prevents us from needing to reinstall our package everytime we want to use it. Here's how we initially created it:

```bash
conda create env -n ds-project-template
conda activate ds-project-template
conda install jupyterlab
conda install pandas
conda install pytest
conda install sphinx
```

Now, we can go ahead and install our package into the environment by navigating to `pkg` and running `make init` which will use the Makefile to run the commands under `init`. We will go back to this Makefile throughout the project - it's a really easy way to track and organize simple collections of commands for different purposes. The file itself is easy to read, too.

With the environment activated and the package installed, we will be able to import `fakeproj`. Otherwise, the computer would have no idea what `fakeproj` is. We can also export the environment:

```bash
conda env export > env.yml
```

This produces a `yaml` file capturing all of the `conda` and `pip` packages installed in your `ds-project-template` environment. Although the environment gives us access to `fakeproj` when we activate it, that is not reflected in the `yaml` file itself, so when you share the project with another person, they'll need to create the environment and install `fakeproj` into it:

```bash
conda env create -f env.yml
pip install -e pkg
```

Alternatively, they could use the Makefile:

```bash
conda env create -f env.yml
cd pkg
make init
```

The `-e` part of installing `fakeproj` stands for `--editable`, and it allows us to develop the package as we go. That way, when we make a change to the package, we don't have to reinstall it! You will, however, need to reimport it. If we hadn't used the `-e` option, the package would show up explicitly when we export the environment to `env.yml`, but we would need to reinstall it whenever we make a change (`make install` via the Makefile).

Another useful tip for working with packages alongside Jupyter Notebooks: add the following cell magic to the first cell in the notebook so that your import statements reflect the latest changes in your code:

```python
%load_ext autoreload
%autoreload 2
```

## Documentation w/ sphinx

Sphinx is a tool for automatic documentation of Python packages. It works together with docstrings to generate HTML documentation like what you would see on `readthedocs`. To generate documentation for the project, enter the `pkg` directory, and run `make -C docs html`. This will create a `_build` folder in the `pkg/docs` with HTML for a documents web page based on your docstrings. Big thanks to @enmyj for tackling this!

## Unit Testing with pytest

`pytest` is the go-to framework for unit- and integreation-testing in Python. Use `make unittest`, `make integrationtest`, and/or `make alltests` to run your tests. 