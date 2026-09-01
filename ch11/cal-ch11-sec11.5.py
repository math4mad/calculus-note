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
    mo.md(r"""
    # 第 11 章 11.5 节：增长与衰减模型

    连续复利和人口增长都满足 $y'=ky$，所以 $y(t)=y_0e^{kt}$。
    当 $k<0$ 时是指数衰减；Newton 冷却满足 $T(t)=T_a+(T_0-T_a)e^{-kt}$。
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 12, 500)
    _growth = 1000 * np.exp(0.12 * _time)
    _decay = 1000 * np.exp(-0.18 * _time)
    _cooling = 20 + 80 * np.exp(-0.25 * _time)
    _fig, _ax = plt.subplots(figsize=(10, 5))
    _ax.plot(_time, _growth, label="growth", color="#176b87")
    _ax.plot(_time, _decay, label="decay", color="#d95f02")
    _ax.plot(_time, _cooling, label="cooling", color="#16805b")
    _ax.set(xlabel="time", ylabel="value", title="Exponential models")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
