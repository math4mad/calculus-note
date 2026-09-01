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
    mo.md(r"""
    # 第 11 章 11.2 节：斜率场

    对方程 $y'=f(x,y)$，在每个点 $(x,y)$ 画出方向 $(1,f(x,y))$，就得到斜率场。
    解曲线沿着这些小线段前进。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-3, 3, 25)
    _y = np.linspace(-3, 3, 25)
    _xx, _yy = np.meshgrid(_x, _y)
    _slope = _yy
    _length = np.sqrt(1 + _slope**2)
    _fig, _ax = plt.subplots(figsize=(8, 6))
    _ax.quiver(_xx, _yy, 1 / _length, _slope / _length, color="#176b87", alpha=0.75)
    for _initial in [-2, -1, 1, 2]:
        _curve_x = np.linspace(-3, 3, 300)
        _ax.plot(_curve_x, _initial * np.exp(_curve_x), color="#d95f02")
    _ax.set(xlabel="x", ylabel="y", title="Direction field and solution family for y' = y")
    _ax.set_ylim(-3, 3)
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
