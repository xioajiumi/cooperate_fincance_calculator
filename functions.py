#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    :
# @File    : functions.py
"""
计算功能的具体实现
以下参数的一般顺序：
    flow:一股现金流
    pv:现值
    fv:终值
    rate:比率
    nper:期次

"""
import toys
import math

def annuity_factor(rate,nper):
    af=(1-1/pow(1+rate,nper))/rate
    return af
def discount_factor(rate,nper):
    df=1/pow(1+rate,nper)
    return df

def fv(pv, rate, nper):
    fv = pv * pow((1 + rate), nper)

    # round 解决精度丢失问题
    return round(fv, 3)


def fv_continuous(pv, rate, nper):
    fv = pv * (pow(math.e, rate * nper))
    return fv


def afr2efr(rate, nper=1, max=False):
    if max:
        efv = fv_continuous(1000, rate, nper=nper)
    else:
        efv = fv(1000, rate / nper, nper)
    epr = (efv - 1000) / 1000
    return round(epr, 5)


def df(pv, fv, rate, nper=1):
    return pv / fv


def pv(fv, rate, nper, compound=True):
    if compound:
        pv = fv / pow((1 + rate), nper)
        return round(pv, 6)


def cash_flow_pv(flow, rate):
    time = 1
    flow_pv = []
    for cash in flow:
        flow_pv.append(cash / pow(1 + rate, time))
        time += 1
    return sum(flow_pv)


def npv(pv, invest):
    return pv - invest


def annuity_pv(cash_flow, rate, start_late_at=0, end_at=None):
    if start_late_at:
        pv = cash_flow * (1 / (rate * pow(1 + rate, start_late_at)))
    elif end_at:
        pv = cash_flow * (1 / rate - 1 / (rate * pow(1 + rate, end_at)))
    else:
        pv = cash_flow / rate
    return round(pv, 6)


def annuity_due_pv(cash_flow, rate, start_late_at=0, end_at=None):
    pv = annuity_pv(cash_flow, rate, start_late_at=start_late_at, end_at=end_at) * (1 + rate)
    return pv


def annuity_fv(cash_flow, rate, start_late_at=0, end_at=None):
    if start_late_at:
        pv = cash_flow * (1 / (rate * pow(1 + rate, start_late_at)))
    elif end_at:
        pv = cash_flow * (1 / rate - 1 / (rate * pow(1 + rate, end_at)))
    else:
        pv = cash_flow / rate
    fv = pv * pow(1 + rate, end_at)
    return fv


def growing_annuity_pv(cash_flow, rate, growing_rate, start_late_at=0, end_at=None):
    if start_late_at:
        pv = cash_flow * (1 / rate - growing_rate) * pow(1 + growing_rate, start_late_at) \
             / pow(1 + rate, start_late_at)
    elif end_at:
        pv = cash_flow * (1 - pow(1 + growing_rate, end_at) / pow(1 + rate, end_at)) \
             / (rate - growing_rate)
    else:
        pv = cash_flow / (rate - growing_rate)
    return pv


def growing_annuity_due_pv(cash_flow, rate, growing_rate, start_late_at=0, end_at=None):
    pv = growing_annuity_pv(cash_flow, rate, growing_rate, start_late_at=start_late_at,
                           end_at=end_at) * (1 + rate)
    return pv


def bond_pv(face_value, cupon_rate, discount_rate, nper):
    cupon_pv = annuity_pv(face_value * cupon_rate, discount_rate, end_at=nper)
    face_pv = pv(face_value, discount_rate, nper)
    return round(cupon_pv + face_pv, 6)


def yield_to_maturity(pv, face_value, cupon_rate, nper, accuracy=1.0, tolerence=1000):
    # 容易出叉子，尽量少用或者是降低精度
    gap = 100
    gross_rate = 0.05
    delta = 0.001
    counter = 1
    while abs(gap) > accuracy:
        # print()
        counter += 1
        # 用精度换取性能
        if counter > tolerence: break
        gross_pv = bond_pv(face_value, cupon_rate, gross_rate, nper=nper)
        gap = round(pv - gross_pv, 8)
        # 开始求近似解
        if counter > 200 or gross_rate > 0.15 or gross_rate < -0.005:
            # 说明出问题了，可能无限循环
            if gap > 0:
                gross_rate -= delta
            else:
                gross_rate += delta
        else:
            seed = round(gap / pv, 8) / 10  # 不断改变种子的大小，是一个临时的delta
            # 在一定程度上优化性能，但可能牺牲一定的精度,但是在高精度<0.001下表现良好
            # if seed<delta:counter=200;continue;
            if gap > 0:
                gross_rate -= seed
            else:
                gross_rate += seed
        gross_rate = round(gross_rate, 9)

    return gross_rate


print(annuity_factor(0.0625/12,360))
print(cash_flow_pv([2528.28 for i in range(360)],0.04/12))

