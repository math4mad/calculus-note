import marimo

__generated_with = "0.17.2"
app = marimo.App(width="medium")


@app.cell
def __(mo, plt, np):
    import marimo as mo
    import matplotlib.pyplot as plt
    import numpy as np
    mo.md("# 第 1 章 1.5 节：三角函数\n\n三角函数与单位圆关系密切。单位圆上的点为 $(\\cos t,\\sin t)$。")
    _theta = np.pi / 6
    _circle = np.linspace(0, 2 * np.pi, 601)
    _arc = np.linspace(0, _theta, 101)
    _fig, _axes = plt.subplots(1, 2, figsize=(11, 4.5))
    _axes[0].plot(np.cos(_circle), np.sin(_circle), color="#176b87")
    _axes[0].plot([0, np.cos(_theta)], [0, np.sin(_theta)], color="#d95f02")
    _axes[0].plot(0.3 * np.cos(_arc), 0.3 * np.sin(_arc), color="#d95f02")
    _axes[0].annotate(r"$\theta=\pi/6$", (0.2, 0.1))
    _wave = np.linspace(-3 * np.pi, 3 * np.pi, 901)
    _axes[1].plot(_wave, np.sin(_wave), label=r"$\sin t$", color="#176b87")
    _axes[1].plot(_wave, np.cos(_wave), label=r"$\cos t$", color="#d95f02")
    _axes[1].set_ylim(-1.1, 1.1)
    _axes[1].set_title("Periodic sine and cosine")
    for _axis in _axes:
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
    _axes[0].set_aspect("equal")
    _axes[1].legend()
    _fig.tight_layout()
    _fig


@app.cell
def __(plt, np):
    mo.md("## 三角函数的变换\n\n改变振幅、周期、反射方向或垂直位置。")
    _t = np.linspace(-2 * np.pi, 2 * np.pi, 901)
    _functions = [np.sin(_t), 5 * np.sin(2 * _t), -5 * np.sin(_t / 2), 1 + 2 * np.sin(_t)]
    _labels = [r"$\sin t$", r"$5\sin(2t)$", r"$-5\sin(t/2)$", r"$1+2\sin t$"]
    _fig, _axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
    for _axis, _values, _label in zip(_axes.flat, _functions, _labels):
        _axis.plot(_t, _values, label=_label)
        _axis.axhline(0, color="#555555", linewidth=1)
        _axis.axvline(0, color="#555555", linewidth=1)
        _axis.grid(alpha=0.2)
        _axis.legend()
    _fig.tight_layout()
    _fig


if __name__ == "__main__":
    app.run()
