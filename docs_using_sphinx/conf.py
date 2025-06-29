# -- Path setup --------------------------------------------------------------

import os
import sys
sys.path.append(os.path.abspath('sphinxext'))
# 添加源码目录到Python路径
sys.path.insert(0, os.path.abspath('../../Easy-Graph'))

# -- Project information -----------------------------------------------------

project = 'EasyGraph'
copyright = '2020-2025, DataNET Group, Fudan University'
author = 'DataNET Group, Fudan University'
release = '1.4.1'

# -- General configuration ---------------------------------------------------

extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',   # 用来自动生成 API stub
    'sphinx.ext.coverage',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    # 'numpydoc',  # 暂时注释掉，避免版本冲突
]

# 自动为 autosummary 生成 stub 文件，执行 make html 前先运行一次 sphinx-autogen 或者在 CI 里直接打开
autosummary_generate = True

# 如果你的代码里 import 了但文档环境缺失的第三方库，就在这里 mock 掉
autodoc_mock_imports = [
    "torch_geometric",
    "torch",
    "torch_scatter",
    "torch_sparse", 
    "cpp_easygraph",  # 添加C++扩展模块
    "seaborn",
    "matplotlib",
    "networkx",
    "sklearn",       # 添加scikit-learn
    "pandas",        # 添加pandas
    "optuna",        # 添加optuna
    "numpy",
    "scipy",
    # 添加其他可能 import 失败的包
]

# 屏蔽一些常见的警告
suppress_warnings = [
    "autosummary.stub",    # stub file not found
    "ref.undefined",       # 未定义的标签
    "ref.duplicated",      # 重复的引用目标
    "autodoc.import",      # import 模块失败
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '*test*.rst']

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    'style_nav_header_background': 'white',
    'navigation_depth': 1,
    "navbar_end": ["navbar-icon-links"],
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/easy-graph/Easy-Graph",
            "icon": "fab fa-github",
            "type": "fontawesome",
            "attributes": {"title": "Source repository"},
        },
    ],
    "github_repo": "https://github.com/easy-graph/Easy-Graph",
}

html_static_path = ['_static']
html_logo = "logo.png"
html_title = "EasyGraph 1.4.1"
latex_engine = "xelatex"
latex_paper_size = "letter"

def setup(app):
    app.add_js_file("copybutton.js")
    app.add_css_file('my_theme.css')
