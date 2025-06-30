#!/usr/bin/env python3
"""
Pytest tests for verifying notebook output.
These tests read the setup-checker notebook and verify that the existing output
contains the expected pattern: a hello message with username followed by 8 checkmarks.
"""

import json
import re
import pytest
from pathlib import Path


def extract_notebook_output():
  """Extract the existing output from the notebook file."""
  # Read the notebook file
  with open('setup-checker.ipynb', 'r') as f:
    notebook = json.load(f)

  # Extract all output text from cells
  outputs = []
  for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
      for output in cell.get('outputs', []):
        if output['output_type'] == 'stream':
          # Handle both string and list outputs
          text = output['text']
          if isinstance(text, list):
            text = ''.join(text)
          outputs.append(text)
        elif output['output_type'] == 'execute_result':
          if 'data' in output and 'text/plain' in output['data']:
            text = output['data']['text/plain']
            if isinstance(text, list):
              text = ''.join(text)
            outputs.append(text)

  return '\n'.join(outputs)


@pytest.fixture
def notebook_output():
  """Fixture to provide notebook output for all tests."""
  return extract_notebook_output()


def test_notebook_file_exists():
  """Test that the notebook file exists."""
  assert Path('setup-checker.ipynb').exists(), "setup-checker.ipynb not found"


def test_notebook_output_not_empty(notebook_output):
  """Test that the notebook has output content."""
  assert notebook_output is not None, "No output text extracted from notebook"
  assert len(notebook_output.strip()) > 0, "Notebook output is empty"


def test_hello_message_with_username(notebook_output):
  """Test that the output contains a hello message with username."""
  hello_pattern = r'👋 Hello, \w+!'
  hello_match = re.search(hello_pattern, notebook_output)

  assert hello_match is not None, "Hello message with username not found"
  print(f"✅ Found hello message: {hello_match.group()}")


def test_exactly_eight_checkmarks(notebook_output):
  """Test that the output contains exactly 8 checkmarks."""
  checkmark_count = notebook_output.count('✅')

  assert checkmark_count == 8, f"Expected 8 checkmarks, found {checkmark_count}"
  print(f"✅ Found {checkmark_count} checkmarks")


def test_python_version_check(notebook_output):
  """Test that the output contains python version check."""
  pattern = r'✅ Current python version:'
  assert re.search(
      pattern, notebook_output) is not None, "Python version check not found"


def test_pip_version_check(notebook_output):
  """Test that the output contains pip version check."""
  pattern = r'✅ Current pip version:'
  assert re.search(
      pattern, notebook_output) is not None, "Pip version check not found"


def test_conda_version_check(notebook_output):
  """Test that the output contains conda version check."""
  pattern = r'✅ Current conda version:'
  assert re.search(
      pattern, notebook_output) is not None, "Conda version check not found"


def test_environment_check(notebook_output):
  """Test that the output contains environment check."""
  pattern = r'✅ Current environment:'
  assert re.search(
      pattern, notebook_output) is not None, "Environment check not found"


def test_dependencies_check(notebook_output):
  """Test that the output contains dependencies check."""
  pattern = r'✅ Current dependencies:'
  assert re.search(
      pattern, notebook_output) is not None, "Dependencies check not found"


def test_git_version_check(notebook_output):
  """Test that the output contains git version check."""
  pattern = r'✅ Current git version:'
  assert re.search(
      pattern, notebook_output) is not None, "Git version check not found"


def test_git_repository_check(notebook_output):
  """Test that the output contains git repository check."""
  pattern = r'✅ Current directory is a git repository'
  assert re.search(
      pattern, notebook_output) is not None, "Git repository check not found"


def test_jupyter_version_check(notebook_output):
  """Test that the output contains jupyter version check."""
  pattern = r'✅ Current jupyter version:'
  assert re.search(
      pattern, notebook_output) is not None, "Jupyter version check not found"


def test_all_expected_patterns_present(notebook_output):
  """Test that all expected output patterns are present."""
  expected_patterns = [
      r'✅ Current python version:',
      r'✅ Current pip version:',
      r'✅ Current conda version:',
      r'✅ Current environment:',
      r'✅ Current dependencies:',
      r'✅ Current git version:',
      r'✅ Current directory is a git repository',
      r'✅ Current jupyter version:'
  ]

  missing_patterns = []
  for pattern in expected_patterns:
    if not re.search(pattern, notebook_output):
      missing_patterns.append(pattern)

  assert len(
      missing_patterns) == 0, f"Missing expected patterns: {missing_patterns}"


def test_output_format_summary(notebook_output):
  """Test that provides a summary of the output format."""
  print("\n📋 Notebook output summary:")
  print("-" * 50)
  print(notebook_output)
  print("-" * 50)

  # This test always passes, it's just for display purposes
  assert True
