from ml_data_analysis import compute_average_mass, check_hemisphere, count_classes
import pytest

# Test if proper float value is returned
def test_averageDecimal():
    assert compute_average_mass([{'a' : 1.5},{'a' : 5}],'a') == 3.25

# Test for average of one value
def test_average():
    assert compute_average_mass([{'a': 1}], 'a') == 1

# Test division by zero
def test_fail():
   # initialize python exception; expecting an error
   with pytest.raises(Exception):
    assert compute_average_mass([],'') == ZeroDivisionError

# Test for Keyerror (wrong key for one dict)
def test_KeyError_():
   # initialize python exception; expecting an error KeyError
   with pytest.raises(KeyError):
    assert compute_average_mass([{27 : 2},{'1' : 1}], 1)

# Test for Keyerror (wrong key)
def test_KeyError_wrongKey():
   # initialize python exception; expecting an error KeyError
   with pytest.raises(KeyError):
    assert compute_average_mass([{27 : 2}], '1') 

# Test for ValueError (wrong value in dict)
def test_ValueError():
   # initialize python exception; expecting an error KeyError
   with pytest.raises(ValueError):
    assert compute_average_mass([{'a': '2.6y'}], 'a') 

# Test for arbitrary values
def test_HemiSuccess():
  assert check_hemisphere(2.3, 1.5)

# Test for negative and zero values
def test_HemiSuccess_NegZero():
  assert check_hemisphere(0.0, -1.5)

# Test for wrong type (non float)
def test_HemiFail():
  with pytest.raises(TypeError):
   assert check_hemisphere('2.3', 1.5)

# Test return proper value
def test_HemiSuccess_Return():
  assert check_hemisphere(2.3, 1.5) == 'Northern & Eastern'

# Test passes 
def test_CountSuccess():
  assert count_classes([{'a' : '2'}],'a')

# Test fail key error (dict does not have key 2)
def test_Count_KeyError():
  with pytest.raises(KeyError):
   assert count_classes([{}], 2)

# Test fail type error (expected list of dict NOT dict of list)
def test_Count_TypeError():
  with pytest.raises(TypeError):
   assert count_classes({[]}, '2')