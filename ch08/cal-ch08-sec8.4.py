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
    # 第 8 章 8.4 节：密度与质心

    离散质点的质心为 $\\bar{x}=\\sum m_ix_i/\\sum m_i$。连续杆的质心为
    $$\\bar{x}=\\frac{\\int_a^b x\\delta(x)dx}{\\int_a^b\\delta(x)dx}.$$
    """)
    return


@app.cell
def _(np, plt):
    _x = np.linspace(0, 1, 501)
    _density = 15 * _x**2
    _mass = np.trapezoid(_density, _x)
    _center = np.trapezoid(_x * _density, _x) / _mass
    _fig, _ax = plt.subplots(figsize=(8, 4.5))
    _ax.plot(_x, _density, color="#176b87", label=r"$\delta(x)=15x^2$")
    _ax.axvline(_center, color="#d95f02", linestyle="--", label=f"center = {_center:.3f}")
    _ax.set(xlabel="x", ylabel="density", title="Center of mass of a nonuniform rod")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


@app.cell
def _(mo):
    mo.md("## 区域的质心\n\n均匀三角形的质心位于三个顶点平均位置；半球的质心可用水平圆盘切片近似。")
    return


if __name__ == "__main__":
    app.run()
