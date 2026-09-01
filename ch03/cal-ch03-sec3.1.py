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
    # 第 3 章 3.1 节：幂函数和多项式

    常数倍法则、和差法则与幂法则分别为

    $$
    \\frac{d}{dx}[cf(x)]=cf'(x),\\qquad
    \\frac{d}{dx}[f(x)\\pm g(x)]=f'(x)\\pm g'(x),\\qquad
    \\frac{d}{dx}x^n=nx^{n-1}.
    $$
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-2.5, 2.5, 501)
    _coefficients = [1, 5, 0.5, -2]
    _fig, _axes = plt.subplots(4, 1, figsize=(8, 12))
    for _axis, _coefficient in zip(_axes, _coefficients):
        _function = _coefficient * np.cos(_x + 1)
        _slope = -_coefficient * np.sin(-1.8 + 1)
        _x0 = -1.8
        _y0 = _coefficient * np.cos(_x0 + 1)
        _local_x = np.array([_x0 - 0.5, _x0 + 0.5])
        _axis.plot(_x, _function, color="#176b87", label=f"{_coefficient} cos(x + 1)")
        _axis.plot(_local_x, _y0 + _slope * ( _local_x - _x0), "--", color="#d95f02", label="tangent")
        _axis.scatter([_x0], [_y0], color="#16805b")
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 多项式、速度与加速度

    例如 $f(x)=5x^2+3x+2$ 的导数是 $f'(x)=10x+3$。
    对位移 $s(t)=-4.9t^2+5t+6$，速度与加速度分别为

    $$
    v(t)=-9.8t+5,\\qquad a(t)=-9.8.
    $$
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-3, 3, 601)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, _x**2, color="#176b87", label=r"$x^2$")
    _axes[0].plot(_x, 2 * _x, "--", color="#d95f02", label=r"$2x$")
    _axes[1].plot(_x, _x**3, color="#16805b", label=r"$x^3$")
    _axes[1].plot(_x, 3 * _x**2, "--", color="#d95f02", label=r"$3x^2$")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 切线近似与风力发电

    切线近似公式为

    $$f(x)\\approx f(a)+f'(a)(x-a).$$

    若 $P(v)=2v^3$，则 $P'(v)=6v^2$。在 $v=10$ 处，
    $P(10)=2000$、$P'(10)=600$，所以 $P(v)\\approx2000+600(v-10)$。
    """)
    return


@app.cell
def _(mo, np, pd):
    _wind_speed = np.array([9.5, 10, 10.1, 10.5, 12, 20, 50])
    _exact = 2 * _wind_speed**3
    _approximation = 2000 + 600 * (_wind_speed - 10)
    _data = pd.DataFrame({"wind speed": _wind_speed, "exact power": _exact, "linear approximation": _approximation})
    mo.ui.table(_data)
    return


if __name__ == "__main__":
    app.run()
