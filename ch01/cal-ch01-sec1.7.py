{
  "cells": [
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": ["import marimo as mo", "import matplotlib.pyplot as plt", "import numpy as np", "import pandas as pd"]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "# 第 1 章 1.7 节：函数连续性和极限简介",
        "",
        "微积分研究变化规律，也研究在何处研究变化。极限把注意力放在测试点附近的局部环境。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 连续性的想法",
        "",
        "计算机用离散点和插值近似曲线。当采样间隔足够小时，散点会看起来像平滑曲线。理想情况下，连续函数可以不离开笔尖地画完。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_x = np.linspace(-2, 2, 801)",
        "_f1 = 3 * _x**3 - _x**2 + 2 * _x - 1",
        "_f2 = np.where(_x == 0, np.nan, 1 / _x)",
        "_fig, _axes = plt.subplots(1, 3, figsize=(13, 4))",
        "_axes[0].plot(_x, _f1, color=\"#176b87\")",
        "_axes[0].set_title(\"Continuous: polynomial\")",
        "_axes[1].plot(_x, _f2, color=\"#d95f02\")",
        "_axes[1].set_ylim(-10, 10)",
        "_axes[1].set_title(\"Break at x=0: 1/x\")",
        "_step_x = np.linspace(0.01, 4, 500)",
        "_step_y = np.select([_step_x <= 1, _step_x <= 2], [7, 14], default=21)",
        "_axes[2].step(_step_x, _step_y, where=\"post\", color=\"#16805b\")",
        "_axes[2].set_yticks([0, 7, 14, 21])",
        "_axes[2].set_title(\"Jump discontinuities\")",
        "for _axis in _axes:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "从图形看，$3x^3-x^2+2x-1$ 在所示区间连续；$1/x$ 在 $x=0$ 没有定义；阶梯函数在跳跃处不连续。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 从数值观点看连续性", "", "考察 $f(x)=x^2$ 在 $x=2$ 附近的值，可以看到输入逐渐接近 2 时，输出逐渐接近 4。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_near_two = np.array([1.9, 1.99, 1.999, 2.0, 2.001, 2.01, 2.1])",
        "_near_two_data = pd.DataFrame({\"x\": _near_two, \"x^2\": _near_two**2})",
        "mo.ui.table(_near_two_data)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_windows = [(-6, 6), (-3, 3), (-1, 1), (1.9, 2.1), (1.9999, 2.0001)]",
        "_fig, _axes = plt.subplots(5, 1, figsize=(8, 10))",
        "for _axis, (_left, _right) in zip(_axes, _windows):",
        "    _values = np.linspace(_left, _right, 401)",
        "    _axis.plot(_values, _values**2, color=\"#176b87\")",
        "    _axis.scatter([2], [4], color=\"#d95f02\")",
        "    _axis.set_title(f\"x from {_left} to {_right}\")",
        "    _axis.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 函数极限和连续性的区别",
        "",
        "极限关注 $x$ 接近 $c$ 时 $f(x)$ 趋向的数值：$lim(x -> c) f(x)=L$。连续性还要求这个极限等于实际函数值：$L=f(c)$。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "def F(x):",
        "    return np.cos(x) - 2 * x**2",
        "",
        "_root_interval = np.arange(0.6, 0.7001, 0.01)",
        "_root_data = pd.DataFrame({\"x\": _root_interval, \"F(x)\": F(_root_interval)})",
        "mo.ui.table(_root_data)",
        "print({\"F(0.6)\": F(0.6), \"F(0.7)\": F(0.7)})"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "函数 $F(x)=cos(x)-2x^2$ 在 0.6 和 0.7 之间发生符号变化，因此连续性保证这一区间内存在一个零点。这是中值定律的直观应用。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 三个极限例子", "", "下面的图形分别展示可去间断、左右极限不同，以及函数值无界的情形。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_limit_x = np.linspace(-2, 6, 801)",
        "_limit_x = _limit_x[_limit_x != 3]",
        "_fig, _axes = plt.subplots(1, 3, figsize=(14, 4))",
        "_axes[0].plot(_limit_x, _limit_x + 3, color=\"#176b87\", label=\"(x²-9)/(x-3)\")",
        "_axes[0].scatter([3], [6], facecolors=\"white\", edgecolors=\"#d95f02\", s=70, zorder=3)",
        "_axes[0].set_title(\"Limit is 6, with a removable hole\")",
        "_sign_x = np.linspace(-2, 3, 501)",
        "_sign_x = _sign_x[_sign_x != 2]",
        "_axes[1].plot(_sign_x, np.where(_sign_x < 2, -1, 1), color=\"#d95f02\")",
        "_axes[1].set_title(\"|x-2|/(x-2): no two-sided limit\")",
        "_infinite_x = np.linspace(-1, 1, 801)",
        "_infinite_x = _infinite_x[_infinite_x != 0]",
        "_axes[2].plot(_infinite_x, 1 / _infinite_x**2, color=\"#16805b\")",
        "_axes[2].set_ylim(0, 40)",
        "_axes[2].set_title(\"1/x² grows without bound near 0\")",
        "for _axis in _axes:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_osc_x = np.linspace(-0.5 * np.pi, 0.5 * np.pi, 3001)",
        "_osc_x = _osc_x[_osc_x != 0]",
        "_fig, _ax = plt.subplots(figsize=(9, 4))",
        "_ax.plot(_osc_x, np.sin(1 / _osc_x), color=\"#8e44ad\")",
        "_ax.set(xlabel=\"x\", ylabel=\"sin(1/x)\", title=\"Rapid oscillation near x=0\")",
        "_ax.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    }
  ]
}
