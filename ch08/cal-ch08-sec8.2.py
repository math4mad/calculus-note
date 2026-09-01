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
    # 第 8 章 8.2 节：积分的几何应用

    绕 $x$ 轴旋转的体积为 $\\int_a^b\\pi f(x)^2dx$。图像弧长为
    $$\\int_a^b\\sqrt{1+(f'(x))^2}dx.$$
    参数曲线的路程使用 $\\int\\sqrt{(dx/dt)^2+(dy/dt)^2}dt$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 1, 200)
    _theta = np.linspace(0, 2 * np.pi, 120)
    _x_mesh, _theta_mesh = np.meshgrid(_x, _theta)
    _radius = np.exp(-_x_mesh)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, np.exp(-_x), color="#176b87")
    _axes[0].fill_between(_x, 0, np.exp(-_x), alpha=0.25, color="#d95f02")
    _axes[0].set_title("y = exp(-x)")
    _axes[1].plot_surface if False else None
    _axes[1].plot(_x_mesh[0], _radius[0], color="#16805b")
    _axes[1].set_title("radius profile")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    interval = mo.ui.dropdown(options={"0 to 0.5": (0, 0.5), "0.5 to 1": (0.5, 1)}, value="0 to 0.5", label="time interval")
    interval
    return interval


@app.cell
def _(interval, np, plt):
    _t = np.linspace(*interval.value, 301)
    _x, _y = np.cos(_t), np.sin(_t)
    _fig, _ax = plt.subplots(figsize=(6, 5))
    _ax.plot(_x, _y, color="#176b87")
    _ax.set_aspect("equal")
    _ax.set_title(f"Parametric particle path: {interval.value}")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
