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
    # 第 5 章 5.1 节：用下和与上和估计距离

    速度数据可以用矩形面积估计路程。下和使用每段较小的速度，上和使用每段较大的速度。
    """)
    return


@app.cell
def _(mo):
    time = mo.ui.slider(-10, 10, value=5, step=1, label="time")
    time
    return time


@app.cell
def _(mo, np, pd, plt, time):
    _velocity = np.array([0, 5, 10, 15, 20, 25, 30])
    _dt = 1
    _lower = np.minimum(_velocity[:-1], _velocity[1:])
    _upper = np.maximum(_velocity[:-1], _velocity[1:])
    _data = pd.DataFrame({"interval": np.arange(6), "lower speed": _lower, "upper speed": _upper, "lower distance": _lower * _dt, "upper distance": _upper * _dt})
    mo.ui.table(_data)
    _x = np.linspace(0, 6, 301)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, 5 * _x, color="#176b87", label=r"$v(t)=5t$")
    _ax.bar(np.arange(6), _lower, width=1, align="edge", alpha=0.25, color="#d95f02", label="lower sum")
    _ax.bar(np.arange(6), _upper, width=1, align="edge", alpha=0.18, color="#16805b", label="upper sum")
    _ax.axvline(time.value, color="#8e44ad", linestyle="--", label=f"t = {time.value}")
    _ax.set(xlabel="time", ylabel="velocity", title="Lower and upper distance estimates")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
