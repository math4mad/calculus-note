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
    # 第 5 章 5.4 节：积分的性质与曲线之间的面积

    积分满足线性性质：

    $$\\int_a^b(\\alpha f+\\beta g)dx=\\alpha\\int_a^b fdx+\\beta\\int_a^b gdx.$$

    在对称区间上，奇函数的有向积分为 $0$，但几何面积应使用绝对值。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(1, 3, 501)
    _f = _x**2 - 4 * _x + 5
    _g = -_x**2 + 4 * _x - 1
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _f, color="#176b87", label=r"$f(x)=x^2-4x+5$")
    _ax.plot(_x, _g, color="#d95f02", label=r"$g(x)=-x^2+4x-1$")
    _ax.fill_between(_x, _f, _g, color="#16805b", alpha=0.25, label="area between curves")
    _ax.set(xlabel="x", ylabel="y", title="Area between curves on [1, 3]")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 正弦函数的对称性

    $\\sin(x)$ 是奇函数，因此在 $[-\\pi,\\pi]$ 上的有向积分为 $0$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-np.pi, np.pi, 501)
    _fig, _ax = plt.subplots(figsize=(8, 4))
    _ax.plot(_x, np.sin(_x), color="#176b87")
    _ax.fill_between(_x, np.sin(_x), color="#d95f02", alpha=0.2)
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.set(xlabel="x", ylabel="sin(x)", title="Odd symmetry and signed area")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
