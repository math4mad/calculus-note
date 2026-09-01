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
    # 第 1 章 1.9 节：极限思想的扩展

    ## 当两个函数的轨迹几乎相似的时候

    比较

    $$
    f(x)=\\frac{x^2-x-6}{x-3},\\qquad g(x)=x+2.
    $$

    因为 $x^2-x-6=(x-3)(x+2)$，所以当 $x\\ne3$ 时，两个函数相等。
    但 $f$ 在 $x=3$ 处没有定义，因此图像中会留下一个空点。
    """)
    return


@app.cell
def _(np, plt):
    _x_left = np.linspace(-3, 2.99, 500)
    _x_right = np.linspace(3.01, 7, 400)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    for _x_values in [_x_left, _x_right]:
        _ax.plot(_x_values, _x_values + 2, color="#176b87")
    _ax.scatter([3], [5], facecolors="white", edgecolors="#d95f02", s=80, zorder=3)
    _ax.set(xlabel="x", ylabel="y", title="Equivalent graphs except at x = 3")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 夹逼定理

    对 $x\\ne0$，有

    $$
    -x^2\\le x^2\\cos(1/x)\\le x^2.
    $$

    两条边界曲线都趋近于 $0$，所以夹逼定理给出
    $\\lim_{x\\to0}x^2\\cos(1/x)=0$。
    """)
    return


@app.cell
def _(np, plt):
    _x_left = np.linspace(-0.3 * np.pi, -0.005, 2500)
    _x_right = np.linspace(0.005, 0.3 * np.pi, 2500)
    _fig, _ax = plt.subplots(figsize=(9, 4.5))
    for _x_values in [_x_left, _x_right]:
        _ax.plot(_x_values, _x_values**2 * np.cos(1 / _x_values), color="#176b87", linewidth=1, label=r"$x^2\cos(1/x)$")
        _ax.plot(_x_values, _x_values**2, color="#d95f02", linestyle="--", label=r"$x^2$")
        _ax.plot(_x_values, -_x_values**2, color="#16805b", linestyle="--", label=r"$-x^2$")
    _handles, _labels = _ax.get_legend_handles_labels()
    _ax.legend(_handles[:3], _labels[:3])
    _ax.set(xlabel="x", ylabel="y", ylim=(-0.1, 0.1), title="Squeeze theorem")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
