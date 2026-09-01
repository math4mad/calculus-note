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
    # 第 1 章 1.8 节：极限思想的扩展

    ## 单侧极限

    考察函数 $f(x)=\\frac{|x-2|}{x-2}$ 在 $x=2$ 附近的行为。
    """)
    return


@app.cell
def _(np, plt):
    _x_left = np.linspace(-2, 1.999, 500)
    _x_right = np.linspace(2.001, 3, 250)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x_left, np.full_like(_x_left, -1), color="#176b87", label=r"$x<2$")
    _ax.plot(_x_right, np.full_like(_x_right, 1), color="#d95f02", label=r"$x>2$")
    _ax.scatter([2], [-1], facecolors="white", edgecolors="#176b87", s=70)
    _ax.scatter([2], [1], facecolors="white", edgecolors="#d95f02", s=70)
    _ax.set(xlim=(-2, 3), ylim=(-1.5, 1.5), xlabel="x", ylabel="f(x)")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    左极限与右极限不同，因此二侧极限不存在：

    $$
    \\lim_{x\\to2^-}f(x)=-1,
    \\qquad \\lim_{x\\to2^+}f(x)=1.
    $$
    """)
    return


@app.cell
def _(mo):
    mo.md("### 从 $x=2$ 的右侧进行计算")
    return


@app.cell
def _(mo, np, pd):
    _delta_x = np.array([0.1, 0.001, 0.0001, 0.00001, 0.000001])
    _right_data = pd.DataFrame(
        {"delta x": _delta_x, "x = 2 + delta x": 2 + _delta_x, "f(x)": np.ones_like(_delta_x)}
    )
    mo.ui.table(_right_data)
    return


@app.cell
def _(mo):
    mo.md("### 从 $x=2$ 的左侧进行计算")
    return


@app.cell
def _(mo, np, pd):
    _delta_x = np.array([0.1, 0.001, 0.0001, 0.00001, 0.000001])
    _left_data = pd.DataFrame(
        {"delta x": _delta_x, "x = 2 - delta x": 2 - _delta_x, "f(x)": -np.ones_like(_delta_x)}
    )
    mo.ui.table(_left_data)
    return


@app.cell
def _(mo):
    mo.md("""
    ## 极限和渐近线

    水平渐近行为与无穷远处的极限密切相关。下面比较 $1/x$ 与 $1/x^2$。
    对这两个函数而言，$y=0$ 是水平渐近线，$x=0$ 是垂直渐近线。
    """)
    return


@app.cell
def _(np, plt):
    _x_left = np.linspace(-2, -0.03, 500)
    _x_right = np.linspace(0.03, 2, 500)
    _fig, _axes = plt.subplots(1, 2, figsize=(12, 4.5))
    for _axis, _power, _title in zip(
        _axes, [1, 2], [r"$f(x)=1/x$", r"$f(x)=1/x^2$"]
    ):
        _axis.plot(_x_left, 1 / _x_left**_power, color="#176b87")
        _axis.plot(_x_right, 1 / _x_right**_power, color="#d95f02")
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.set(xlim=(-2, 2), ylim=(-35, 35), title=_title, xlabel="x")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 垂直渐近线和极限

    当 $x$ 接近垂直渐近线时，函数值可能变化得非常快。观察左右极限有助于描述这种局部行为。
    """)
    return


if __name__ == "__main__":
    app.run()
