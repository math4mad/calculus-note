import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd

    return mo, np, pd, plt


@app.cell
def _(mo):
    mo.md("""
    # 第 4 章 4.5 节：边际成本与边际收益

    成本、收益和利润分别记为 $C(x)$、$R(x)$ 和 $P(x)=R(x)-C(x)$。
    边际成本与边际收益是 $MC=C'$ 和 $MR=R'$。
    """)
    return


@app.cell
def _(mo, np, pd, plt):
    _x = np.linspace(0, 20, 401)
    _cost = 40 + 2 * _x + 5 * np.sin(_x / 2)
    _revenue = 8 * _x
    _profit = _revenue - _cost
    _data = pd.DataFrame({"production": _x[::80], "cost": _cost[::80], "revenue": _revenue[::80], "profit": _profit[::80]})
    mo.ui.table(_data)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _cost, label="cost", color="#d95f02")
    _ax.plot(_x, _revenue, label="revenue", color="#176b87")
    _ax.plot(_x, _profit, label="profit", color="#16805b")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.set(xlabel="units", ylabel="value", title="Cost, revenue, and profit")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 割线与切线

    对 $f(x)=e^x$，割线斜率在区间缩小时趋近于导数 $f'(x)=e^x$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-1, 1, 401)
    _a, _b = 0.0, 0.8
    _slope = (np.exp(_b) - np.exp(_a)) / (_b - _a)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, np.exp(_x), color="#176b87", label=r"$e^x$")
    _ax.plot(_x, 1 + _slope * _x, "--", color="#d95f02", label="secant")
    _ax.plot(_x, 1 + _x, ":", color="#16805b", label="tangent at 0")
    _ax.scatter([_a, _b], [np.exp(_a), np.exp(_b)], color="#8e44ad")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
