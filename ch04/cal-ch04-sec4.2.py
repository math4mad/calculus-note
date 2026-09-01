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
    # 第 4 章 4.2 节：全局极值与优化

    闭区间上的全局极值只能出现在端点或内部临界点。应当比较所有候选点的函数值。
    """)
    return


@app.cell
def _(mo, np, pd):
    _x = np.linspace(0, np.pi / 2, 1001)
    _values = _x - np.sin(2 * _x)
    _candidates = np.array([0, np.pi / 6, np.pi / 2])
    _candidate_values = _candidates - np.sin(2 * _candidates)
    mo.ui.table(pd.DataFrame({"x": _candidates, "g(x)": _candidate_values}))
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, np.pi / 2, 501)
    _y = _x - np.sin(2 * _x)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _y, color="#176b87")
    _ax.set(xlabel="x", ylabel="g(x)", title="Optimization on a closed interval")
    _ax.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    decay = mo.ui.slider(0.1, 2.0, value=0.5, step=0.1, label="b")
    decay
    return decay


@app.cell
def _(decay, np, plt):
    _t = np.linspace(0, 10, 501)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_t, _t * np.exp(-decay.value * _t), color="#d95f02")
    _axes[0].set_title(f"C(t) = t exp(-{decay.value:.1f}t)")
    _axes[1].plot(_t, np.exp(-_t) * np.cos(_t), color="#16805b")
    _axes[1].set_title("damped oscillation")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
