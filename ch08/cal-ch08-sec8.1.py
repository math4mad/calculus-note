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
    # 第 8 章 8.1 节：积分求面积和体积

    水平切片的宽度可以通过积分累加。三角形的宽度为 $10-2h$，半圆的宽度为 $2\\sqrt{49-h^2}$。
    旋转体的体积则由横截面积的积分给出。
    """)
    return


@app.cell
def _(mo):
    height = mo.ui.slider(0, 5, value=2.5, step=0.1, label="slice height")
    slices = mo.ui.dropdown(options={"100": 100, "250": 250, "500": 500, "1000": 1000}, value="250", label="slices")
    mo.hstack([height, slices])
    return height, slices


@app.cell
def _(height, np, plt, slices):
    _h = np.linspace(0, 5, slices.value + 1)
    _width = 10 - 2 * _h
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot([0, 5, 10], [0, 0, 0], color="#176b87")
    _axes[0].plot([0, 5, 10], [0, 5, 0], color="#176b87")
    _axes[0].axhline(height.value, color="#d95f02", linestyle="--")
    _axes[0].set_aspect("equal")
    _axes[0].set_title(f"triangle slice at h={height.value:.1f}")
    _x = np.linspace(-7, 7, 501)
    _y = np.sqrt(np.clip(49 - _x**2, 0, None))
    _axes[1].plot(_x, _y, color="#16805b")
    _axes[1].set_aspect("equal")
    _axes[1].set_title(f"semicircle, n={slices.value}")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
