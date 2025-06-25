#!/usr/bin/env python3
""" Initialize Exponential"""


class Exponential:
    """a class Exponential that represents an exponential distribution"""

    def __init__(self, data=None, lambtha=1.):
        """docs"""
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if type(data) != list:
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.data = data
            self.lambtha = len(data) / sum(data)

    def pdf(self, x):
        """docs"""
        if x < 0:
            return 0
        else:
            return self.lambtha * (2.7182818285 ** (-self.lambtha * x))

    def cdf(self, x):
        """docs"""
        if x < 0:
            return 0
        else:
            return 1 - 2.7182818285 ** (-self.lambtha * x)
