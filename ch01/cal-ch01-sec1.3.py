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
    mo.md("""
    # 第 1 章 1.3 节：从已有函数扩展为新函数

    已知一个函数后，可以通过平移、伸缩、反射和组合得到新的函数。
    """)
    return


@app.cell
def _(np, plt):
    def piecewise_function(x):
        if x < -3:
            return 1
        if x < -1:
            return -x - 2
        if x < 1:
            return x
        if x < 3:
            return -x + 2
        return -1

    x_values = np.linspace(-5, 5, 401)
    y_values = np.array([piecewise_function(value) for value in x_values])
    _fig, _ax = plt.subplots(figsize=(7, 5))
    _ax.plot(x_values, y_values, linestyle="--", color="#176b87", label="f(x)")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.set(xlim=(-4, 4), ylim=(-3, 3), title="A piecewise function")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return x_values, y_values


@app.cell
def _(plt, x_values, y_values):
    _fig, _ax = plt.subplots(figsize=(7, 5))
    _ax.plot(x_values, y_values, linestyle="--", color="#176b87", label="f(x)")
    _ax.plot(x_values, -2 * y_values, linestyle=":", color="#222222", label="-2f(x)")
    _ax.plot(x_values, 3 * y_values, color="#d95f02", label="3f(x)")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.set(xlim=(-4, 4), ylim=(-3, 3), title="Vertical stretches and reflection")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 平移、组合与对称性")
    _x_transform = np.linspace(-4, 4, 401)
    _base = _x_transform**2
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)
    _axes[0].plot(_x_transform, _base, label=r"$x^2$")
    _axes[0].plot(_x_transform, _base + 4, label=r"$x^2+4$")
    _axes[0].set_title("Vertical translation")
    _axes[1].plot(_x_transform, _base, label=r"$x^2$")
    _axes[1].plot(_x_transform, (_x_transform - 2)**2, label=r"$(x-2)^2$")
    _axes[1].set_title("Horizontal translation")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.set(xlim=(-4, 4), ylim=(0, 8))
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo, pd):
    def f(x):
        return x**2

    def g(x):
        return x - 2

    composition_data = pd.DataFrame(
        {"expression": ["f(g(3))", "g(f(3))"], "value": [f(g(3)), g(f(3))]}
    )
    mo.ui.table(composition_data)
    return


@app.cell
def _(mo, np, plt):
    mo.md(
        """函数组合一般不满足交换律：$f(g(x))=(x-2)^2$，而 $g(f(x))=x^2-2$。

    偶函数关于 $y$ 轴对称，奇函数关于原点对称。
    """
    )


@app.cell
def _(np, plt):
    _x_symmetry = np.linspace(-2, 2, 401)
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True)
    _axes[0].plot(_x_symmetry, _x_symmetry**2, color="#176b87", label=r"$x^2$")
    _axes[0].scatter([-1, 1], [1, 1], color="#d95f02")
    _axes[0].set_title("Even function")
    _axes[1].plot(_x_symmetry, _x_symmetry**3, color="#16805b", label=r"$x^3$")
    _axes[1].scatter([-1, 1], [-1, 1], color="#d95f02")
    _axes[1].set_title("Odd function")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.set_aspect("equal")
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
