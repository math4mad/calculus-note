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
    # 第 4 章 4.4 节：函数族与数学建模

    钟形函数族可以写成

    $$f(x)=e^{-(x-a)^2/b},\\qquad b>0.$$

    参数 $a$ 控制中心，参数 $b$ 控制宽度。
    """)
    return


@app.cell
def _(mo):
    center = mo.ui.dropdown(options={"-2": -2, "-1": -1, "0": 0, "1": 1, "2": 2}, value="0", label="a")
    width = mo.ui.slider(0.5, 5, value=1, step=0.5, label="b")
    mo.hstack([center, width])
    return center, width


@app.cell
def _(center, np, plt, width):
    _x = np.linspace(-5, 5, 601)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    for _a, _b in [(center.value, width.value), (0, 1), (-1, 2)]:
        _ax.plot(_x, np.exp(-(_x - _a) ** 2 / _b), label=f"a={_a}, b={_b}")
    _ax.set(xlabel="x", ylabel="f(x)", title="Bell-shaped function family")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 有界指数与 logistic 模型

    有界指数模型为 $f(x)=A(1-e^{-bx})$。logistic 模型则在增长后趋近于承载量 $K$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 501)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, 70 * (1 - np.exp(-0.5 * _x)), color="#176b87")
    _axes[0].set_title("bounded exponential")
    _axes[1].plot(_x, 70 / (1 + 9 * np.exp(-0.8 * _x)), color="#d95f02")
    _axes[1].set_title("logistic model")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
