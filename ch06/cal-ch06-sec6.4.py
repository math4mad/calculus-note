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
    # 第 6 章 6.4 节：微积分第二基本定理

    对连续函数，定积分可以构造反导函数：

    $$F(x)=\\int_a^x f(t)dt\\Longrightarrow F'(x)=f(x).$$
    """)
    return


@app.cell
def _(mo, np, pd):
    def riemann_sum(a, b, n, function):
        points = np.linspace(a, b, n + 1)
        width = (b - a) / n
        left = width * np.sum(function(points[:-1]))
        right = width * np.sum(function(points[1:]))
        return left, right

    _upper_limits = np.array([0.00011, 1, 2, 3])
    _rows = []
    for _upper in _upper_limits:
        _left, _right = riemann_sum(0.00001, _upper, 250, lambda values: np.sinc(values / np.pi))
        _rows.append((_upper, (_left + _right) / 2))
    _data = pd.DataFrame(_rows, columns=["x", "Si(x) approximate"])
    mo.ui.table(_data)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 正弦积分

    正弦积分可以写为

    $$Si(x)=\\int_0^x\\frac{\\sin t}{t}dt,$$

    其中 $t=0$ 处使用连续延拓值 $1$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0.001, 8, 801)
    _integrand = np.sin(_x) / _x
    _dx = _x[1] - _x[0]
    _si = np.concatenate([[0], np.cumsum((_integrand[:-1] + _integrand[1:]) * _dx / 2)])
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _si, color="#176b87", label=r"$Si(x)=\int_0^x\sin(t)/t\,dt$")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.set(xlabel="x", ylabel="Si(x)", title="Numerical sine integral")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
