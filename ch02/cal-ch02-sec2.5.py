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
    # 第 2 章 2.5 节：二阶导数

    对 $f(x)=x^2$，有 $f'(x)=2x$ 和 $f''(x)=2$。二阶导数描述一阶导数变化的方向，也就是曲线的凹凸性。

    在运动问题中，速度和加速度分别是位移的一阶和二阶导数：

    $$
    v(t)=s'(t)=\\frac{dy}{dt},\\qquad a(t)=s''(t)=v'(t)=\\frac{d^2y}{dt^2}.
    $$
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-3, 3, 601)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(_x, _x**2, color="#176b87", label=r"$f(x)=x^2$")
    _axes[0].plot(_x, 2 * _x, "--", color="#d95f02", label=r"$f'(x)=2x$")
    _axes[0].set_title("Concave up: f''(x) = 2")
    _axes[1].plot(_x, -_x**2, color="#16805b", label=r"$f(x)=-x^2$")
    _axes[1].plot(_x, -2 * _x, "--", color="#d95f02", label=r"$f'(x)=-2x$")
    _axes[1].set_title("Concave down: f''(x) = -2")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    加速度也可以由速度的差商逼近：

    $$
    a(t)=v'(t)=\\lim_{h\\to0}\\frac{v(t+h)-v(t)}{h}.
    $$
    """)
    return


if __name__ == "__main__":
    app.run()
