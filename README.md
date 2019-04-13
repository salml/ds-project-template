# ds-project-template

This repo demonstrates how I like to set up a DS project in Python. Similar concepts apply to R, and I will likely build this out to exemplify a project with both Python and R code (this happens more than you would think in data science consulting).

## Startup
1. Clone the Github repository into your home directory. For OSX and Linux, you can get there with the following command:
```bash
cd ~
```
2. Set up package stuff (**repeat each session**)
```bash
source init.sh
```
In this example, the init script adds the location of our package to the PYTHONPATH environment variable. We need to run this code in order to import the project package into a script or notebook. 

