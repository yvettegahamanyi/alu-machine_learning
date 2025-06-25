#!/usr/bin/env python3
"""Initialize Normal"""


class Normal():
    """a class Normal that represents a normal distribution"""

    def __init__(self, data=None, mean=0., stddev=1.):
        """doc"""
        if data is None:
            if stddev <= 0:
                raise ValueError("stddev must be a positive value")
            else:
                self.stddev = float(stddev)
                self.mean = float(mean)
        else:
            if type(data) is not list:
                raise TypeError("data must be a list")
            elif len(data) < 2:
                raise ValueError("data must contain multiple values")
            else:
                self.mean = sum(data) / len(data)
                std = 0
                for i in range(len(data)):
                    std += (data[i] - self.mean) ** 2
                self.stddev = (std / len(data)) ** 0.5

    def z_score(self, x):
        """doc"""
        return (x - self.mean) / self.stddev

    def x_value(self, z):
        """doc"""
        return self.stddev * z + self.mean

    def pdf(self, x):
        """doc"""
        sdsd = (2.71828182845904523536028 **
                (-0.5 * ((x - self.mean)/self.stddev)**2))/(
            self.stddev * (2 * 3.1415926535897932384626) ** 0.5)
        return sdsd

    def cdf(self, x):
        """doc"""
        rr = (x - self.mean) / (self.stddev * (2 ** 0.5))
        trrt = (2/(3.1415926535897932384626)**0.5) * (rr - ((rr**3)/3) + (
            (rr**5)/10) - ((rr**7)/42) + ((rr**9)/216))
        return 0.5 * (1 + trrt)
