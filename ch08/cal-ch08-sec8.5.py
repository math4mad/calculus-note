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
    mo.md("""
    # 第 8 章 8.5 节：积分的物理应用

    恒力做功为 $W=Fd$，变力做功为
    $$W=\\int_a^bF(x)dx.$$

    液体压力满足 $p=\\delta gh$，可通过水平切片求总力。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 0.1, 501)
    _spring_force = 8 * _x
    _spring_work = np.trapezoid(_spring_force, _x)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, _spring_force, color="#176b87", label=f"spring work = {_spring_work:.3f}")
    _axes[0].fill_between(_x, _spring_force, alpha=0.25, color="#d95f02")
    _axes[0].set_title("Hooke's law: F=8x")
    _depth = np.linspace(0, 11, 401)
    _width = 400 - (10 / 11) * _depth
    _pressure = 1000 * 9.8 * _depth
    _axes[1].plot(_width, _pressure, color="#16805b")
    _axes[1].set_title("Dam width and hydrostatic pressure")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
