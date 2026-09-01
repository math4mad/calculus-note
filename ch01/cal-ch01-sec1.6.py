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
        "# 第 1 章 1.6 节：幂函数、多项式函数和有理函数",
        "",
        "幂函数的一般形式为 $f(x)=kx^p$，其中 $k$ 和 $p$ 是常数。当 $p$ 为自然数时，常见形式是 $x^n$。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_power_x = np.linspace(-2, 2, 401)",
        "_fig, _axes = plt.subplots(1, 2, figsize=(10, 4), sharex=True)",
        "for _power, _label in [(5, r\"$x^5$\"), (3, r\"$x^3$\")]:",
        "    _axes[0].plot(_power_x, _power_x**_power, label=_label)",
        "for _power, _label in [(4, r\"$x^4$\"), (2, r\"$x^2$\")]:",
        "    _axes[1].plot(_power_x, _power_x**_power, label=_label)",
        "for _axis in _axes:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.set(xlim=(-2, 2), ylim=(-10, 10))",
        "    _axis.grid(alpha=0.2)",
        "    _axis.legend()",
        "_axes[0].set_title(\"Odd powers\")",
        "_axes[1].set_title(\"Even powers\")",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 指数函数和幂函数哪个最终增长更快", "", "在相同的较大输入下，指数函数最终会远远超过固定次数的幂函数。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_growth_ranges = [np.linspace(1, 5, 200), np.linspace(1, 12, 300), np.linspace(1, 15, 350)]",
        "_fig, _axes = plt.subplots(1, 3, figsize=(12, 4))",
        "for _axis, _values in zip(_axes, _growth_ranges):",
        "    _axis.plot(_values, 2**_values, label=r\"$2^x$\", color=\"#d95f02\")",
        "    _axis.plot(_values, _values**3, label=r\"$x^3$\", color=\"#176b87\")",
        "    _axis.set_xlabel(\"x\")",
        "    _axis.grid(alpha=0.2)",
        "_axes[0].set_ylim(0, 20)",
        "_axes[1].set_ylim(0, 2000)",
        "_axes[0].legend()",
        "_fig.suptitle(\"Exponential versus power growth\")",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 多项式", "", "多项式是不同幂函数的组合，常数和直线也属于多项式。随着 $x$ 变大，最高次幂项最终主导函数图像。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_poly_ranges = [np.linspace(-4, 4, 401), np.linspace(-20, 20, 801)]",
        "_fig, _axes = plt.subplots(2, 2, figsize=(10, 7))",
        "for _column, _values in enumerate(_poly_ranges):",
        "    _axes[0, _column].plot(_values, _values**4, label=r\"$x^4$\")",
        "    _axes[0, _column].plot(_values, _values**4 - 15 * _values**2 - 15 * _values, label=r\"$x^4-15x^2-15x$\")",
        "    _axes[0, _column].set_title(\"Polynomial comparison\")",
        "    _axes[1, _column].plot(_values, _values**4, color=\"#176b87\")",
        "    _axes[1, _column].plot(_values, _values**4 - 15 * _values**2 - 15 * _values, color=\"#d95f02\")",
        "    _axes[1, _column].set_title(\"Dominant fourth-power term\")",
        "for _axis in _axes.flat:",
        "    _axis.axhline(0, color=\"#555555\", linewidth=1)",
        "    _axis.axvline(0, color=\"#555555\", linewidth=1)",
        "    _axis.grid(alpha=0.2)",
        "_axes[0, 0].legend(fontsize=8)",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 有理函数", "", "有理函数是两个函数的商。例如 $f(x)=1/(x^2+4)$ 在 $x$ 趋向正无穷或负无穷时趋近于 0，但不会等于 0；$y=0$ 是它的水平渐近线。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_rational_x = np.linspace(-10, 10, 801)",
        "_rational_y = 1 / (_rational_x**2 + 4)",
        "_fig, _ax = plt.subplots(figsize=(8, 4.5))",
        "_ax.plot(_rational_x, _rational_y, color=\"#16805b\", label=r\"$1/(x^2+4)$\")",
        "_ax.axhline(0, color=\"#555555\", linewidth=1, linestyle=\"--\", label=\"horizontal asymptote y=0\")",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set(xlabel=\"x\", ylabel=\"f(x)\", title=\"A rational function\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    }
  ]
}
