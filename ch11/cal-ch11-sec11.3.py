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
    mo.md(r"""
    # 第 11 章 11.3 节：Euler 方法

    Euler 方法用切线斜率逐步推进：
    $$y_{k+1}=y_k+h f(t_k,y_k).$$
    步长越小，通常近似越精确，但计算量也会增加。
    """)
    return


@app.cell
def _(np, pd, plt):
    def euler(function, interval, initial, steps):
        _time = np.linspace(interval[0], interval[1], steps + 1)
        _values = np.empty(steps + 1)
        _values[0] = initial
        for _index in range(steps):
            _step = _time[_index + 1] - _time[_index]
            _values[_index + 1] = _values[_index] + _step * function(_time[_index], _values[_index])
        return _time, _values

    _time, _euler = euler(lambda t, y: y, (0, 2), 1, 10)
    _exact_time = np.linspace(0, 2, 200)
    _exact = np.exp(_exact_time)
    _table = pd.DataFrame({"t": _time, "Euler y": _euler})
    _fig, _ax = plt.subplots(figsize=(9, 4.5))
    _ax.plot(_exact_time, _exact, color="#d95f02", label="e^t")
    _ax.plot(_time, _euler, "o-", color="#176b87", label="Euler, h=0.2")
    _ax.set(xlabel="t", ylabel="y", title="Euler approximation of y' = y, y(0)=1")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    print(_table.to_string(index=False))
    _fig
    return euler, _table


if __name__ == "__main__":
    app.run()
