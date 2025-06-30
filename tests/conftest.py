def pytest_itemcollected(item):
  """
  This function is used to clean up the whitespace and use the docstring as the test ID.
  """
  doc = item.function.__doc__
  if doc:
    # Clean up whitespace and use the docstring as the test ID
    item._nodeid = f"{item.fspath.basename}:: {doc.strip()}"
