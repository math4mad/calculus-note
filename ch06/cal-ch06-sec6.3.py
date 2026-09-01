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
    # 第 6 章 6.3 节：微分方程和运动

    方程 $dy/dx=f(x)$ 的解是 $y=F(x)+C$，其中 $F'(x)=f(x)$。

    例如：

    $$\\frac{dy}{dx}=2x\\Longrightarrow y=x^2+C.$$

    若 $y(3)=5$，则 $C=-4$，得到 $y=x^2-4$。
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(-4, 4, 501)
    _constants = [-4, 0, 1, 2, 5]
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    for _constant in _constants:
        _ax.plot(_x, _x**2 + _constant, label=f"C={_constant}")
    _ax.axhline(0, color="#555555", linewidth=1)
    _ax.axvline(0, color="#555555", linewidth=1)
    _ax.set(xlabel="x", ylabel="y", ylim=(-4, 20), title="Family of solutions y = x^2 + C")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 运动方程

    取竖直向上为正方向，重力加速度向下：

    $$s(t)=-\\frac{g}{2}t^2+v_0t+s_0,\\qquad g=9.8\\,\\mathrm{m/s^2}.$$

    每一项都必须具有长度单位，这正是量纲分析的作用。
    """)
    return


if __name__ == "__main__":
    app.run()
