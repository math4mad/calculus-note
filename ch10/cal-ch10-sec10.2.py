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
    # 第 10 章 10.2 节：Taylor 级数与二项式级数

    几何级数给出
    $$\frac{1}{1+x}=1-x+x^2-x^3+\cdots,$$
    其收敛区间为 $|x|<1$。部分和可以直接观察收敛速度与边界行为。
    """)
    return


@app.cell
def _(np, plt):
    _x_values = [-0.8, 0.5, 0.9, 1.1]
    _n = np.arange(1, 31)
    _fig, _axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
    for _axis, _x in zip(_axes.flat, _x_values):
        _partial = np.cumsum([(-_x) ** k for k in range(30)])
        _target = 1 / (1 + _x)
        _axis.plot(_n, _partial, marker=".", color="#176b87", label="partial sum")
        _axis.axhline(_target, color="#d95f02", linestyle="--", label="1/(1+x)")
        _axis.set_title(f"x = {_x}")
        _axis.grid(alpha=0.2)
        _axis.legend()
    _axes[1, 0].set_xlabel("number of terms")
    _axes[1, 1].set_xlabel("number of terms")
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
