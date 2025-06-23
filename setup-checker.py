#!/usr/bin/env python
# coding: utf-8

# # Environment Setup Checker
# 
# this notebook is used to check the environment setup of the user.
# 
# it will check the following:
# - python version
# - pip version
# - conda version
# - environment
# - git version
# - jupyter version

# In[1]:


import sys
import os
import subprocess


# In[2]:


class SetupCheck:
  def __init__(self, name):
    self.name = name

  def check_setup(self):
    print(f"Checking setup for {self.name}")
    self.check_python()
    self.check_pip()
    self.check_conda()
    self.check_environment()
    self.check_git()
    self.check_jupyter()

  def check_python(self):
    # current python version
    print(f"Current python version: {sys.version}")

  def check_pip(self):
    # current pip version
    try:
      result = subprocess.run(['pip', '--version'], capture_output=True, text=True)
      print(f"Current pip version: {result.stdout.strip()}")
    except:
      print("🚨 pip not found")

  def check_conda(self):
    # current conda version
    try:
      result = subprocess.run(['conda', '--version'], capture_output=True, text=True)
      print(f"Current conda version: {result.stdout.strip()}")
    except:
      print("🚨 conda not found")

  def check_environment(self):
    # current environment
    try:
      env = os.environ.get('CONDA_DEFAULT_ENV', 'No conda environment')
      print(f"Current environment: {env}")
    except:
      print("🚨 Environment info not available")

  def check_git(self):
    # current git version
    try:
      result = subprocess.run(['git', '--version'], capture_output=True, text=True)
      print(f"Current git version: {result.stdout.strip()}")
    except:
      print("🚨 git not found")

  def check_jupyter(self):
    # current jupyter version
    try:
      result = subprocess.run(['jupyter', '--version'], capture_output=True, text=True)
      print(f"Current jupyter version: {result.stdout.strip()}")
    except:
      print("🚨 jupyter not found")


# In[3]:


setup_check = SetupCheck("IT2053C")
setup_check.check_setup()


# The following script converts the setup-checker.ipynb to a python script.
# 
# When I review your code on GitHub, leaving comments on a notebook can be difficult. This is why we convert the notebook to a python script, so I can leave comments on the python script on GitHub.

# In[4]:


get_ipython().system('jupyter nbconvert --to python setup-checker.ipynb')

