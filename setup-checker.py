#!/usr/bin/env python
# coding: utf-8

# # Environment Setup Checker
# 
# this notebook is used to check the environment setup of the user.
# 
# it will check the following:
# 
# - python version
# - pip version
# - conda version
# - environment
# - git version
# - jupyter version
# 

# In[21]:


import sys
import os
import subprocess
import importlib


# In[22]:


class SetupCheck:
  def __init__(self, name):
    self.name = name
    self.dependencies = []

  def check_username(self):
    # current username
    username = os.environ.get('STUDENT_USERNAME')
    print(f"👋 Hello, {username}!")

  def check_setup(self):
    print(f"Checking setup for {self.name}")
    self.check_username()
    self.check_python()
    self.check_pip()
    self.check_conda()
    self.check_environment()
    self.check_dependencies()
    self.check_git()
    self.check_current_directory_is_a_git_repository()
    self.check_jupyter()

  def check_python(self):
    # current python version
    print(f"✅ Current python version: {sys.version}")

  def check_dependencies(self):
    # current dependencies
    packages_to_check = [
        ("pandas", "pandas"),
        ("numpy", "numpy"),
        ("matplotlib", "matplotlib"),
        ("seaborn", "seaborn"),
        ("scikit-learn", "sklearn"),
        ("plotly", "plotly"),
        ("ipywidgets", "ipywidgets")
    ]

    for package_name, import_name in packages_to_check:
      if importlib.util.find_spec(import_name) is not None:
        self.dependencies.append(package_name)
      else:
        print(f"🚨 {package_name} not found")

    print(f"✅ Current dependencies: {self.dependencies}")

  def check_pip(self):
    # current pip version
    try:
      result = subprocess.run(
          ['pip', '--version'], capture_output=True, text=True)
      print(f"✅ Current pip version: {result.stdout.strip()}")
    except:
      print("🚨 pip not found")

  def check_conda(self):
    # current conda version
    try:
      result = subprocess.run(
          ['conda', '--version'], capture_output=True, text=True)
      print(f"✅ Current conda version: {result.stdout.strip()}")
    except:
      print("🚨 conda not found")

  def check_environment(self):
    # current environment
    try:
      env = os.environ.get('CONDA_DEFAULT_ENV', 'No conda environment')
      if env == self.name:
        print(f"✅ Current environment: {env}")
      else:
        print(
            f"🚨 Current environment: {env} is not the same as the expected environment: {self.__name__}")
    except:
      print("🚨 Environment info not available")

  def check_git(self):
    # current git version
    try:
      result = subprocess.run(
          ['git', '--version'], capture_output=True, text=True)
      print(f"✅ Current git version: {result.stdout.strip()}")
    except:
      print("🚨 git not found")

  def check_current_directory_is_a_git_repository(self):
    try:
      result = subprocess.run(
          ['git', 'rev-parse', '--is-inside-work-tree'], capture_output=True, text=True)
      if result.returncode == 0:
        print(f"✅ Current directory is a git repository")
      else:
        print("🚨 Current directory is not a git repository")
    except:
      print("🚨 Current directory is not a git repository")

  def check_jupyter(self):
    # current jupyter version
    try:
      result = subprocess.run(
          ['jupyter', '--version'], capture_output=True, text=True)
      print(f"✅ Current jupyter version: {result.stdout.strip()}")
    except:
      print("🚨 jupyter not found")


# In[23]:


def is_running_in_notebook():
  """
  Detect if the code is running in a Jupyter notebook environment.
  Returns True if running in notebook, False if running as script.
  """
  try:
    # Method 1: Check if IPython is available and has get_ipython
    shell = get_ipython().__class__.__name__
    if shell == 'ZMQInteractiveShell':  # Jupyter notebook
      return True
    elif shell == 'TerminalInteractiveShell':  # IPython terminal
      return False
    else:
      return False
  except NameError:
    # Method 2: Check if we're in IPython at all
    return False
  except:
    # Method 3: Check for Jupyter-specific environment variables
    return 'JPY_PARENT_PID' in os.environ


# The following script converts the setup-checker.ipynb to a python script.
# 
# When I review your code on GitHub, leaving comments on a notebook can be difficult. This is why we convert the notebook to a python script, so I can leave comments on the python script on GitHub.
# 

# In[24]:


if is_running_in_notebook():
  get_ipython().system('jupyter nbconvert --to python setup-checker.ipynb')


# In[25]:


setup_check = SetupCheck("IT2053C")
setup_check.check_setup()

