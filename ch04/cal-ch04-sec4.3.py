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
    # 第 4 章 4.3 节：优化与数学建模

    下面比较几何优化和有界模型。平方根曲线只在 $x\\geq0$ 上定义。
    """)
    return


@app.cell
def _(mo):
    point = mo.ui.slider(0.2, 8.8, value=2.0, step=0.2, label="a")
    amplitude = mo.ui.slider(40, 100, value=70, step=1, label="A")
    mo.hstack([point, amplitude])
    return amplitude, point


@app.cell
def _(amplitude, np, plt, point):
    _x = np.linspace(0.001, 9, 501)
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    _axes[0].plot(_x, np.sqrt(_x), color="#176b87")
    _axes[0].fill_between([0, point.value], 0, [np.sqrt(0.001), np.sqrt(point.value)], alpha=0.25, color="#d95f02")
    _axes[0].set_title("rectangle under sqrt(x)")
    _box_x = np.linspace(0.1, 10, 300)
    _axes[1].plot(_box_x, _box_x * (10 - _box_x), color="#16805b")
    _axes[1].set_title("box volume model")
    _model_x = np.linspace(0, 8, 300)
    _axes[2].plot(_model_x, amplitude.value * (1 - np.exp(-0.5 * _model_x)), color="#8e44ad")
    _axes[2].set_title(f"bounded exponential, A={amplitude.value}")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## Logistic family\n\n有界增长也可以用 logistic 函数描述，分母始终保持为正。")
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 10, 401)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    for _carrying, _rate in [(40, 0.6), (70, 0.8), (100, 1.0)]:
        _ax.plot(_x, _carrying / (1 + 9 * np.exp(-_rate * _x)), label=f"K={_carrying}, r={_rate}")
    _ax.set(xlabel="x", ylabel="population", title="Logistic models")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
