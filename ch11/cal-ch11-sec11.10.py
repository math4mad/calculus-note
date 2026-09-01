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
    # 第 11 章 11.10 节：二阶微分方程

    自由落体满足 $s''=-g$；Hooke 定律给出简谐运动方程 $x''+\omega^2x=0$。
    初值决定振幅和相位，而角频率决定周期。
    """)
    return


@app.cell
def _(np, plt):
    _time = np.linspace(0, 12, 600)
    _position = np.cos(1.5 * _time)
    _velocity = -1.5 * np.sin(1.5 * _time)
    _fig, _ax = plt.subplots(figsize=(10, 4.5))
    _ax.plot(_time, _position, color="#176b87", label="position x(t)")
    _ax.plot(_time, _velocity, color="#d95f02", label="velocity x'(t)")
    _ax.axhline(0, color="#16805b", linewidth=0.8)
    _ax.set(xlabel="time", ylabel="value", title="Simple harmonic motion")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
