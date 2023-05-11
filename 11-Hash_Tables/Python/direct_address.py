"""
This is a Python implementation of Direct Address Table, where each position (or slot) in the table corresponds to a key in the universe U.

Author: Robert Joseph George
"""

class DirectAddressTable:
  def init(self, size):
    """
    Initializes the direct address table with a given size and sets all values to None initially.
    Args:
    - size: the size of the direct address table
    """
    self.table = [None] * size

def search(self, key):
    """
    Searches for an element with a given key in the direct address table.

    Args:
    - key: the key to be searched

    Returns:
    - the element with the given key, or None if no element is found with the key
    """
    return self.table[key]

def insert(self, x):
    """
    Inserts an element into the direct address table.

    Args:
    - x: the element to be inserted
    """
    self.table[x.key] = x

def delete(self, x):
    """
    Deletes an element from the direct address table.

    Args:
    - x: the element to be deleted
    """
    self.table[x.key] = None

class Element:
  def init(self, key, value):
    """
    Initializes an element with a given key and value.
    Args:
    - key: the key of the element
    - value: the value of the element
    """
    self.key = key
    self.value = value

def find_max_element(table):
  """
  Finds the maximum element in the given direct address table.
  Args:
  - table: the direct address table

  Returns:
  - the maximum element in the table, or None if the table is empty
  """
  max_key = None
  max_element = None
  for element in table:
      if element is not None and (max_key is None or element.key > max_key):
          max_key = element.key
          max_element = element
  return max_element

# Example
table = DirectAddressTable(10)
x = Element(key=3, value="some value")
table.insert(x)
y = table.search(3)
table.delete(x)