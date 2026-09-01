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
    # 第 11 章 11.8-2 节：Lotka–Volterra 模型

    捕食者与猎物的数量可由
    $$u'=au-buv,\qquad v'=-cv+duv$$
    描述。相图显示两个种群之间的周期性变化。
    """)
    return


@app.cell
def _(np, plt):
    _steps, _dt = 1800, 0.02
    _prey, _predator = np.empty(_steps + 1), np.empty(_steps + 1)
    _prey[0], _predator[0] = 1.8, 1.0
    for _index in range(_steps):
        _prey[_index + 1] = _prey[_index] + _dt * (_prey[_index] - 0.6 * _prey[_index] * _predator[_index])
        _predator[_index + 1] = _predator[_index] + _dt * (-0.8 * _predator[_index] + 0.3 * _prey[_index] * _predator[_index])
    _time = np.arange(_steps + 1) * _dt
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_time, _prey, label="prey", color="#176b87")
    _axes[0].plot(_time, _predator, label="predator", color="#d95f02")
    _axes[0].set(xlabel="time", ylabel="population", title="Population cycles")
    _axes[0].legend()
    _axes[1].plot(_prey, _predator, color="#16805b")
    _axes[1].set(xlabel="prey", ylabel="predator", title="Phase plane")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
