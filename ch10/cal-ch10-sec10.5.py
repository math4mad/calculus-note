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
    # 第 10 章 10.5 节：Fourier 多项式

    方波可以用奇数次谐波的正弦函数近似：
    $$S_N(x)=\frac{4}{\pi}\sum_{k=0}^{N-1}\frac{\sin((2k+1)x)}{2k+1}.$$
    增加谐波数会改善大部分区间的近似，但跳跃点附近会出现 Gibbs 现象。
    """)
    return


@app.cell
def _(mo):
    harmonics = mo.ui.slider(start=1, stop=15, step=1, value=5, label="odd harmonics")
    harmonics
    return harmonics


@app.cell
def _(np, plt, harmonics):
    _x = np.linspace(-np.pi, np.pi, 1200)
    _n = harmonics.value
    _square = np.where(np.sin(_x) >= 0, 1, -1)
    _series = sum(4 / np.pi * np.sin((2 * _k + 1) * _x) / (2 * _k + 1) for _k in range(_n))
    _fig, _ax = plt.subplots(figsize=(10, 4.5))
    _ax.plot(_x, _square, color="#176b87", label="square wave")
    _ax.plot(_x, _series, color="#d95f02", label=f"Fourier approximation, N={_n}")
    _ax.set(xlabel="x", ylabel="value", title="Fourier approximation of a square wave")
    _ax.grid(alpha=0.2)
    _ax.legend()
    _fig.tight_layout()
    _fig
    return


if __name__ == "__main__":
    app.run()
