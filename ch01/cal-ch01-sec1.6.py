import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    return mo, np, plt


@app.cell
def _(mo):
    mo.md("# 第 1 章 1.6 节：幂函数、多项式函数和有理函数\n\n幂函数的一般形式为 $f(x)=kx^p$。")


@app.cell
def _(np, plt):
    _x = np.linspace(-2, 2, 401)
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    for _power in [5, 3]:
        _axes[0].plot(_x, _x**_power, label=f"x^{_power}")
    for _power in [4, 2]:
        _axes[1].plot(_x, _x**_power, label=f"x^{_power}")
    _axes[0].set_title("Odd powers")
    _axes[1].set_title("Even powers")
    for _axis in _axes:
        _axis.set_ylim(-10, 10)
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig


@app.cell
def _(mo):
    mo.md("## 指数函数和幂函数\n\n指数函数最终会远远超过固定次数的幂函数。")


@app.cell
def _(np, plt):
    _x = np.linspace(1, 15, 500)
    _fig, _axes = plt.subplots(1, 3, figsize=(12, 4))
    for _axis, _end in zip(_axes, [5, 12, 15]):
        _values = np.linspace(1, _end, 300)
        _axis.plot(_values, 2**_values, label="2^x", color="#d95f02")
        _axis.plot(_values, _values**3, label="x^3", color="#176b87")
        _axis.grid(alpha=0.2)
    _axes[0].set_ylim(0, 20)
    _axes[1].set_ylim(0, 2000)
    _axes[0].legend()
    _fig.tight_layout()
    _fig


@app.cell
def _(mo):
    mo.md("## 多项式和有理函数")


@app.cell
def _(np, plt):
    _x = np.linspace(-10, 10, 801)
    _fig, _axes = plt.subplots(1, 2, figsize=(10, 4))
    _axes[0].plot(_x, _x**4 - 15 * _x**2 - 15 * _x, label="polynomial")
    _axes[0].plot(_x, _x**4, label="x^4")
    _axes[1].plot(_x, 1 / (_x**2 + 4), color="#16805b", label="1/(x^2+4)")
    _axes[1].axhline(0, linestyle="--", color="#555555", label="y=0 asymptote")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig


if __name__ == "__main__":
    app.run()
