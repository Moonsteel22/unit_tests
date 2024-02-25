# Quadratic equation Unit Tests
### Build image
```
docker build -t test:1.0 .
```
### Run project
```
docker run test:1.0
```
### Check output
```
============================= test session starts ==============================
rootdir: /unit_tests
collecting ... collected 5 items
tests/test_a_coef.py::test_a_coef <- unit_tests\unit_tests\tests\test_a_coef.py PASSED [ 20%]
tests/test_discriminant.py::test_zero_discriminant <- unit_tests\unit_tests\tests\test_discriminant.py PASSED [ 40%]
tests/test_one_root.py::test_zero_roots <- unit_tests\tests\test_one_root.py PASSED [ 60%]
tests/test_two_roots.py::test_zero_roots <- unit_tests\tests\test_two_roots.py PASSED [ 80%]
tests/test_zero_roots.py::test_zero_roots <- unit_tests\tests\test_zero_roots.py PASSED [100%]

============================== 5 passed in 0.04s ===============================


```
