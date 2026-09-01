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
        "# 第 1 章 1.2 节：指数函数",
        "",
        "指数函数可以描述持续增长或衰减的数量。本节从人口数据和药物剂量出发，观察指数模型的结构。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 人口增长模型",
        "",
        "布基纳法索的人口数据如下。除了人口的绝对变化，也要观察相邻年份的比值。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "year = np.arange(2007, 2014)",
        "population = np.array([14.235, 14.660, 15.095, 15.540, 15.995, 16.460, 16.934])",
        "population_data = pd.DataFrame({\"year\": year, \"population\": population})",
        "population_data[\"change\"] = population_data[\"population\"].diff().fillna(0)",
        "population_data[\"ratio\"] = population_data[\"population\"].div(population_data[\"population\"].shift(1)).fillna(1)",
        "mo.ui.table(population_data)"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "相邻年份的人口比值接近 $1.029$，也就是每年大约增长 $2.9\\%$。以 2007 年为初始时刻，模型为 $P(t)=14.235(1.029)^t$，其中 $t$ 表示经过的年数。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_t_population = np.linspace(-10, 50, 601)",
        "_population_model = 14.235 * 1.029 ** _t_population",
        "_fig, _ax = plt.subplots(figsize=(8, 4.5))",
        "_ax.plot(_t_population, _population_model, color=\"#176b87\", label=r\"$P(t)=14.235(1.029)^t$\")",
        "_ax.axhline(0, color=\"#555555\", linewidth=1)",
        "_ax.axvline(0, color=\"#555555\", linewidth=1)",
        "_ax.set(xlabel=\"years since 2007\", ylabel=\"population (millions)\", title=\"Exponential population growth\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 函数的凸性",
        "",
        "人口增长模型是上凹的，也就是图像的斜率随着时间增加而增加。凸性是描述函数形状的重要特征。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 体内药物的衰减模型",
        "",
        "$f(0)=250$，$f(1)=250(0.6)$，$f(2)=250(0.6)^2$。经过 $t$ 小时后，体内药物量为 $Q=f(t)=250(0.6)^t$。每个时间段有 $40\\%$ 的药物分解。"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_t_drug = np.arange(0, 7)",
        "_drug_amount = 250 * 0.6 ** _t_drug",
        "drug_data = pd.DataFrame({\"time (hours)\": _t_drug, \"Q (mg)\": _drug_amount.round(1)})",
        "mo.ui.table(drug_data)"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_fig, _ax = plt.subplots(figsize=(8, 4.5))",
        "_ax.plot(_t_drug, _drug_amount, marker=\"o\", color=\"#d95f02\", label=r\"$Q(t)=250(0.6)^t$\")",
        "_ax.set(xlabel=\"time (hours)\", ylabel=\"Q (mg)\", title=\"Exponential drug decay\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend()",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": [
        "## 一般形式的指数函数",
        "",
        "指数函数的一般形式为 $P=P_0a^t$。$P_0$ 是初始值，$a$ 是变化因子，$t$ 是从初始时刻开始计算的时间。",
        "",
        "当 $a>1$ 时是指数增长模型；当 $0<a<1$ 时是指数衰减模型。"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {"language": "markdown"},
      "source": ["## 指数函数簇", "", "改变变化因子 $a$，可以得到一组具有不同增长或衰减速度的函数。"]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_t_growth = np.linspace(0, 7, 701)",
        "_growth_factors = [10, 5, 3, 2, 1.5]",
        "_fig, _ax = plt.subplots(figsize=(7, 5))",
        "for _factor in _growth_factors:",
        "    _ax.plot(_t_growth, _factor ** _t_growth, label=fr\"${_factor}^t$\")",
        "_ax.set(xlim=(0, 7), ylim=(0, 40), xlabel=\"t\", ylabel=\"a^t\", title=\"Exponential growth: a > 1\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend(loc=\"lower right\")",
        "_fig.tight_layout()",
        "_fig"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {"language": "mo-python"},
      "source": [
        "_t_decay = np.linspace(0, 12, 701)",
        "_decay_factors = [0.1, 0.5, 0.8, 0.9, 0.95]",
        "_fig, _ax = plt.subplots(figsize=(7, 5))",
        "for _factor in _decay_factors:",
        "    _ax.plot(_t_decay, _factor ** _t_decay, label=fr\"${_factor}^t$\")",
        "_ax.set(xlim=(0, 12), ylim=(0, 1), xlabel=\"t\", ylabel=\"a^t\", title=\"Exponential decay: 0 < a < 1\")",
        "_ax.grid(alpha=0.2)",
        "_ax.legend(loc=\"lower right\")",
        "_fig.tight_layout()",
        "_fig"
      ]
    }
  ]
}
