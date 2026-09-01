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
    # 第 11 章 11.6 节：微分方程模型

    微分方程可以描述冰层增长、终端速度和盐水混合等过程。模型的参数决定时间尺度与长期行为。
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 10, 400)
    _ice = np.sqrt(2 * 0.8 * _time)
    _velocity = 70 / 0.7 * (1 - np.exp(-0.7 * _time / 0.7))
    _concentration = 4 * np.exp(-0.18 * _time)
    _fig, _axes = plt.subplots(1, 3, figsize=(13, 4))
    _axes[0].plot(_time, _ice, color="#176b87")
    _axes[0].set(title="Ice-layer thickness", xlabel="time", ylabel="y")
    _axes[1].plot(_time, _velocity, color="#d95f02")
    _axes[1].set(title="Terminal velocity", xlabel="time", ylabel="v")
    _axes[2].plot(_time, _concentration, color="#16805b")
    _axes[2].set(title="Salt concentration", xlabel="time", ylabel="C")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
