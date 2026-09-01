{
  "cells": [
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "import marimo as mo",
        "import matplotlib.pyplot as plt",
        "import numpy as np",
        "import pandas as pd"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "# 第 1 章 1.3 节：从已有函数扩展为新函数",
        "",
        "已知一个函数后，可以通过平移、伸缩、反射和组合得到新的函数。观察这些操作，有助于理解复杂函数的性质。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 平移和拉伸方法", "", "先定义一个分段函数，再观察垂直伸缩和关于 $x$ 轴的反射。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "def piecewise_function(x):",
        "    if x < -3:",
        "        return 1",
        "    if x < -1:",
        "        return -x - 2",
        "    if x < 1:",
        "        return x",
        "    if x < 3:",
        "        return -x + 2",
        "    return -1",
        "",
        "_x = np.linspace(-5, 5, 401)",
        "_y = np.array([piecewise_function(value) for value in _x])",
        "_fig, _ax = plt.subplots(figsize=(7, 5))",
        "_ax.plot(_x, _y, linestyle=\"--\", color=\"#176b87\", label=\"f(x)\")",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set(xlim=(-4, 4), ylim=(-3, 3), title=\"A piecewise function\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_fig, _ax = plt.subplots(figsize=(7, 5))",
        "_ax.plot(_x, _y, linestyle=\"--\", color=\"#176b87\", label=\"f(x)\")",
        "_ax.plot(_x, -2 * _y, linestyle=\":\", color=\"#222222\", label=\"-2f(x)\")",
        "_ax.plot(_x, 3 * _y, color=\"#d95f02\", label=\"3f(x)\")",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set(xlim=(-4, 4), ylim=(-3, 3), title=\"Vertical stretches and reflection\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_x_transform = np.linspace(-4, 4, 401)",
        "_base = _x_transform ** 2",
        "_vertical = _base + 4",
        "_horizontal = (_x_transform - 2) ** 2",
        "_fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharey=True)",
        "_axes[0].plot(_x_transform, _base, label=r\"$x^2$\")",
        "_axes[0].plot(_x_transform, _vertical, label=r\"$x^2+4$\")",
        "_axes[0].set_title(\"Vertical translation\")",
        "_axes[1].plot(_x_transform, _base, label=r\"$x^2$\")",
        "_axes[1].plot(_x_transform, _horizontal, label=r\"$(x-2)^2$\")",
        "_axes[1].set_title(\"Horizontal translation\")",
        "for _axis in _axes:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.set(xlim=(-4, 4), ylim=(0, 8))",
        "    _axis.grid(alpha=0.2)",
        "    _axis.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 函数的组合",
        "",
        "组合函数把一个函数的输出交给另一个函数。令 $f(x)=x^2$，$g(x)=x-2$，不同的组合顺序通常会产生不同结果。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "def f(x):",
        "    return x**2",
        "",
        "def g(x):",
        "    return x - 2",
        "",
        "composition_data = pd.DataFrame({",
        "    \"expression\": [\"f(g(3))\", \"g(f(3))\"],",
        "    \"value\": [f(g(3)), g(f(3))],",
        "})",
        "mo.ui.table(composition_data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "$f(g(x))=f(x-2)=(x-2)^2$，而 $g(f(x))=g(x^2)=x^2-2$。所以一般来说，函数的组合不满足交换律。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 奇偶函数：对称性", "", "偶函数关于 $y$ 轴对称；奇函数关于原点对称。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_symmetry_x = np.linspace(-2, 2, 401)",
        "_fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True)",
        "_axes[0].plot(_symmetry_x, _symmetry_x**2, color=\"#176b87\", label=r\"$x^2$\")",
        "_axes[0].scatter([-1, 1], [1, 1], color=\"#d95f02\")",
        "_axes[0].set_title(\"Even function: y-axis symmetry\")",
        "_axes[1].plot(_symmetry_x, _symmetry_x**3, color=\"#16805b\", label=r\"$x^3$\")",
        "_axes[1].scatter([-1, 1], [-1, 1], color=\"#d95f02\")",
        "_axes[1].set_title(\"Odd function: origin symmetry\")",
        "for _axis in _axes:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.set_aspect(\"equal\")",
        "    _axis.grid(alpha=0.2)",
        "    _axis.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    }
  ]
}
