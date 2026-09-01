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
    # 第 3 章 3.2 节：指数函数的导数

    指数函数的导数仍然是它本身的常数倍：

    $$
    \\frac{d}{dx}a^x=ka^x.
    $$
    """)
    return


@app.cell
def _(mo, np, pd):
    _h = np.array([-0.1, -0.01, -0.001, 0.001, 0.01, 0.1])
    _k = (2**_h - 1) / _h
    _data = pd.DataFrame({"h": _h, "(2^h - 1) / h": _k})
    mo.ui.table(_data)
    return


@app.cell
def _(mo):
    mo.md("""
    对 $g(x)=2^x$，有

    $$
    g'(x)=\\left(\\lim_{h\\to0}\\frac{2^h-1}{h}\\right)2^x
    \\approx0.693\\cdot2^x.
    $$
    """)
    return


@app.cell
def _(mo, np, pd):
    _bases = np.arange(2, 11)
    _h = 0.0001
    _k = ((1 + _h) ** (1 / _h)) * np.log(_bases) / _bases
    _data = pd.DataFrame({"base a": _bases, "estimated k": _k})
    mo.ui.table(_data)
    return


@app.cell
def _(mo, np, pd):
    _h = np.array([0.5, 0.1, 0.01, 0.001, 0.0001])
    _e_estimate = (1 + _h) ** (1 / _h)
    _data = pd.DataFrame({"h": _h, "(1+h)^(1/h)": _e_estimate})
    mo.ui.table(_data)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 自然底数 $e$

    选择使 $k=1$ 的底数，就得到自然指数函数。它的特殊性质是

    $$
    \\frac{d}{dx}e^x=e^x.
    $$
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-2, 2, 401)
    _fig, _axes = plt.subplots(1, 3, figsize=(14, 4.5))
    _plots = [
        (2**_x, 0.693 * 2**_x, r"$2^x$ and $0.693\cdot2^x$"),
        (np.exp(_x), np.exp(_x), r"$e^x$ and $(e^x)'$"),
        (3**_x, 1.1 * 3**_x, r"$3^x$ and $1.1\cdot3^x$"),
    ]
    for _axis, (_function, _derivative, _title) in zip(_axes, _plots):
        _axis.plot(_x, _function, color="#176b87", label="function")
        _axis.plot(_x, _derivative, "--", color="#d95f02", label="derivative estimate")
        _axis.set_title(_title)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
