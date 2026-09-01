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
    # 第 8 章 8.3 节：极坐标表示的面积和弧长

    极坐标与直角坐标满足 $x=r\\cos\\theta$、$y=r\\sin\\theta$。
    极坐标曲线围成的面积为
    $$A=\\frac12\\int_\\alpha^\\beta r(\\theta)^2d\\theta.$$
    """)
    return


@app.cell
def _(np, plt):
    _theta = np.linspace(0, 2 * np.pi, 2001)
    _curves = [(np.ones_like(_theta), "circle"), (_theta / (2 * np.pi), "spiral"), (3 * np.sin(2 * _theta), "rose"), (3 + 2 * np.cos(_theta), "limacon")]
    _fig, _axes = plt.subplots(1, 4, figsize=(15, 4))
    for _axis, (_radius, _title) in zip(_axes, _curves):
        _axis.plot(_radius * np.cos(_theta), _radius * np.sin(_theta), color="#176b87")
        _axis.set_aspect("equal")
        _axis.set_title(_title)
        _axis.grid(alpha=0.2)
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("""
    ## 极坐标中的斜率和弧长

    $$\\frac{dy}{dx}=\\frac{dy/d\\theta}{dx/d\\theta},\\qquad
    L=\\int_a^b\\sqrt{(dx/d\\theta)^2+(dy/d\\theta)^2}d\\theta.$$
    """)
    return


if __name__ == "__main__":
    app.run()
