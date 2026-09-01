import marimo

__generated_with = "0.24.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md("""
    # 第 6 章 6.1 节：反导数的图形和数值特性

    如果 $F'(x)=f(x)$，那么 $F(x)+C$ 是一族反导函数。改变常数 $C$ 只会平移图像。

    例如，下面观察 $f(x)=e^{-x^2}$，并构造满足 $F(0)=0$ 的数值反导函数。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-2, 2, 1001)
    _integrand = np.exp(-_x**2)
    _dx = _x[1] - _x[0]
    _antiderivative = np.concatenate([[0], np.cumsum((_integrand[:-1] + _integrand[1:]) * _dx / 2)])
    _zero_index = np.argmin(np.abs(_x))
    _antiderivative = _antiderivative - _antiderivative[_zero_index]
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, _integrand, color="#176b87", label=r"$f(x)=e^{-x^2}$")
    _axes[1].plot(_x, _antiderivative, color="#d95f02", label=r"$F(x)=\int_0^x e^{-t^2}dt$")
    _axes[0].set_title("integrand")
    _axes[1].set_title("numerical antiderivative")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
