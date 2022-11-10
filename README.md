pyseatrials
================

<!-- WARNING: THIS FILE WAS AUTOGENERATED! DO NOT EDIT! -->

The library is a collection of functions, written in , that are useful
for estimating ship performance from sea trials data. The library is
based on ITTC [Preparation, Conduct and Analysis of Speed/Power Trials.
7.5-04-01-01.1](https://www.ittc.info/media/8370/75-04-01-011.pdf) and
is designed to make the process of estimating ships peformance easier,
faster and more reliable by packaging all the equations into a clearly
documented python library with examples and code testing for all
functions.

There full documentation is available at
https://jonnob.github.io/pyseatrials/

The library uses nbdev by fastdotai and most functions depend solely on
numpy. Most of the functions allow for vectorisation.

## N.B. This project is in early development. Function names and library structure may have breaking changes at anytime

## Install

``` sh
python -m pip install git+https://github.com/JonnoB/pyseatrials 
```

## How to use

As an example here is the
[`law_of_cosines`](https://JonnoB.github.io/pyseatrials/trig.html#law_of_cosines)
from the `pyseatrials.trig` module.

``` python
import numpy as np
```

In the first case the law of cosines is applied to a right angle
triangle, simplifying it to pythagoras theorem

``` python
law_of_cosines(3,4, np.pi/2)
```

    5.0

In the second case the law of cosines in applied to $45^\circ$ or
$\frac{\pi}{2}$

``` python
law_of_cosines(3,4, np.pi/4)
```

    2.833626166508712

# Notes

- The library attempts to use descriptive naming of the variables,
  however, this is not always possible
- The library refers to ‘ITTC’ throughout, this always refers to
  ‘7.5-04-01-01.1 Preparation, Conduct and Analysis of Speed/Power
  Trials’
- Where the equations are directly from ITTC they are marked **ITTC
  equations**: x
- The library focuses on the equations needed to accurately measure
  performance during sea trials. However, many of these equations can be
  applied at other stages of measuring ship performance, e.g. model
  performance in the a tank test.

## Some useful definations

- Tank test: a test performed at a marine testing facilty on a scale
  model of the vessel. This is used to obtain valuable performance data
  which can be scaled to better understand the real performance of the
  ship during seatrials.

# What still needs to be implemented

The following parts of ITTC need to be implemented as a minimum

- Appendix F
- Appendix J
- Images
  - Wind
  - law of cosines
  - STAWAVE-1
- test for errors, such as divide by 0

# Licence

The library is a python implementation of the ITTC library and is free
to use under an Apache 2.0 licence
