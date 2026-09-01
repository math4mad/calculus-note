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
    # 第 2 章 2.1 节：如何测量速度

    ## 瞬时速度

    平均变化率为 $\\frac{s(a+h)-s(a)}{h}$。当 $h$ 趋近于 $0$ 时，得到瞬时速度：

    $$
    v(a)=\\lim_{h\\to0}\\frac{s(a+h)-s(a)}{h}.
    $$

    从几何上看，这就是位置曲线在该点的切线斜率。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 2, 401)
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    for _axis, (_left, _right) in zip(_axes, [(0, 2), (1, 1.5), (1.25, 1.3)]):
        _local_x = np.linspace(_left, _right, 301)
        _axis.plot(_local_x, np.exp(_local_x), color="#176b87")
        _axis.set(xlim=(_left, _right), title=f"exp(x), [{_left}, {_right}]")
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 竖直投掷

    设初速度为 $v_0=30$，重力加速度为 $g=9.8$。物体高度为

    $$h(t)=v_0t-\\frac12gt^2.
    $$
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 6.5, 326)
    _height = 30 * _time - 0.5 * 9.8 * _time**2
    _height = np.maximum(_height, 0)
    _fig, _ax = plt.subplots(figsize=(9, 4.8))
    _ax.plot(_time, _height, color="#d95f02", label=r"$h(t)=30t-4.9t^2$")
    _sample_time = np.array([0, 1, 2, 3, 4, 5])
    _sample_height = np.maximum(30 * _sample_time - 4.9 * _sample_time**2, 0)
    _ax.scatter(_sample_time, _sample_height, color="#176b87", zorder=3)
    for _label, _x, _y in zip("ABCDEF", _sample_time, _sample_height):
        _ax.annotate(_label, (_x, _y), xytext=(5, 7), textcoords="offset points")
    _ax.set(xlabel="time (s)", ylabel="height (m)", title="Vertical projectile motion")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 数值计算瞬时速度\n\n在 $t=2$ 附近取不同的时间间隔，比较相应的割线斜率。")
    return


@app.cell
def _(mo, np, pd):
    _interval = np.array([-0.1, -0.01, -0.001, 0.001, 0.01, 0.1])
    _time = 2 + _interval
    _height = 30 * _time - 4.9 * _time**2
    _data = pd.DataFrame({"h": _interval, "time": _time, "height": _height})
    mo.ui.table(_data)
    return


if __name__ == "__main__":
    app.run()
