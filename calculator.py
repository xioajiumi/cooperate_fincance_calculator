#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : functions.py
import functions as func


class Calculator:
    """
    这个类只是一个集成作用而已，略显鸡肋，具体计算过程在functions.py
    以下参数的一般顺序：
    flow:一股现金流
    pv:现值
    fv:终值
    rate:比率
    nper:期次

    """

    def fv(self, pv, rate, nper, month=False):
        return func.fv(pv, rate, nper, month=month)

    def fv_continuous(self, pv, rate, nper):
        return func.fv_continuous(pv, rate, nper)

    def df(self, pv, fv, rate, nper=1):
        return func.df(pv, fv, rate, nper=nper)

    def pv(self, fv, rate, nper, compound=True):
        return func.pv(fv, rate, nper, compound=compound)

    def cash_flow_pv(self, flow, rate):
        return func.cash_flow_pv(flow, rate)

    def npv(self, pv, invest):
        return func.npv(pv, invest)

    def annuity_pv(self, cash_flow, rate, start_late_at=0, end_at=None):
        return func.annuity_pv(cash_flow, rate, start_late_at=0, end_at=end_at)

    def annuity_due_pv(self, cash_flow, rate, start_late_at=0, end_at=None):
        return func.annuity_due_pv(cash_flow, rate, start_late_at=start_late_at, end_at=end_at)

    def annuity_fv(self, cash_flow, rate, start_late_at=0, end_at=None):
        return func.annuity_fv(cash_flow, rate, start_late_at=start_late_at, end_at=end_at)

    def growing_annuity_pv(self, cash_flow, rate, growing_rate, start_late_at=0, end_at=None):
        return func.growing_annuity_pv(cash_flow, rate, growing_rate, start_late_at=start_late_at, end_at=end_at)

    def growing_annuity_due_pv(self, cash_flow, rate, growing_rate, start_late_at=0, end_at=None):
        return func.growing_annuity_due_pv(cash_flow, rate, growing_rate, start_late_at=start_late_at, end_at=end_at)

    def bond_pv(self, face_value, cupon_rate, discount_rate, nper):
        return func.bond_pv(face_value, cupon_rate, discount_rate, nper)

    def yield_to_maturity(self, pv, face_value, cupon_rate, nper, accuracy=1.0):
        return func.yield_to_maturity(pv, face_value, cupon_rate, nper, accuracy=accuracy)


if __name__ == "__main__":
    cal = Calculator()
