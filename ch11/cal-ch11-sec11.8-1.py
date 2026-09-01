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
    # 第 11 章 11.8-1 节：SIR 模型

    SIR 模型把人群分为易感者 $S$、感染者 $I$ 和移出者 $R$：
    $$S'=-\beta SI/N,\quad I'=\beta SI/N-\gamma I,\quad R'=\gamma I.$$
    下面用 Euler 方法进行离散模拟。
    """)
    return


@app.cell
def _(np, plt):
    _steps = 240
    _dt = 0.1
    _susceptible = np.empty(_steps + 1)
    _infected = np.empty(_steps + 1)
    _removed = np.empty(_steps + 1)
    _susceptible[0], _infected[0], _removed[0] = 990, 10, 0
    _beta, _gamma, _population = 0.32, 0.1, 1000
    for _index in range(_steps):
        _new_infections = _beta * _susceptible[_index] * _infected[_index] / _population
        _new_removals = _gamma * _infected[_index]
        _susceptible[_index + 1] = _susceptible[_index] - _dt * _new_infections
        _infected[_index + 1] = _infected[_index] + _dt * (_new_infections - _new_removals)
        _removed[_index + 1] = _removed[_index] + _dt * _new_removals
    _time = np.arange(_steps + 1) * _dt
    _fig, _ax = plt.subplots(figsize=(10, 4.5))
    _ax.plot(_time, _susceptible, label="S", color="#176b87")
    _ax.plot(_time, _infected, label="I", color="#d95f02")
    _ax.plot(_time, _removed, label="R", color="#16805b")
    _ax.set(xlabel="time", ylabel="people", title="SIR epidemic model")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
