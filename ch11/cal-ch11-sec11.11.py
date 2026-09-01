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
    # 第 11 章 11.11 节：阻尼振动

    线性方程 $x''+2\gamma x'+\omega_0^2x=0$ 的特征根决定运动类型：欠阻尼、临界阻尼或过阻尼。
    下面比较三种阻尼系数的响应。
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 12, 600)
    _natural = 1.0
    _responses = {
        "underdamped": np.exp(-0.12 * _time) * np.cos(0.99 * _time),
        "critical": (1 + _time) * np.exp(-_time),
        "overdamped": 1.8 * np.exp(-0.38 * _time) - 0.8 * np.exp(-2.62 * _time),
    }
    _fig, _ax = plt.subplots(figsize=(10, 4.5))
    for _name, _response in _responses.items():
        _ax.plot(_time, _response, label=_name)
    _ax.set(xlabel="time", ylabel="x(t)", title="Damped oscillator responses")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
