{
  "cells": [
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "import marimo as mo",
        "import matplotlib.pyplot as plt",
        "import numpy as np"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "# 第 1 章 1.5 节：三角函数",
        "",
        "三角函数与单位圆（半径为 1）关系密切。在单位圆中，角度对应的点坐标可以写成 $(\\cos t,\\sin t)$。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_theta = np.pi / 6",
        "_circle = np.linspace(0, 2 * np.pi, 601)",
        "_arc = np.linspace(0, _theta, 101)",
        "_fig, _ax = plt.subplots(figsize=(6, 6))",
        "_ax.plot(np.cos(_circle), np.sin(_circle), color=\"#176b87\")",
        "_ax.plot([0, np.cos(_theta)], [0, np.sin(_theta)], color=\"#d95f02\", linewidth=2)",
        "_ax.plot(0.3 * np.cos(_arc), 0.3 * np.sin(_arc), color=\"#d95f02\", linewidth=2)",
        "_ax.scatter([0, np.cos(_theta)], [0, np.sin(_theta)], color=\"#222222\")",
        "_ax.annotate(r\"$\\theta=\\pi/6$\", (0.22, 0.08))",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set_aspect(\"equal\")",
        "_ax.set(title=\"An angle on the unit circle\", xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))",
        "_ax.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "在单位圆中，$x=\\cos t$，$y=\\sin t$。因此当角度旋转 $2\\pi$ 后回到同一点，得到周期关系 $\\cos(t+2\\pi)=\\cos t$ 和 $\\sin(t+2\\pi)=\\sin t$。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_fig, _ax = plt.subplots(figsize=(6, 6))",
        "_ax.plot(np.cos(_circle), np.sin(_circle), color=\"#176b87\")",
        "_ax.plot([0, np.cos(_theta), np.cos(_theta), 0], [0, np.sin(_theta), 0, 0], linestyle=\"--\", color=\"#d95f02\")",
        "_ax.plot(1.1 * np.cos(_arc), 1.1 * np.sin(_arc), linestyle=\":\", color=\"#16805b\")",
        "_ax.annotate(r\"$x=\\cos t$\", (0.55, 0.1))",
        "_ax.annotate(r\"$y=\\sin t$\", (0.9, 0.35))",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set_aspect(\"equal\")",
        "_ax.set(title=\"Coordinates from the unit circle\", xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))",
        "_ax.grid(alpha=0.2)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_wave_t = np.linspace(-3 * np.pi, 3 * np.pi, 901)",
        "_fig, _ax = plt.subplots(figsize=(9, 4.5))",
        "_ax.plot(_wave_t, np.sin(_wave_t), label=r\"$\\sin t$\", color=\"#176b87\")",
        "_ax.plot(_wave_t, np.cos(_wave_t), label=r\"$\\cos t$\", color=\"#d95f02\")",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set(xlabel=\"t\", ylabel=\"value\", ylim=(-1.1, 1.1), title=\"Periodic sine and cosine functions\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## Example 1：三角函数的变换", "", "改变振幅、周期、反射方向或垂直位置，可以从 $f(t)=\\sin t$ 得到新的函数。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_transform_t = np.linspace(-2 * np.pi, 2 * np.pi, 901)",
        "_transformations = [",
        "    (np.sin(_transform_t), r\"$\\sin t$\"),",
        "    (5 * np.sin(2 * _transform_t), r\"$5\\sin(2t)$\"),",
        "    (-5 * np.sin(_transform_t / 2), r\"$-5\\sin(t/2)$\"),",
        "    (1 + 2 * np.sin(_transform_t), r\"$1+2\\sin t$\"),",
        "]",
        "_fig, _axes = plt.subplots(2, 2, figsize=(10, 7), sharex=True)",
        "for _axis, (_values, _label) in zip(_axes.flat, _transformations):",
        "    _axis.plot(_transform_t, _values, label=_label)",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.grid(alpha=0.2)",
        "    _axis.legend()",
        "_fig.suptitle(\"Transformations of the sine function\")",
        "_fig.tight_layout()",
        "_fig"
      ]
    }
  ]
}
