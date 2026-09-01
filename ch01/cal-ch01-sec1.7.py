import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    return mo, np, pd, plt


@app.cell
def _(mo):
    mo.md("# 第 1 章 1.7 节：函数连续性和极限简介\n\n极限把注意力放在测试点附近的局部环境。")


@app.cell
def _(mo, np, pd, plt):
    _x = np.linspace(-2, 2, 801)
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    _axes[0].plot(_x, 3 * _x**3 - _x**2 + 2 * _x - 1, color="#176b87")
    _axes[0].set_title("Continuous polynomial")
    _x_reciprocal = _x[_x != 0]
    _axes[1].plot(_x_reciprocal, 1 / _x_reciprocal, color="#d95f02")
    _axes[1].set_ylim(-10, 10)
    _axes[1].set_title("1/x: break at 0")
    _step_x = np.linspace(0.01, 4, 500)
    _axes[2].step(_step_x, np.select([_step_x <= 1, _step_x <= 2], [7, 14], default=21), where="post", color="#16805b")
    _axes[2].set_title("Jump discontinuities")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    _near_two = np.array([1.9, 1.99, 1.999, 2, 2.001, 2.01, 2.1])
    mo.ui.table(pd.DataFrame({"x": _near_two, "x^2": _near_two**2}))


@app.cell
def __(mo):
    mo.md("## 数值观点和中值定律\n\n连续函数在符号变化的区间内至少有一个零点。")


@app.cell
def __(mo, np, pd, plt):
    def F(x):
        return np.cos(x) - 2 * x**2
    _x = np.arange(0.6, 0.7001, 0.01)
    _data = pd.DataFrame({"x": _x, "F(x)": F(_x)})
    mo.ui.table(_data)
    print({"F(0.6)": F(0.6), "F(0.7)": F(0.7)})
    _fig, _ax = plt.subplots(figsize=(8, 4))
    _plot_x = np.linspace(0, 1, 401)
    _ax.plot(_plot_x, F(_plot_x), color="#176b87", label="cos(x)-2x^2")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig


@app.cell
def __(mo):
    mo.md("## 极限例子\n\n可去间断、左右极限不同、无界增长和快速振荡说明了不同的极限行为。")


@app.cell
def __(np, plt):
    _x = np.linspace(-2, 6, 801)
    _x = _x[_x != 3]
    _fig, _axes = plt.subplots(1, 3, figsize=(14, 4))
    _axes[0].plot(_x, _x + 3, color="#176b87")
    _axes[0].scatter([3], [6], facecolors="white", edgecolors="#d95f02", s=70)
    _axes[0].set_title("(x^2-9)/(x-3), limit 6")
    _sign_x = np.linspace(-2, 3, 501)
    _sign_x = _sign_x[_sign_x != 2]
    _axes[1].plot(_sign_x, np.where(_sign_x < 2, -1, 1), color="#d95f02")
    _axes[1].set_title("|x-2|/(x-2), no limit")
    _infinite_x = np.linspace(-1, 1, 801)
    _infinite_x = _infinite_x[_infinite_x != 0]
    _axes[2].plot(_infinite_x, 1 / _infinite_x**2, color="#16805b")
    _axes[2].set_ylim(0, 40)
    _axes[2].set_title("1/x^2 near zero")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig


@app.cell
def __(mo):
    mo.md("## 振荡极限\n\n$\\sin(1/x)$ 在 $x$ 接近 0 时持续振荡，因此没有唯一极限。")


@app.cell
def __(np, plt):
    _x = np.linspace(-0.5 * np.pi, 0.5 * np.pi, 3001)
    _x = _x[_x != 0]
    _fig, _ax = plt.subplots(figsize=(9, 4))
    _ax.plot(_x, np.sin(1 / _x), color="#8e44ad")
    _ax.set_title("Rapid oscillation near zero")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig


if __name__ == "__main__":
    app.run()
