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
    # 第 5 章 5.2 节：定积分与黎曼和

    对区间 $[a,b]$ 划分为 $n$ 个小区间，左端点和右端点黎曼和分别近似定积分。
    """)
    return


@app.cell
def _(np, pd):
    def riemann_sums(a, b, n, function):
        points = np.linspace(a, b, n + 1)
        width = (b - a) / n
        left = width * np.sum(function(points[:-1]))
        right = width * np.sum(function(points[1:]))
        return points, width, left, right

    partition, width, left_sum, right_sum = riemann_sums(1, 2, 8, lambda values: 1 / values)
    sum_data = pd.DataFrame({"n": [8], "delta x": [width], "left sum": [left_sum], "right sum": [right_sum]})
    return left_sum, partition, right_sum, sum_data


@app.cell
def _(mo, sum_data):
    mo.ui.table(sum_data)
    return


@app.cell
def _(np, partition, plt):
    _x = np.linspace(1, 2, 501)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, 1 / _x, color="#176b87", label=r"$f(x)=1/x$")
    _ax.bar(partition[:-1], 1 / partition[:-1], width=partition[1] - partition[0], align="edge", alpha=0.25, color="#d95f02", label="left rectangles")
    _ax.set(xlabel="x", ylabel="f(x)", title="Left Riemann sum")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 半圆面积

    函数 $f(x)=\\sqrt{1-x^2}$ 在 $[-1,1]$ 上给出上半圆。数值积分可以逼近其面积 $\\pi/2$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-1, 1, 501)
    _y = np.sqrt(np.clip(1 - _x**2, 0, None))
    _fig, _ax = plt.subplots(figsize=(7, 4.5))
    _ax.fill_between(_x, _y, color="#16805b", alpha=0.25)
    _ax.plot(_x, _y, color="#176b87")
    _ax.set_aspect("equal")
    _ax.set(xlabel="x", ylabel="y", title="Area under the upper semicircle")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
