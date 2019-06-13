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
pip install -e pkg
```

Now, if the environment is activated, we will be able to import `fakeproj`. Otherwise, the computer has no idea what `fakeproj` is. We can also export the environment:

```bash
conda env export > env.yml
```

This produces a `yaml` file capturing all of the `conda` and `pip` packages installed in your `ds-project-template` environment. Although the environment gives us access to `fakeproj` when we activate it, that is not reflected in the `yaml` file itself, so when you share the project with another person, they'll need to create the environment and install `fakeproj` into it:

```bash
conda env create -f env.yml
pip install -e pkg
```

The `-e` part of installing `fakeproj` stands for `--editable`, and it allows us to develop the package as we go. That way, when we make a change to the package, we don't have to reinstall it! You will, however, need to reimport it. 


## Documentation
