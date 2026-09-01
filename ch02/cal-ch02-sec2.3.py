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
    # 第 2 章 2.3 节：导函数

    用附近的割线斜率估计导数：

    $$m(h,p)=\\frac{f(p+h)-f(p)}{h}.$$
    """)
    return


@app.cell
def _(np, pd):
    sample_points = np.array([-2, -1, 0, 1, 2, 3, 4, 5])
    step = 0.001
    function_values = lambda values: 4.2 * np.cos(values + 0.2)
    slopes = (function_values(sample_points + step) - function_values(sample_points)) / step
    slope_data = pd.DataFrame({"x": sample_points, "estimated f'(x)": slopes})
    return function_values, sample_points, slope_data


@app.cell
def _(mo, slope_data):
    mo.ui.table(slope_data)
    return


@app.cell
def _(function_values, np, plt, sample_points):
    _x = np.linspace(-2.5, 5.5, 601)
    _fig, _ax = plt.subplots(figsize=(9, 4.5))
    _ax.plot(_x, function_values(_x), color="#176b87", label=r"$4.2\cos(x+0.2)$")
    _ax.scatter(sample_points, function_values(sample_points), color="#d95f02", zorder=3)
    for _point in sample_points:
        _slope = (function_values(_point + 0.001) - function_values(_point)) / 0.001
        _local_x = np.array([_point - 0.35, _point + 0.35])
        _ax.plot(_local_x, function_values(_point) + _slope * (_local_x - _point), color="#16805b", linewidth=1)
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 药物浓度的变化率

    对离散数据使用前向差分，可以近似每个时间段的浓度变化率。
    """)
    return


@app.cell
def _(mo, np, pd, plt):
    _time = np.arange(0, 1.01, 0.1)
    _concentration = np.array([0.84, 0.89, 0.94, 0.98, 1.00, 1.00, 0.97, 0.90, 0.79, 0.63, 0.41])
    _rate = np.diff(_concentration) / 0.1
    _data = pd.DataFrame({"time": _time[:-1], "forward rate": _rate.round(2)})
    mo.ui.table(_data)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_time, _concentration, "o-", color="#d95f02")
    _ax.set(xlabel="time", ylabel="concentration", title="Drug concentration")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 基本导数规则

    $$
    \\frac{d}{dx}c=0,\\qquad \\frac{d}{dx}(mx+b)=m,\\qquad
    \\frac{d}{dx}x^n=nx^{n-1}.
    $$
    """)
    return


if __name__ == "__main__":
    app.run()
