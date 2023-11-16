## Description
This part of the documentation shows some examples of how the smallangle package functions can be used

## Examples
### sin / tan
```python
>>>tan(5)
          x       tan (x)
0  0.000000  0.000000e+00
1  1.570796  1.633124e+16
2  3.141593 -1.224647e-16
3  4.712389  5.443746e+15
4  6.283185 -2.449294e-16
```
```python
>>>sin(5)
          x       sin (x)
0  0.000000  0.000000e+00
1  1.570796  1.000000e+00
2  3.141593  1.224647e-16
3  4.712389 -1.000000e+00
4  6.283185 -2.449294e-16
```

### approx
```python
>>>approx(0.01)
For an accuracy of 0.01, the sine small-angle approximation holds
up to x = 0.393
```
```python
>>>approx(0.01, tangent = True)
For an accuracy of 0.01, the tangent small-angle approximation holds
up to x = 0.307
```
```python
>>>approx(0.001, compare = True)
For an accuracy of 0.001, the sine-tangent equality approximation holds
up to x = 0.126
```