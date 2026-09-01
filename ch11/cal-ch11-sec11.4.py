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
    # 第 11 章 11.4 节：分离变量

    当 $y'=g(t)h(y)$ 时，可以把变量分离为
    $$\frac{dy}{h(y)}=g(t)dt.$$
    对 $y'=ky$，分离变量得到指数解 $y=y_0e^{kt}$；Newton 冷却模型则趋向环境温度。
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 8, 400)
    _growth = np.exp(0.35 * _time)
    _cooling = 22 + 78 * np.exp(-0.4 * _time)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_time, _growth, color="#176b87")
    _axes[0].set(title="y' = ky", xlabel="t", ylabel="y")
    _axes[1].plot(_time, _cooling, color="#d95f02", label="temperature")
    _axes[1].axhline(22, color="#16805b", linestyle="--", label="ambient")
    _axes[1].set(title="Newton cooling", xlabel="t", ylabel="temperature")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
