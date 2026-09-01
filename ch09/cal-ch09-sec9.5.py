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
    # 第 9 章 9.5 节：幂级数与收敛区间

    一般幂级数写作
    $$\\sum_{n=0}^{\\infty}C_n(x-a)^n.$$

    有限部分和只能展示数值收敛行为，不能代替收敛性证明。
    """)
    return


@app.cell
def _(mo, np, pd):
    _n = np.arange(1, 16)
    _x_values = [1.4, 1.9, 2.3]
    _rows = {"n": _n}
    for _value in _x_values:
        _term = (_value - 1) ** _n / _n * (-1) ** (_n + 1)
        _rows[f"x={_value}"] = np.cumsum(_term)
    mo.ui.table(pd.DataFrame(_rows))
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 2.5, 601)
    _fig, _ax = plt.subplots(figsize=(9, 4.5))
    for _terms in [2, 5, 6, 8, 11, 14]:
        _n = np.arange(1, _terms + 1)
        _partial = np.sum(((_x[:, None] - 1) ** _n / _n) * (-1) ** (_n + 1), axis=1)
        _ax.plot(_x, _partial, label=f"{_terms} terms")
    _ax.axvline(2, color="#d95f02", linestyle="--", label="x = 2")
    _ax.set(xlabel="x", ylabel="partial sum", title="Partial sums of an alternating power series")
    _ax.set_ylim(-3, 3)
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
