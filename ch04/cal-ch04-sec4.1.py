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
    # 第 4 章 4.1 节：一阶与二阶导数的应用

    对 $f(x)=x^3-9x^2-48x+52$，有 $f'(x)=3x^2-18x-48$、$f''(x)=6x-18$。
    一阶导数决定增减性，二阶导数决定凹凸性。
    """)
    return


@app.cell
def _(mo, np, pd):
    _critical = np.array([-2, 8])
    _values = _critical**3 - 9 * _critical**2 - 48 * _critical + 52
    mo.ui.table(pd.DataFrame({"critical x": _critical, "f(x)": _values, "f'(x)": [0, 0]}))
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-8, 12, 601)
    _f = _x**3 - 9 * _x**2 - 48 * _x + 52
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _f, color="#176b87", label=r"$f(x)$")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 有理函数与参数模型

    $g(x)=1/[x(x-1)]$ 在 $x=0,1$ 处无定义。下面用分段网格避免跨越渐近线。
    """)
    return


@app.cell
def _(mo):
    parameter = mo.ui.slider(0, 6.28, value=1.0, step=0.1, label="parameter")
    parameter
    return (parameter,)


@app.cell
def _(np, parameter, plt):
    _parts = [np.linspace(-2, -0.03, 300), np.linspace(0.03, 0.97, 300), np.linspace(1.03, 2, 300)]
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    for _values in _parts:
        _axes[0].plot(_values, 1 / (_values * (_values - 1)), color="#d95f02")
    _x = np.linspace(-2, 2, 401)
    _axes[1].plot(_x, np.sin(_x + parameter.value) + 2 * np.exp(_x), color="#16805b")
    _axes[0].set_title("1/[x(x-1)]")
    _axes[1].set_title(f"sin(x + {parameter.value:.1f}) + 2 exp(x)")
    for _axis in _axes:
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
