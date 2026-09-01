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
    # 第 4 章 4.8 节：参数方程与运动

    参数方程用 $x(t)$ 和 $y(t)$ 描述平面曲线。切向量为 $(x'(t),y'(t))$。
    """)
    return


@app.cell
def _(mo):
    time = mo.ui.slider(-10, 10, value=1, step=1, label="t")
    time
    return time


@app.cell
def _(mo, np, plt, time):
    _t = np.linspace(0, 2 * np.pi, 501)
    _x, _y = np.cos(_t), np.sin(_t)
    _point = (np.cos(time.value), np.sin(time.value))
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    _axes[0].plot(_x, _y, color="#176b87")
    _axes[0].scatter([_point[0]], [_point[1]], color="#d95f02")
    _axes[0].set_title("circle")
    _square = np.array([[-1, -1], [1, -1], [1, 1], [-1, 1], [-1, -1]])
    _axes[1].plot(_square[:, 0], _square[:, 1], color="#16805b")
    _axes[1].set_title("square")
    _line_t = np.linspace(-2, 2, 200)
    _axes[2].plot(_line_t**3, 2 * _line_t, color="#d95f02")
    _axes[2].set_title("x=t^3, y=2t")
    for _axis in _axes:
        _axis.set_aspect("equal")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 椭圆与李萨如曲线\n\n改变参数频率可以生成椭圆和复杂的周期轨迹。")
    return


@app.cell
def _(np, plt):
    _t = np.linspace(0, 2 * np.pi, 1001)
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    _axes[0].plot(2 * np.cos(_t), np.sin(_t), color="#176b87")
    _axes[0].set_title("ellipse")
    _axes[1].plot(np.sin(3 * _t), np.sin(2 * _t), color="#d95f02")
    _axes[1].set_title("Lissajous curve")
    for _axis in _axes:
        _axis.set_aspect("equal")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
