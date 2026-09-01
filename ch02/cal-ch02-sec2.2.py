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
    # 第 2 章 2.2 节：在某个点的导数

    导数定义为

    $$f'(a)=\\lim_{h\\to0}\\frac{f(a+h)-f(a)}{h}.$$

    割线斜率在 $h$ 趋近于 $0$ 时逼近切线斜率。
    """)
    return


@app.cell
def _(mo):
    endpoint = mo.ui.slider(3.2, 4.2, step=0.2, value=4.0, label="b")
    endpoint
    return endpoint


@app.cell
def _(endpoint, np, plt):
    _a = 3.0
    _b = endpoint.value
    _function = lambda value: 4**value + 16 * value
    _fa, _fb = _function(_a), _function(_b)
    _slope = (_fb - _fa) / (_b - _a)
    _x = np.linspace(2.5, 4.5, 401)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _function(_x), color="#176b87", label=r"$f(t)=4^t+16t$")
    _ax.plot(_x, _fa + _slope * (_x - _a), "--", color="#d95f02", label=f"secant slope = {_slope:.2f}")
    _ax.scatter([_a, _b], [_fa, _fb], color="#16805b", zorder=3)
    _ax.set(xlabel="t", ylabel="f(t)", title=f"Secant line from a = 3 to b = {_b:.1f}")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 局部线性近似\n\n放大曲线附近的区域，可以看到光滑曲线越来越接近直线。")
    return


@app.cell
def _(np, plt):
    _windows = [1, 0.5, 0.2, 0.1, 0.05]
    _fig, _axes = plt.subplots(1, 5, figsize=(15, 3))
    for _axis, _window in zip(_axes, _windows):
        _x = np.linspace(-_window, _window, 301)
        _axis.plot(_x, np.sin(_x), color="#176b87")
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.set(xlim=(-_window, _window), ylim=(-_window, _window), title=f"window={_window}")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## $2^x$ 的导数

    在 $x=0$ 附近，中央差分给出 $2^x$ 的导数约为 $0.693\\cdot2^x$，因此切线近似为 $y=0.693x+1$。
    """)
    return


@app.cell
def _(mo, np, pd, plt):
    _h = np.array([-0.1, -0.01, -0.001, 0.001, 0.01, 0.1])
    _quotient = (2**_h - 1) / _h
    _data = pd.DataFrame({"h": _h, "(2^h - 1) / h": _quotient})
    mo.ui.table(_data)
    _x = np.linspace(-2, 2, 401)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, 2**_x, color="#176b87", label=r"$2^x$")
    _ax.plot(_x, 0.693 * _x + 1, "--", color="#d95f02", label=r"$0.693x+1$")
    _ax.scatter([-1, 0, 1], [0.5, 1, 2], color="#16805b")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
