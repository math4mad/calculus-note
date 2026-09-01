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
    # 第 5 章 5.3 节：微积分基本定理

    若 $F'(x)=f(x)$，则

    $$\\int_a^b f(x)dx=F(b)-F(a).$$

    积分可以解释为累计变化，也可以解释为曲线与 $x$ 轴之间的有向面积。
    """)
    return


@app.cell
def _(mo):
    time = mo.ui.slider(-10, 10, value=5, step=1, label="time")
    time
    return time


@app.cell
def _(mo, np, pd, plt, time):
    _t = np.linspace(0, max(0.1, time.value), 101)
    _rate = 5 * 2**_t
    _accumulation = 5 * (2**_t - 1) / np.log(2)
    _data = pd.DataFrame({"t": _t[::20], "rate 5*2^t": _rate[::20], "accumulation": _accumulation[::20]})
    mo.ui.table(_data)
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_t, _rate, color="#176b87", label=r"$f(t)=5\cdot2^t$")
    _ax.fill_between(_t, _rate, color="#d95f02", alpha=0.2)
    _ax.set(xlabel="t", ylabel="rate", title=f"Accumulation through t = {time.value}")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 初始条件\n\n指数增长模型的初始条件决定积分常数；这里 $F(0)=5$ 表示初始数量为 $5$。")
    return


if __name__ == "__main__":
    app.run()
