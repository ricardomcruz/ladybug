# coding=utf-8
"""Generic data type."""
from __future__ import division

from ._base import DataTypeBase


class RValue(DataTypeBase):
    """R Value"""
    name = 'R Value'
    units = ['m2-K/W', 'h-ft2-F/Btu', 'clo']
    min = 0
    abbreviation = 'Rval'

    def _m2K_W_to_hft2F_Btu(self, value):
        return value * 5.678263337

    def _m2K_W_to_clo(self, value):
        return value / 0.155

    def _hft2F_Btu_to_m2K_W(self, value):
        return value / 5.678263337

    def _clo_to_m2K_W(self, value):
        return value * 0.155

    def to_unit(self, values, unit, from_unit):
        """Return values in a given unit given the input from_unit."""
        return self._to_unit_base('m2-K/W', values, unit, from_unit)

    def to_ip(self, values, from_unit):
        """Return values in IP given the input from_unit."""
        ip_units = ['h-ft2-F/Btu', 'clo']
        if from_unit in ip_units:
            return values, from_unit
        else:
            return self.to_unit(values, 'h-ft2-F/Btu', from_unit), 'h-ft2-F/Btu'

    def to_si(self, values, from_unit):
        """Return values in SI given the input from_unit."""
        si_units = ['m2-K/W', 'clo']
        if from_unit in si_units:
            return values, from_unit
        else:
            return self.to_unit(values, 'm2-K/W', from_unit), 'm2-K/W'

    @property
    def isRValue(self):
        """Return True."""
        return True


class ClothingInsulation(RValue):
    name = 'Clothing Insulation'
    abbreviation = 'Rclo'
    unit_descr = '0 = No Clothing, \n0.5 = T-shirt + Shorts, \n1 = 3-piece Suit'
