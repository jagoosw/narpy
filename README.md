# narpy - NASA AMES Reader for Python
[![DOI](https://zenodo.org/badge/338199187.svg)](https://zenodo.org/badge/latestdoi/338199187)

narpy is a simple NASA AMES file Reader for Python. There didn't seem to be any functioning libraries for opening .na or NASA AMES files in Python so this is what I ended up with. Functionality is fairly limited but gets the core needs done.

## Installation

`pip install narpy`

## Usage

``` 
$ python
>>> import narpy as na
>>> f=na.file("example.na")
>>> f["x"].data
[1,2,3,4,5,6,7,8,9]
>>> f.comment
This is an example file 
```
