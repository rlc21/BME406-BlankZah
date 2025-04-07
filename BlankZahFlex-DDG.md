# Final

## Setup


```python
from google.colab import drive
import sys
drive.mount('/content/drive')

nb_path = '/content/colab_libraries'
# sys.path.insert(0,nb_path)

# !pip install --target=$nb_path pyrosettacolabsetup
# !pip install --target=$nb_path py3Dmol
# !pip install --target=$nb_path nglview

# sys.path.append("/usr/local/lib/python3.9/site-packages")

import pyrosettacolabsetup; pyrosettacolabsetup.install_pyrosetta()
```

    Drive already mounted at /content/drive; to attempt to forcibly remount, call drive.mount("/content/drive", force_remount=True).
    Collecting pyrosettacolabsetup
      Using cached pyrosettacolabsetup-1.0.9-py3-none-any.whl.metadata (294 bytes)
    Using cached pyrosettacolabsetup-1.0.9-py3-none-any.whl (4.9 kB)
    Installing collected packages: pyrosettacolabsetup
    Successfully installed pyrosettacolabsetup-1.0.9
    [33mWARNING: Target directory /content/colab_libraries/pyrosettacolabsetup already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pyrosettacolabsetup-1.0.9.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0mCollecting py3Dmol
      Using cached py3Dmol-2.4.2-py2.py3-none-any.whl.metadata (1.9 kB)
    Using cached py3Dmol-2.4.2-py2.py3-none-any.whl (7.0 kB)
    Installing collected packages: py3Dmol
    Successfully installed py3Dmol-2.4.2
    [33mWARNING: Target directory /content/colab_libraries/py3Dmol-2.4.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/py3Dmol already exists. Specify --upgrade to force replacement.[0m[33m
    [0mCollecting nglview
      Using cached nglview-3.1.4-py3-none-any.whl
    Collecting ipywidgets>=8 (from nglview)
      Using cached ipywidgets-8.1.5-py3-none-any.whl.metadata (2.3 kB)
    Collecting notebook>=7 (from nglview)
      Using cached notebook-7.3.2-py3-none-any.whl.metadata (10 kB)
    Collecting jupyterlab>=3 (from nglview)
      Using cached jupyterlab-4.3.4-py3-none-any.whl.metadata (16 kB)
    Collecting jupyterlab_widgets (from nglview)
      Using cached jupyterlab_widgets-3.0.13-py3-none-any.whl.metadata (4.1 kB)
    Collecting numpy (from nglview)
      Using cached numpy-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (62 kB)
    Collecting comm>=0.1.3 (from ipywidgets>=8->nglview)
      Using cached comm-0.2.2-py3-none-any.whl.metadata (3.7 kB)
    Collecting ipython>=6.1.0 (from ipywidgets>=8->nglview)
      Using cached ipython-8.31.0-py3-none-any.whl.metadata (4.9 kB)
    Collecting traitlets>=4.3.1 (from ipywidgets>=8->nglview)
      Using cached traitlets-5.14.3-py3-none-any.whl.metadata (10 kB)
    Collecting widgetsnbextension~=4.0.12 (from ipywidgets>=8->nglview)
      Using cached widgetsnbextension-4.0.13-py3-none-any.whl.metadata (1.6 kB)
    Collecting async-lru>=1.0.0 (from jupyterlab>=3->nglview)
      Using cached async_lru-2.0.4-py3-none-any.whl.metadata (4.5 kB)
    Collecting httpx>=0.25.0 (from jupyterlab>=3->nglview)
      Using cached httpx-0.28.1-py3-none-any.whl.metadata (7.1 kB)
    Collecting ipykernel>=6.5.0 (from jupyterlab>=3->nglview)
      Using cached ipykernel-6.29.5-py3-none-any.whl.metadata (6.3 kB)
    Collecting jinja2>=3.0.3 (from jupyterlab>=3->nglview)
      Using cached jinja2-3.1.5-py3-none-any.whl.metadata (2.6 kB)
    Collecting jupyter-core (from jupyterlab>=3->nglview)
      Using cached jupyter_core-5.7.2-py3-none-any.whl.metadata (3.4 kB)
    Collecting jupyter-lsp>=2.0.0 (from jupyterlab>=3->nglview)
      Using cached jupyter_lsp-2.2.5-py3-none-any.whl.metadata (1.8 kB)
    Collecting jupyter-server<3,>=2.4.0 (from jupyterlab>=3->nglview)
      Using cached jupyter_server-2.15.0-py3-none-any.whl.metadata (8.4 kB)
    Collecting jupyterlab-server<3,>=2.27.1 (from jupyterlab>=3->nglview)
      Using cached jupyterlab_server-2.27.3-py3-none-any.whl.metadata (5.9 kB)
    Collecting notebook-shim>=0.2 (from jupyterlab>=3->nglview)
      Using cached notebook_shim-0.2.4-py3-none-any.whl.metadata (4.0 kB)
    Collecting packaging (from jupyterlab>=3->nglview)
      Using cached packaging-24.2-py3-none-any.whl.metadata (3.2 kB)
    Collecting setuptools>=40.8.0 (from jupyterlab>=3->nglview)
      Using cached setuptools-75.8.0-py3-none-any.whl.metadata (6.7 kB)
    Collecting tornado>=6.2.0 (from jupyterlab>=3->nglview)
      Using cached tornado-6.4.2-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.5 kB)
    Collecting anyio (from httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached anyio-4.8.0-py3-none-any.whl.metadata (4.6 kB)
    Collecting certifi (from httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached certifi-2024.12.14-py3-none-any.whl.metadata (2.3 kB)
    Collecting httpcore==1.* (from httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached httpcore-1.0.7-py3-none-any.whl.metadata (21 kB)
    Collecting idna (from httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached idna-3.10-py3-none-any.whl.metadata (10 kB)
    Collecting h11<0.15,>=0.13 (from httpcore==1.*->httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached h11-0.14.0-py3-none-any.whl.metadata (8.2 kB)
    Collecting debugpy>=1.6.5 (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached debugpy-1.8.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.3 kB)
    Collecting jupyter-client>=6.1.12 (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached jupyter_client-8.6.3-py3-none-any.whl.metadata (8.3 kB)
    Collecting matplotlib-inline>=0.1 (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached matplotlib_inline-0.1.7-py3-none-any.whl.metadata (3.9 kB)
    Collecting nest-asyncio (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached nest_asyncio-1.6.0-py3-none-any.whl.metadata (2.8 kB)
    Collecting psutil (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached psutil-6.1.1-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (22 kB)
    Collecting pyzmq>=24 (from ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached pyzmq-26.2.0-cp311-cp311-manylinux_2_28_x86_64.whl.metadata (6.2 kB)
    Collecting decorator (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached decorator-5.1.1-py3-none-any.whl.metadata (4.0 kB)
    Collecting jedi>=0.16 (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)
    Collecting pexpect>4.3 (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached pexpect-4.9.0-py2.py3-none-any.whl.metadata (2.5 kB)
    Collecting prompt_toolkit<3.1.0,>=3.0.41 (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached prompt_toolkit-3.0.50-py3-none-any.whl.metadata (6.6 kB)
    Collecting pygments>=2.4.0 (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached pygments-2.19.1-py3-none-any.whl.metadata (2.5 kB)
    Collecting stack_data (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached stack_data-0.6.3-py3-none-any.whl.metadata (18 kB)
    Collecting typing_extensions>=4.6 (from ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached typing_extensions-4.12.2-py3-none-any.whl.metadata (3.0 kB)
    Collecting MarkupSafe>=2.0 (from jinja2>=3.0.3->jupyterlab>=3->nglview)
      Using cached MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.0 kB)
    Collecting platformdirs>=2.5 (from jupyter-core->jupyterlab>=3->nglview)
      Using cached platformdirs-4.3.6-py3-none-any.whl.metadata (11 kB)
    Collecting argon2-cffi>=21.1 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached argon2_cffi-23.1.0-py3-none-any.whl.metadata (5.2 kB)
    Collecting jupyter-events>=0.11.0 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached jupyter_events-0.11.0-py3-none-any.whl.metadata (5.8 kB)
    Collecting jupyter-server-terminals>=0.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached jupyter_server_terminals-0.5.3-py3-none-any.whl.metadata (5.6 kB)
    Collecting nbconvert>=6.4.4 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached nbconvert-7.16.5-py3-none-any.whl.metadata (8.5 kB)
    Collecting nbformat>=5.3.0 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached nbformat-5.10.4-py3-none-any.whl.metadata (3.6 kB)
    Collecting overrides>=5.0 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached overrides-7.7.0-py3-none-any.whl.metadata (5.8 kB)
    Collecting prometheus-client>=0.9 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached prometheus_client-0.21.1-py3-none-any.whl.metadata (1.8 kB)
    Collecting send2trash>=1.8.2 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached Send2Trash-1.8.3-py3-none-any.whl.metadata (4.0 kB)
    Collecting terminado>=0.8.3 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached terminado-0.18.1-py3-none-any.whl.metadata (5.8 kB)
    Collecting websocket-client>=1.7 (from jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached websocket_client-1.8.0-py3-none-any.whl.metadata (8.0 kB)
    Collecting babel>=2.10 (from jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached babel-2.16.0-py3-none-any.whl.metadata (1.5 kB)
    Collecting json5>=0.9.0 (from jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached json5-0.10.0-py3-none-any.whl.metadata (34 kB)
    Collecting jsonschema>=4.18.0 (from jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached jsonschema-4.23.0-py3-none-any.whl.metadata (7.9 kB)
    Collecting requests>=2.31 (from jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached requests-2.32.3-py3-none-any.whl.metadata (4.6 kB)
    Collecting sniffio>=1.1 (from anyio->httpx>=0.25.0->jupyterlab>=3->nglview)
      Using cached sniffio-1.3.1-py3-none-any.whl.metadata (3.9 kB)
    Collecting argon2-cffi-bindings (from argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached argon2_cffi_bindings-21.2.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (6.7 kB)
    Collecting parso<0.9.0,>=0.8.4 (from jedi>=0.16->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached parso-0.8.4-py2.py3-none-any.whl.metadata (7.7 kB)
    Collecting attrs>=22.2.0 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached attrs-24.3.0-py3-none-any.whl.metadata (11 kB)
    Collecting jsonschema-specifications>=2023.03.6 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached jsonschema_specifications-2024.10.1-py3-none-any.whl.metadata (3.0 kB)
    Collecting referencing>=0.28.4 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached referencing-0.36.1-py3-none-any.whl.metadata (2.8 kB)
    Collecting rpds-py>=0.7.1 (from jsonschema>=4.18.0->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached rpds_py-0.22.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (4.2 kB)
    Collecting python-dateutil>=2.8.2 (from jupyter-client>=6.1.12->ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl.metadata (8.4 kB)
    Collecting python-json-logger>=2.0.4 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached python_json_logger-3.2.1-py3-none-any.whl.metadata (4.1 kB)
    Collecting pyyaml>=5.3 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (2.1 kB)
    Collecting rfc3339-validator (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl.metadata (1.5 kB)
    Collecting rfc3986-validator>=0.1.1 (from jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl.metadata (1.7 kB)
    Collecting beautifulsoup4 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached beautifulsoup4-4.12.3-py3-none-any.whl.metadata (3.8 kB)
    Collecting bleach!=5.0.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached bleach-6.2.0-py3-none-any.whl.metadata (30 kB)
    Collecting defusedxml (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached defusedxml-0.7.1-py2.py3-none-any.whl.metadata (32 kB)
    Collecting jupyterlab-pygments (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl.metadata (4.4 kB)
    Collecting mistune<4,>=2.0.3 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached mistune-3.1.0-py3-none-any.whl.metadata (1.7 kB)
    Collecting nbclient>=0.5.0 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached nbclient-0.10.2-py3-none-any.whl.metadata (8.3 kB)
    Collecting pandocfilters>=1.4.1 (from nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached pandocfilters-1.5.1-py2.py3-none-any.whl.metadata (9.0 kB)
    Collecting fastjsonschema>=2.15 (from nbformat>=5.3.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached fastjsonschema-2.21.1-py3-none-any.whl.metadata (2.2 kB)
    Collecting ptyprocess>=0.5 (from pexpect>4.3->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached ptyprocess-0.7.0-py2.py3-none-any.whl.metadata (1.3 kB)
    Collecting wcwidth (from prompt_toolkit<3.1.0,>=3.0.41->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached wcwidth-0.2.13-py2.py3-none-any.whl.metadata (14 kB)
    Collecting charset-normalizer<4,>=2 (from requests>=2.31->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (35 kB)
    Collecting urllib3<3,>=1.21.1 (from requests>=2.31->jupyterlab-server<3,>=2.27.1->jupyterlab>=3->nglview)
      Using cached urllib3-2.3.0-py3-none-any.whl.metadata (6.5 kB)
    Collecting executing>=1.2.0 (from stack_data->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached executing-2.1.0-py2.py3-none-any.whl.metadata (8.9 kB)
    Collecting asttokens>=2.1.0 (from stack_data->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached asttokens-3.0.0-py3-none-any.whl.metadata (4.7 kB)
    Collecting pure-eval (from stack_data->ipython>=6.1.0->ipywidgets>=8->nglview)
      Using cached pure_eval-0.2.3-py3-none-any.whl.metadata (6.3 kB)
    Collecting webencodings (from bleach!=5.0.0->bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached webencodings-0.5.1-py2.py3-none-any.whl.metadata (2.1 kB)
    Collecting tinycss2<1.5,>=1.1.0 (from bleach[css]!=5.0.0->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached tinycss2-1.4.0-py3-none-any.whl.metadata (3.0 kB)
    Collecting fqdn (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached fqdn-1.5.1-py3-none-any.whl.metadata (1.4 kB)
    Collecting isoduration (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached isoduration-20.11.0-py3-none-any.whl.metadata (5.7 kB)
    Collecting jsonpointer>1.13 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached jsonpointer-3.0.0-py2.py3-none-any.whl.metadata (2.3 kB)
    Collecting uri-template (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached uri_template-1.3.0-py3-none-any.whl.metadata (8.8 kB)
    Collecting webcolors>=24.6.0 (from jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached webcolors-24.11.1-py3-none-any.whl.metadata (2.2 kB)
    Collecting six>=1.5 (from python-dateutil>=2.8.2->jupyter-client>=6.1.12->ipykernel>=6.5.0->jupyterlab>=3->nglview)
      Using cached six-1.17.0-py2.py3-none-any.whl.metadata (1.7 kB)
    Collecting cffi>=1.0.1 (from argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (1.5 kB)
    Collecting soupsieve>1.2 (from beautifulsoup4->nbconvert>=6.4.4->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached soupsieve-2.6-py3-none-any.whl.metadata (4.6 kB)
    Collecting pycparser (from cffi>=1.0.1->argon2-cffi-bindings->argon2-cffi>=21.1->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached pycparser-2.22-py3-none-any.whl.metadata (943 bytes)
    Collecting arrow>=0.15.0 (from isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached arrow-1.3.0-py3-none-any.whl.metadata (7.5 kB)
    Collecting types-python-dateutil>=2.8.10 (from arrow>=0.15.0->isoduration->jsonschema[format-nongpl]>=4.18.0->jupyter-events>=0.11.0->jupyter-server<3,>=2.4.0->jupyterlab>=3->nglview)
      Using cached types_python_dateutil-2.9.0.20241206-py3-none-any.whl.metadata (2.1 kB)
    Using cached ipywidgets-8.1.5-py3-none-any.whl (139 kB)
    Using cached jupyterlab-4.3.4-py3-none-any.whl (11.7 MB)
    Using cached jupyterlab_widgets-3.0.13-py3-none-any.whl (214 kB)
    Using cached notebook-7.3.2-py3-none-any.whl (13.2 MB)
    Using cached numpy-2.2.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (16.4 MB)
    Using cached async_lru-2.0.4-py3-none-any.whl (6.1 kB)
    Using cached comm-0.2.2-py3-none-any.whl (7.2 kB)
    Using cached httpx-0.28.1-py3-none-any.whl (73 kB)
    Using cached httpcore-1.0.7-py3-none-any.whl (78 kB)
    Using cached ipykernel-6.29.5-py3-none-any.whl (117 kB)
    Using cached ipython-8.31.0-py3-none-any.whl (821 kB)
    Using cached jinja2-3.1.5-py3-none-any.whl (134 kB)
    Using cached jupyter_core-5.7.2-py3-none-any.whl (28 kB)
    Using cached jupyter_lsp-2.2.5-py3-none-any.whl (69 kB)
    Using cached jupyter_server-2.15.0-py3-none-any.whl (385 kB)
    Using cached jupyterlab_server-2.27.3-py3-none-any.whl (59 kB)
    Using cached notebook_shim-0.2.4-py3-none-any.whl (13 kB)
    Using cached packaging-24.2-py3-none-any.whl (65 kB)
    Using cached setuptools-75.8.0-py3-none-any.whl (1.2 MB)
    Using cached tornado-6.4.2-cp38-abi3-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (437 kB)
    Using cached traitlets-5.14.3-py3-none-any.whl (85 kB)
    Using cached widgetsnbextension-4.0.13-py3-none-any.whl (2.3 MB)
    Using cached anyio-4.8.0-py3-none-any.whl (96 kB)
    Using cached argon2_cffi-23.1.0-py3-none-any.whl (15 kB)
    Using cached babel-2.16.0-py3-none-any.whl (9.6 MB)
    Using cached debugpy-1.8.12-cp311-cp311-manylinux_2_5_x86_64.manylinux1_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (3.1 MB)
    Using cached idna-3.10-py3-none-any.whl (70 kB)
    Using cached jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)
    Using cached json5-0.10.0-py3-none-any.whl (34 kB)
    Using cached jsonschema-4.23.0-py3-none-any.whl (88 kB)
    Using cached jupyter_client-8.6.3-py3-none-any.whl (106 kB)
    Using cached jupyter_events-0.11.0-py3-none-any.whl (19 kB)
    Using cached jupyter_server_terminals-0.5.3-py3-none-any.whl (13 kB)
    Using cached MarkupSafe-3.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (23 kB)
    Using cached matplotlib_inline-0.1.7-py3-none-any.whl (9.9 kB)
    Using cached nbconvert-7.16.5-py3-none-any.whl (258 kB)
    Using cached nbformat-5.10.4-py3-none-any.whl (78 kB)
    Using cached overrides-7.7.0-py3-none-any.whl (17 kB)
    Using cached pexpect-4.9.0-py2.py3-none-any.whl (63 kB)
    Using cached platformdirs-4.3.6-py3-none-any.whl (18 kB)
    Using cached prometheus_client-0.21.1-py3-none-any.whl (54 kB)
    Using cached prompt_toolkit-3.0.50-py3-none-any.whl (387 kB)
    Using cached pygments-2.19.1-py3-none-any.whl (1.2 MB)
    Using cached pyzmq-26.2.0-cp311-cp311-manylinux_2_28_x86_64.whl (869 kB)
    Using cached requests-2.32.3-py3-none-any.whl (64 kB)
    Using cached certifi-2024.12.14-py3-none-any.whl (164 kB)
    Using cached Send2Trash-1.8.3-py3-none-any.whl (18 kB)
    Using cached terminado-0.18.1-py3-none-any.whl (14 kB)
    Using cached typing_extensions-4.12.2-py3-none-any.whl (37 kB)
    Using cached websocket_client-1.8.0-py3-none-any.whl (58 kB)
    Using cached decorator-5.1.1-py3-none-any.whl (9.1 kB)
    Using cached nest_asyncio-1.6.0-py3-none-any.whl (5.2 kB)
    Using cached psutil-6.1.1-cp36-abi3-manylinux_2_12_x86_64.manylinux2010_x86_64.manylinux_2_17_x86_64.manylinux2014_x86_64.whl (287 kB)
    Using cached stack_data-0.6.3-py3-none-any.whl (24 kB)
    Using cached asttokens-3.0.0-py3-none-any.whl (26 kB)
    Using cached attrs-24.3.0-py3-none-any.whl (63 kB)
    Using cached bleach-6.2.0-py3-none-any.whl (163 kB)
    Using cached charset_normalizer-3.4.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (143 kB)
    Using cached executing-2.1.0-py2.py3-none-any.whl (25 kB)
    Using cached fastjsonschema-2.21.1-py3-none-any.whl (23 kB)
    Using cached h11-0.14.0-py3-none-any.whl (58 kB)
    Using cached jsonschema_specifications-2024.10.1-py3-none-any.whl (18 kB)
    Using cached mistune-3.1.0-py3-none-any.whl (53 kB)
    Using cached nbclient-0.10.2-py3-none-any.whl (25 kB)
    Using cached pandocfilters-1.5.1-py2.py3-none-any.whl (8.7 kB)
    Using cached parso-0.8.4-py2.py3-none-any.whl (103 kB)
    Using cached ptyprocess-0.7.0-py2.py3-none-any.whl (13 kB)
    Using cached python_dateutil-2.9.0.post0-py2.py3-none-any.whl (229 kB)
    Using cached python_json_logger-3.2.1-py3-none-any.whl (14 kB)
    Using cached PyYAML-6.0.2-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (762 kB)
    Using cached referencing-0.36.1-py3-none-any.whl (26 kB)
    Using cached rfc3986_validator-0.1.1-py2.py3-none-any.whl (4.2 kB)
    Using cached rpds_py-0.22.3-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (381 kB)
    Using cached sniffio-1.3.1-py3-none-any.whl (10 kB)
    Using cached urllib3-2.3.0-py3-none-any.whl (128 kB)
    Using cached argon2_cffi_bindings-21.2.0-cp36-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (86 kB)
    Using cached beautifulsoup4-4.12.3-py3-none-any.whl (147 kB)
    Using cached defusedxml-0.7.1-py2.py3-none-any.whl (25 kB)
    Using cached jupyterlab_pygments-0.3.0-py3-none-any.whl (15 kB)
    Using cached pure_eval-0.2.3-py3-none-any.whl (11 kB)
    Using cached rfc3339_validator-0.1.4-py2.py3-none-any.whl (3.5 kB)
    Using cached wcwidth-0.2.13-py2.py3-none-any.whl (34 kB)
    Using cached cffi-1.17.1-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (467 kB)
    Using cached jsonpointer-3.0.0-py2.py3-none-any.whl (7.6 kB)
    Using cached six-1.17.0-py2.py3-none-any.whl (11 kB)
    Using cached soupsieve-2.6-py3-none-any.whl (36 kB)
    Using cached tinycss2-1.4.0-py3-none-any.whl (26 kB)
    Using cached webcolors-24.11.1-py3-none-any.whl (14 kB)
    Using cached webencodings-0.5.1-py2.py3-none-any.whl (11 kB)
    Using cached fqdn-1.5.1-py3-none-any.whl (9.1 kB)
    Using cached isoduration-20.11.0-py3-none-any.whl (11 kB)
    Using cached uri_template-1.3.0-py3-none-any.whl (11 kB)
    Using cached arrow-1.3.0-py3-none-any.whl (66 kB)
    Using cached pycparser-2.22-py3-none-any.whl (117 kB)
    Using cached types_python_dateutil-2.9.0.20241206-py3-none-any.whl (14 kB)
    Installing collected packages: webencodings, wcwidth, pure-eval, ptyprocess, fastjsonschema, widgetsnbextension, websocket-client, webcolors, urllib3, uri-template, typing_extensions, types-python-dateutil, traitlets, tornado, tinycss2, soupsieve, sniffio, six, setuptools, send2trash, rpds-py, rfc3986-validator, pyzmq, pyyaml, python-json-logger, pygments, pycparser, psutil, prompt_toolkit, prometheus-client, platformdirs, pexpect, parso, pandocfilters, packaging, overrides, numpy, nest-asyncio, mistune, MarkupSafe, jupyterlab_widgets, jupyterlab-pygments, jsonpointer, json5, idna, h11, fqdn, executing, defusedxml, decorator, debugpy, charset-normalizer, certifi, bleach, babel, attrs, async-lru, asttokens, terminado, stack_data, rfc3339-validator, requests, referencing, python-dateutil, matplotlib-inline, jupyter-core, jinja2, jedi, httpcore, comm, cffi, beautifulsoup4, anyio, jupyter-server-terminals, jupyter-client, jsonschema-specifications, ipython, httpx, arrow, argon2-cffi-bindings, jsonschema, isoduration, ipywidgets, ipykernel, argon2-cffi, nbformat, nbclient, jupyter-events, nbconvert, jupyter-server, notebook-shim, jupyterlab-server, jupyter-lsp, jupyterlab, notebook, nglview
    [31mERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
    google-colab 1.0.0 requires ipykernel==5.5.6, but you have ipykernel 6.29.5 which is incompatible.
    google-colab 1.0.0 requires ipython==7.34.0, but you have ipython 8.31.0 which is incompatible.
    google-colab 1.0.0 requires notebook==6.5.5, but you have notebook 7.3.2 which is incompatible.
    google-colab 1.0.0 requires tornado==6.3.3, but you have tornado 6.4.2 which is incompatible.
    langchain 0.3.14 requires numpy<2,>=1.22.4; python_version < "3.12", but you have numpy 2.2.2 which is incompatible.
    moviepy 1.0.3 requires decorator<5.0,>=4.0.2, but you have decorator 5.1.1 which is incompatible.
    numba 0.60.0 requires numpy<2.1,>=1.22, but you have numpy 2.2.2 which is incompatible.
    gensim 4.3.3 requires numpy<2.0,>=1.18.5, but you have numpy 2.2.2 which is incompatible.
    cupy-cuda12x 12.2.0 requires numpy<1.27,>=1.20, but you have numpy 2.2.2 which is incompatible.
    pytensor 2.26.4 requires numpy<2,>=1.17.0, but you have numpy 2.2.2 which is incompatible.
    tensorflow 2.17.1 requires numpy<2.0.0,>=1.23.5; python_version <= "3.11", but you have numpy 2.2.2 which is incompatible.
    thinc 8.2.5 requires numpy<2.0.0,>=1.19.0; python_version >= "3.9", but you have numpy 2.2.2 which is incompatible.[0m[31m
    [0mSuccessfully installed MarkupSafe-3.0.2 anyio-4.8.0 argon2-cffi-23.1.0 argon2-cffi-bindings-21.2.0 arrow-1.3.0 asttokens-3.0.0 async-lru-2.0.4 attrs-24.3.0 babel-2.16.0 beautifulsoup4-4.12.3 bleach-6.2.0 certifi-2024.12.14 cffi-1.17.1 charset-normalizer-3.4.1 comm-0.2.2 debugpy-1.8.12 decorator-5.1.1 defusedxml-0.7.1 executing-2.1.0 fastjsonschema-2.21.1 fqdn-1.5.1 h11-0.14.0 httpcore-1.0.7 httpx-0.28.1 idna-3.10 ipykernel-6.29.5 ipython-8.31.0 ipywidgets-8.1.5 isoduration-20.11.0 jedi-0.19.2 jinja2-3.1.5 json5-0.10.0 jsonpointer-3.0.0 jsonschema-4.23.0 jsonschema-specifications-2024.10.1 jupyter-client-8.6.3 jupyter-core-5.7.2 jupyter-events-0.11.0 jupyter-lsp-2.2.5 jupyter-server-2.15.0 jupyter-server-terminals-0.5.3 jupyterlab-4.3.4 jupyterlab-pygments-0.3.0 jupyterlab-server-2.27.3 jupyterlab_widgets-3.0.13 matplotlib-inline-0.1.7 mistune-3.1.0 nbclient-0.10.2 nbconvert-7.16.5 nbformat-5.10.4 nest-asyncio-1.6.0 nglview-3.1.4 notebook-7.3.2 notebook-shim-0.2.4 numpy-2.2.2 overrides-7.7.0 packaging-24.2 pandocfilters-1.5.1 parso-0.8.4 pexpect-4.9.0 platformdirs-4.3.6 prometheus-client-0.21.1 prompt_toolkit-3.0.50 psutil-6.1.1 ptyprocess-0.7.0 pure-eval-0.2.3 pycparser-2.22 pygments-2.19.1 python-dateutil-2.9.0.post0 python-json-logger-3.2.1 pyyaml-6.0.2 pyzmq-26.2.0 referencing-0.36.1 requests-2.32.3 rfc3339-validator-0.1.4 rfc3986-validator-0.1.1 rpds-py-0.22.3 send2trash-1.8.3 setuptools-75.8.0 six-1.17.0 sniffio-1.3.1 soupsieve-2.6 stack_data-0.6.3 terminado-0.18.1 tinycss2-1.4.0 tornado-6.4.2 traitlets-5.14.3 types-python-dateutil-2.9.0.20241206 typing_extensions-4.12.2 uri-template-1.3.0 urllib3-2.3.0 wcwidth-0.2.13 webcolors-24.11.1 webencodings-0.5.1 websocket-client-1.8.0 widgetsnbextension-4.0.13
    [33mWARNING: Target directory /content/colab_libraries/python_json_logger-3.2.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pure_eval already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jedi already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/charset_normalizer-3.4.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonschema_specifications already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/webencodings already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/tinycss2 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/h11-0.14.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/debugpy already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/stack_data already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/stack_data-0.6.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/attrs already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbformat-5.10.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/notebook already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/isoduration already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_lsp already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/Send2Trash-1.8.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/bleach-6.2.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nest_asyncio.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/_yaml already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_server_terminals already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_client-8.6.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/requests already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonschema already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipykernel already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/anyio already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbclient-0.10.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/referencing already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/prompt_toolkit already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_server already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/six.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/json5 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/numpy already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/babel already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/defusedxml-0.7.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/httpx already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/soupsieve-2.6.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/asttokens already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_events-0.11.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/numpy-2.2.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/MarkupSafe-3.0.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rpds already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/argon2_cffi_bindings-21.2.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/uri_template already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/yaml already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/psutil already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/comm already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/fastjsonschema already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pure_eval-0.2.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/cffi-1.17.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/_distutils_hack already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/_argon2_cffi_bindings already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pygments already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/arrow-1.3.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/widgetsnbextension already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/overrides already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipykernel-6.29.5.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonschema-4.23.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/send2trash already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbclient already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_core already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab-4.3.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/referencing-0.36.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pandocfilters.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/soupsieve already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/python_dateutil-2.9.0.post0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/traitlets-5.14.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/httpx-0.28.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipykernel_launcher.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/matplotlib_inline-0.1.7.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pycparser already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/async_lru already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_server-2.27.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/asttokens-3.0.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rpds_py-0.22.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rfc3986_validator.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/matplotlib_inline already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/fastjsonschema-2.21.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_pygments-0.3.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/notebook_shim already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/mistune already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/attr already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonpointer.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/bs4 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_server already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/certifi already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/tornado already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ptyprocess already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/traitlets already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/fqdn already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/requests-2.32.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/uri_template-1.3.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/typing_extensions.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/certifi-2024.12.14.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ptyprocess-0.7.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/async_lru-2.0.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/prometheus_client-0.21.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/prometheus_client already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/zmq already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbconvert-7.16.5.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/argon2 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jinja2-3.1.5.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/websocket already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/setuptools already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_client already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/debugpy-1.8.12.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/h11 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/notebook-7.3.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_widgets already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/wcwidth-0.2.13.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_pygments already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/terminado-0.18.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jedi-0.19.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pyzmq.libs already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipywidgets already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/terminado already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nglview-3.1.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/psutil-6.1.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/httpcore already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/comm-0.2.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/argon2_cffi-23.1.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pythonjsonlogger already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/urllib3 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_server-2.15.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/urllib3-2.3.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/websocket_client-1.8.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/dateutil already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rfc3339_validator.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/wcwidth already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/platformdirs-4.3.6.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/platformdirs already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_core-5.7.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/__pycache__ already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/fqdn-1.5.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/types_python_dateutil-2.9.0.20241206.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/typing_extensions-4.12.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/prompt_toolkit-3.0.50.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/beautifulsoup4-4.12.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/six-1.17.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/tinycss2-1.4.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pandocfilters-1.5.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/sniffio-1.3.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rfc3986_validator-0.1.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/widgetsnbextension-4.0.13.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pycparser-2.22.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/decorator.py already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/webencodings-0.5.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/bleach already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/idna-3.10.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/cffi already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/numpy.libs already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonschema_specifications-2024.10.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipython-8.31.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/overrides-7.7.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/executing already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_server_terminals-0.5.3.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/PyYAML-6.0.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/parso already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/webcolors already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbconvert already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/markupsafe already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/IPython already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nbformat already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/notebook_shim-0.2.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/attrs-24.3.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/_cffi_backend.cpython-311-x86_64-linux-gnu.so already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pexpect already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/mistune-3.1.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/ipywidgets-8.1.5.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/babel-2.16.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jsonpointer-3.0.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyterlab_widgets-3.0.13.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_lsp-2.2.5.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jinja2 already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/json5-0.10.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/decorator-5.1.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/isoduration-20.11.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/packaging already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/webcolors-24.11.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/idna already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/httpcore-1.0.7.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/distutils-precedence.pth already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nest_asyncio-1.6.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/tornado-6.4.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/executing-2.1.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/rfc3339_validator-0.1.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/jupyter_events already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/nglview already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pygments-2.19.1.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/defusedxml already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/sniffio already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/packaging-24.2.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/setuptools-75.8.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pkg_resources already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/parso-0.8.4.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/charset_normalizer already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pyzmq-26.2.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/arrow already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/anyio-4.8.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/pexpect-4.9.0.dist-info already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/dateutil-stubs already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/share already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/etc already exists. Specify --upgrade to force replacement.[0m[33m
    [0m[33mWARNING: Target directory /content/colab_libraries/bin already exists. Specify --upgrade to force replacement.[0m[33m
    [0m




```python
import pyrosetta; pyrosetta.init()
from pyrosetta import *
import glob
print(glob.glob("*.pdb"))
```

    ┌──────────────────────────────────────────────────────────────────────────────┐
    │                                 PyRosetta-4                                  │
    │              Created in JHU by Sergey Lyskov and PyRosetta Team              │
    │              (C) Copyright Rosetta Commons Member Institutions               │
    │                                                                              │
    │ NOTE: USE OF PyRosetta FOR COMMERCIAL PURPOSES REQUIRE PURCHASE OF A LICENSE │
    │         See LICENSE.PyRosetta.md or email license@uw.edu for details         │
    └──────────────────────────────────────────────────────────────────────────────┘
    PyRosetta-4 2025 [Rosetta PyRosetta4.MinSizeRel.python311.ubuntu 2025.03+release.1f5080a079a5261122c0e532c46f61a4f7e20df8 2025-01-13T15:37:50] retrieved from: http://www.pyrosetta.org
    core.init: Checking for fconfig files in pwd and ./rosetta/flags
    core.init: Rosetta version: PyRosetta4.MinSizeRel.python311.ubuntu r390 2025.03+release.1f5080a079 1f5080a079a5261122c0e532c46f61a4f7e20df8 http://www.pyrosetta.org 2025-01-13T15:37:50
    core.init: Rosetta extras: []
    core.init: command: PyRosetta -ex1 -ex2aro -database /usr/local/lib/python3.11/dist-packages/pyrosetta/database
    basic.random.init_random_generator: 'RNG device' seed mode, using '/dev/urandom', seed=-1042726083 seed_offset=0 real_seed=-1042726083
    basic.random.init_random_generator: RandomGenerator:init: Normal mode, seed=-1042726083 RG_type=mt19937
    []



```python
from pyrosetta.toolbox import cleanATOM, mutate_residue
from random import randrange,choice
import copy
AA= ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V']
sfxn = get_score_function()
fr = pyrosetta.rosetta.protocols.relax.FastRelax(scorefxn_in=sfxn , standard_repeats=1)# , standard_repeats=1
# fr.constrain_relax_segments()
```

    core.scoring.ScoreFunctionFactory: SCOREFUNCTION: ref2015
    core.scoring.etable: Starting energy table calculation
    core.scoring.etable: smooth_etable: changing atr/rep split to bottom of energy well
    core.scoring.etable: smooth_etable: spline smoothing lj etables (maxdis = 6)
    core.scoring.etable: smooth_etable: spline smoothing solvation etables (max_dis = 6)
    core.scoring.etable: Finished calculating energy tables.
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBPoly1D.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBFadeIntervals.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBEval.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/DonStrength.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/AccStrength.csv
    core.chemical.GlobalResidueTypeSet: Finished initializing fa_standard residue type set.  Created 985 residue types
    core.chemical.GlobalResidueTypeSet: Total time to initialize 1.72713 seconds.
    basic.io.database: Database file opened: scoring/score_functions/rama/fd/all.ramaProb
    basic.io.database: Database file opened: scoring/score_functions/rama/fd/prepro.ramaProb
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.all.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.gly.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.pro.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.valile.txt
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/P_AA
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/P_AA_n
    core.scoring.P_AA: shapovalov_lib::shap_p_aa_pp_smooth_level of 1( aka low_smooth ) got activated.
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/shapovalov/10deg/kappa131/a20.prop
    protocols.relax.RelaxScriptManager: Reading relax scripts list from database.
    protocols.relax.RelaxScriptManager: Looking for MonomerRelax2019.txt
    protocols.relax.RelaxScriptManager: ================== Reading script file: /usr/local/lib/python3.11/dist-packages/pyrosetta/database/sampling/relax_scripts/MonomerRelax2019.txt ==================
    protocols.relax.RelaxScriptManager: repeat %%nrepeats%%
    protocols.relax.RelaxScriptManager: coord_cst_weight 1.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.040
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.051
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.5
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.265
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.280
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.559
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.581
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 1
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: min 0.00001
    protocols.relax.RelaxScriptManager: accept_to_best
    protocols.relax.RelaxScriptManager: endrepeat


## Prepare the pdb files for AIP and the DARPin

Use [this link](https://direvo.mutanalyst.com/params) to apply [this github repo](https://github.com/matteoferla/rdkit_to_params) to the AIP .mol file created manually based on [this paper](https://www.pnas.org/doi/10.1073/pnas.1506030112) and exported from pymol. This provides a .params file that is needed for pyrosetta to interpret this molecule not as a standard protein, but as a ligand small molecule (because otherwise it doesn't like the non-standard cyclic structure).


```python
ligand_params = Vector1(['drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1.params'])

# added a line to the params file to ensure that
# it allows sampling from all 10 rotamers of AIP during the FastRelax protocol
# these 10 rotamers are not in the base file, but in the rotamers file

pose = pyrosetta.Pose()

# code from https://graylab.jhu.edu/pyrosetta/downloads/scripts/demo/D120_Ligand_interface.py

res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types( ligand_params )
pose.conformation().reset_residue_type_set_for_conf( res_set )

pyrosetta.pose_from_file(pose, "drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1_base.pdb")

print(sfxn(pose))
fr.apply(pose)
print(sfxn(pose)) # it chooses the lowest energy rotamer for now!

# chain_pose=pyrosetta.rosetta.core.pose.Pose.split_by_chain(pose)

# print(len(chain_pose))
# a=[i for i in chain_pose]
# [print(sfxn(a[i])) for i in range(10)]

# a[6].dump_pdb("AIP_best.pdb")

pose.dump_pdb("drive/MyDrive/BME406team/Flex-ddG/AIP_best.pdb")
```

    core.conformation.Conformation: [ WARNING ] Attempted to determine the residue type set of an empty pose.
    core.import_pose.import_pose: File 'drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1_base.pdb' automatically determined to be of type PDB
    core.io.pdb.HeaderInformation: [ ERROR ] Malformed Compound record found: ' AIP'
    27.7766784486412
    protocols.relax.FastRelax: CMD: repeat  27.7767  nan  nan  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  27.7767  nan  nan  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  27.7767  nan  nan  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamers.SingleLigandRotamerLibrary: Added 10 rotamers for AIP
    core.pack.pack_rotamers: built 11 rotamers at 1 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  10.9479  nan  nan  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9479  nan  nan  0.02805
    protocols.relax.FastRelax: CMD: min  10.9479  nan  nan  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  10.9479  nan  nan  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9479  nan  nan  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamers.SingleLigandRotamerLibrary: Added 10 rotamers for AIP
    core.pack.pack_rotamers: built 11 rotamers at 1 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  10.9479  nan  nan  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9479  nan  nan  0.154
    protocols.relax.FastRelax: CMD: min  10.9478  nan  nan  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  10.9478  nan  nan  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9478  nan  nan  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamers.SingleLigandRotamerLibrary: Added 10 rotamers for AIP
    core.pack.pack_rotamers: built 11 rotamers at 1 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  10.9478  nan  nan  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9478  nan  nan  0.31955
    protocols.relax.FastRelax: CMD: min  10.9478  nan  nan  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  10.9478  nan  nan  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  10.9478  nan  nan  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamers.SingleLigandRotamerLibrary: Added 10 rotamers for AIP
    core.pack.pack_rotamers: built 11 rotamers at 1 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  10.9478  nan  nan  0.55
    protocols.relax.FastRelax: CMD: min  10.9478  nan  nan  0.55
    protocols.relax.FastRelax: MRP: 0  10.9478  10.9478  nan  nan
    protocols.relax.FastRelax: CMD: accept_to_best  10.9478  nan  nan  0.55
    protocols.relax.FastRelax: CMD: endrepeat  10.9478  nan  nan  0.55
    protocols::checkpoint: Deleting checkpoints of FastRelax
    10.947826439045837





    True



Alphafolded the DARPin sequence, converted the .cif file to a .pdb file used here


```python
# binderc=pose_from_file('AIP-I-please.cif', read_fold_tree=True, type=pyrosetta.rosetta.core.import_pose.FileType.CIF_file)
# binderc=pose_from_file('drive/MyDrive/BME406team/Flex-ddG/DARPin_fold.cif', read_fold_tree=True, type=pyrosetta.rosetta.core.import_pose.FileType.CIF_file)
binderc=pose_from_pdb('drive/MyDrive/BME406team/Flex-ddG/DARPin_fold.pdb')
print(sfxn(binderc))
fr.apply(binderc)
print(sfxn(binderc))
fr.apply(binderc)
print(sfxn(binderc))
fr.apply(binderc)
print(sfxn(binderc))
binderc.dump_pdb("drive/MyDrive/BME406team/Flex-ddG/DARPin_best.pdb")
```

    -428.30518376849
    -587.8905386792311
    -588.9119268963791
    -588.769925975024





    True



## Full Flex-DDG from iGEM DARPin

### Combine PDB files and relax

Used pymol to manually combine the DARPin with AIP in 5 different initial configurations. Try relaxing all and see which gets lowest energy? Then assume that structure is how it normally binds, and optimize from there


```python
energies=[[0,0,0,0] for i in range(5)]

ligand_params = Vector1(['drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1.params'])
pose = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types( ligand_params )
pose.conformation().reset_residue_type_set_for_conf( res_set )
for i in range(5):
    pose_from_file(pose, "drive/MyDrive/BME406team/Flex-ddG/Binder+AIP_options/AIP_Binder_"+str(i+1)+".pdb")
    energies[i][0]=sfxn(pose)
    for j in range(3):
        fr.apply(pose)
        energies[i][j+1]=sfxn(pose)
        print(energies)
```

    [[524.407356063892, -583.7837593817004, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [0, 0, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, 0, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, -584.7510178103424, 0], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, -584.7510178103424, -581.0737362773634], [0, 0, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, -584.7510178103424, -581.0737362773634], [-577.8436817189021, -578.1326669929686, 0, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, -584.7510178103424, -581.0737362773634], [-577.8436817189021, -578.1326669929686, -576.7729430403792, 0]]
    [[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666], [6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539], [4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164], [707.8885717434343, -584.3425479140429, -584.7510178103424, -581.0737362773634], [-577.8436817189021, -578.1326669929686, -576.7729430403792, -577.2334408723765]]


Output of the above:

[[524.407356063892, -583.7837593817004, -584.6667501454315, -585.2322315222666],

[6554.6713487588895, -579.1082024120345, -583.0821768382589, -586.5125765283539],

[4496.01379091503, -570.1285169729424, -570.7696324307642, -578.8451111521164],

[707.8885717434343, -584.3425479140429, -584.7510178103424, -581.0737362773634],

[-577.8436817189021, -578.1326669929686, -576.7729430403792, -577.2334408723765]]


```python
ligand_params = Vector1(['drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1.params'])
pose = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types( ligand_params )
pose.conformation().reset_residue_type_set_for_conf( res_set )
pose_from_file(pose, "drive/MyDrive/BME406team/Flex-ddG/Binder+AIP_options/AIP_Binder_2.pdb")
print(sfxn(pose))
fr.apply(pose)
print(sfxn(pose))
fr.apply(pose)
print(sfxn(pose))
fr.apply(pose)
print(sfxn(pose))
fr.apply(pose)
print(sfxn(pose))
pose.dump_pdb("drive/MyDrive/BME406team/Flex-ddG/Original_DARPin_Bound.pdb")
```

    6554.6713487588895
    -578.456756423737
    -582.322718044388
    -583.0647273226798
    -585.1220404688302





    True



### Flex ddG


```python
# flexddg
ligand_params = Vector1(['drive/MyDrive/BME406team/Flex-ddG/Autoinduced_Peptide_1.params'])
pose = pyrosetta.Pose()
pose_old = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types( ligand_params )
pose.conformation().reset_residue_type_set_for_conf( res_set )
pose_old.conformation().reset_residue_type_set_for_conf( res_set )
for i in range(1000):
    pose_from_file(pose, "drive/MyDrive/BME406team/Flex-ddG/flexddg_run.pdb")
    mutate_residue(pose,randrange(1,len(pose.sequence())+1),choice(AA)) # 1-indexed AA to mutate
    fr.apply(pose)
    print("relaxed")
    pose_from_file(pose_old, "drive/MyDrive/BME406team/Flex-ddG/flexddg_run.pdb")
    if sfxn(pose)<sfxn(pose_old):
        pose.dump_pdb("drive/MyDrive/BME406team/Flex-ddG/flexddg_run.pdb")
        print("saved")
```


```python
!pip install pyrosetta-installer
!python -c 'import pyrosetta_installer; pyrosetta_installer.install_pyrosetta()'
```

    Requirement already satisfied: pyrosetta-installer in /usr/local/lib/python3.11/dist-packages (0.1.2)
    PyRosetta install detected, doing nothing...



```python
!wget https://graylab.jhu.edu/download/PyRosetta4/archive/release/PyRosetta4.Release.python38.linux/PyRosetta4.Release.python38.linux.release-321.tar.bz2
!tar -xjf PyRosetta4.Release.python38.linux.release-321.tar.bz2
import sys
sys.path.append('/content/PyRosetta4.Release.python38.linux.release-321')
import pyrosetta
pyrosetta.init()
```


```python
from pyrosetta import *
from pyrosetta.rosetta.protocols.ddg import ddGMover
from pyrosetta.rosetta.protocols.relax import FastRelax
from pyrosetta.rosetta.core.scoring import ScoreFunction
from pyrosetta.rosetta.core.pose import Pose
from pyrosetta.rosetta.protocols.simple_moves import MutateResidue

# Initialize PyRosetta
pyrosetta.init()

# Load the PDB file
pose = Pose()
pyrosetta.rosetta.core.import_pose.pose_from_file(pose, "4bxi.pdb")

# Create a score function
scorefxn = pyrosetta.create_score_function("ref2015")

# Set up the ddG mover
ddg = ddGMover()
ddg.score_function(scorefxn)
ddg.num_iterations(50)  # Number of iterations for sampling, increase for better results
ddg.neighbor_cutoff(8.0)  # Angstroms

# Set up the FastRelax mover for minimization
relax = FastRelax()
relax.set_scorefxn(scorefxn)

# Function to perform flex ddG calculation
def calculate_flex_ddg(pose, mutation):
    # Create a copy of the original pose
    mutant_pose = Pose(pose)

    # Perform the mutation
    mutate = MutateResidue(mutation[1], mutation[2])
    mutate.apply(mutant_pose)

    # Relax the mutant pose
    relax.apply(mutant_pose)

    # Calculate ddG
    ddg.apply(mutant_pose)

    # Get the ddG value
    ddg_value = ddg.ddg()

    return ddg_value

# Example usage
mutation = ('A', 10, 'ALA')  # Chain A, residue 10, mutate to Alanine
ddg_value = calculate_flex_ddg(pose, mutation)
print(f"Predicted ddG for mutation {mutation}: {ddg_value} REU")
```

    ┌──────────────────────────────────────────────────────────────────────────────┐
    │                                 PyRosetta-4                                  │
    │              Created in JHU by Sergey Lyskov and PyRosetta Team              │
    │              (C) Copyright Rosetta Commons Member Institutions               │
    │                                                                              │
    │ NOTE: USE OF PyRosetta FOR COMMERCIAL PURPOSES REQUIRE PURCHASE OF A LICENSE │
    │         See LICENSE.PyRosetta.md or email license@uw.edu for details         │
    └──────────────────────────────────────────────────────────────────────────────┘
    PyRosetta-4 2025 [Rosetta PyRosetta4.Release.python311.ubuntu 2025.03+release.1f5080a079a5261122c0e532c46f61a4f7e20df8 2025-01-13T15:37:50] retrieved from: http://www.pyrosetta.org
    core.init: Checking for fconfig files in pwd and ./rosetta/flags
    core.init: Rosetta version: PyRosetta4.Release.python311.ubuntu r390 2025.03+release.1f5080a079 1f5080a079a5261122c0e532c46f61a4f7e20df8 http://www.pyrosetta.org 2025-01-13T15:37:50
    core.init: Rosetta extras: []
    core.init: command: PyRosetta -ex1 -ex2aro -database /usr/local/lib/python3.11/dist-packages/pyrosetta/database
    basic.random.init_random_generator: 'RNG device' seed mode, using '/dev/urandom', seed=-156811217 seed_offset=0 real_seed=-156811217
    basic.random.init_random_generator: RandomGenerator:init: Normal mode, seed=-156811217 RG_type=mt19937
    core.import_pose.import_pose: File '4bxi.pdb' automatically determined to be of type PDB
    core.chemical.GlobalResidueTypeSet: Loading (but possibly not actually using) 'GOL' from the PDB components dictionary for residue type 'pdb_GOL'
    core.chemical.GlobalResidueTypeSet: Loading (but possibly not actually using) 'MPD' from the PDB components dictionary for residue type 'pdb_MPD'
    core.chemical.GlobalResidueTypeSet: Loading (but possibly not actually using) 'ACT' from the PDB components dictionary for residue type 'pdb_ACT'
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue GLU 65
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CD  on residue GLU 65
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE1 on residue GLU 65
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE2 on residue GLU 65
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue GLU 69
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CD  on residue GLU 69
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE1 on residue GLU 69
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE2 on residue GLU 69
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue ASP 71
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OD1 on residue ASP 71
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OD2 on residue ASP 71
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue GLU 83
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CD  on residue GLU 83
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE1 on residue GLU 83
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE2 on residue GLU 83
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CD  on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  NE  on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CZ  on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  NH1 on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  NH2 on residue ARG 100
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CG  on residue GLU 103
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CD  on residue GLU 103
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE1 on residue GLU 103
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OE2 on residue GLU 103
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  CE  on residue LYS 140
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  NZ  on residue LYS 140
    core.conformation.Conformation: [ WARNING ] missing heavyatom:  OXT on residue ASN:CtermProteinFull 146
    core.pack.pack_missing_sidechains: packing residue number 65 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 69 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 71 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 83 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 100 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 103 because of missing atom number 6 atom name  CG
    core.pack.pack_missing_sidechains: packing residue number 140 because of missing atom number 8 atom name  CE
    core.pack.task: Packer task: initialize from command line()
    core.scoring.ScoreFunctionFactory: SCOREFUNCTION: ref2015
    core.scoring.etable: Starting energy table calculation
    core.scoring.etable: smooth_etable: changing atr/rep split to bottom of energy well
    core.scoring.etable: smooth_etable: spline smoothing lj etables (maxdis = 6)
    core.scoring.etable: smooth_etable: spline smoothing solvation etables (max_dis = 6)
    core.scoring.etable: Finished calculating energy tables.
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBPoly1D.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBFadeIntervals.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/HBEval.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/DonStrength.csv
    basic.io.database: Database file opened: scoring/score_functions/hbonds/ref2015_params/AccStrength.csv
    basic.io.database: Database file opened: scoring/score_functions/rama/fd/all.ramaProb
    basic.io.database: Database file opened: scoring/score_functions/rama/fd/prepro.ramaProb
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.all.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.gly.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.pro.txt
    basic.io.database: Database file opened: scoring/score_functions/omega/omega_ppdep.valile.txt
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/P_AA
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/P_AA_n
    core.scoring.P_AA: shapovalov_lib::shap_p_aa_pp_smooth_level of 1( aka low_smooth ) got activated.
    basic.io.database: Database file opened: scoring/score_functions/P_AA_pp/shapovalov/10deg/kappa131/a20.prop
    basic.io.database: Database file opened: scoring/score_functions/elec_cp_reps.dat
    core.scoring.elec.util: Read 40 countpair representative atoms
    core.pack.dunbrack.RotamerLibrary: shapovalov_lib_fixes_enable option is true.
    core.pack.dunbrack.RotamerLibrary: shapovalov_lib::shap_dun10_smooth_level of 1( aka lowest_smooth ) got activated.
    core.pack.dunbrack.RotamerLibrary: Binary rotamer library selected: /usr/local/lib/python3.11/dist-packages/pyrosetta/database/rotamer/shapovalov/StpDwn_0-0-0/Dunbrack10.lib.bin
    core.pack.dunbrack.RotamerLibrary: Using Dunbrack library binary file '/usr/local/lib/python3.11/dist-packages/pyrosetta/database/rotamer/shapovalov/StpDwn_0-0-0/Dunbrack10.lib.bin'.
    core.pack.dunbrack.RotamerLibrary: Dunbrack 2010 library took 0.521523 seconds to load from binary
    core.pack.pack_rotamers: built 106 rotamers at 7 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.RelaxScriptManager: Reading relax scripts list from database.
    core.scoring.ScoreFunctionFactory: SCOREFUNCTION: ref2015
    protocols.relax.RelaxScriptManager: Looking for MonomerRelax2019.txt
    protocols.relax.RelaxScriptManager: ================== Reading script file: /usr/local/lib/python3.11/dist-packages/pyrosetta/database/sampling/relax_scripts/MonomerRelax2019.txt ==================
    protocols.relax.RelaxScriptManager: repeat %%nrepeats%%
    protocols.relax.RelaxScriptManager: coord_cst_weight 1.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.040
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.051
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.5
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.265
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.280
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.559
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: scale:fa_rep 0.581
    protocols.relax.RelaxScriptManager: min 0.01
    protocols.relax.RelaxScriptManager: coord_cst_weight 0.0
    protocols.relax.RelaxScriptManager: scale:fa_rep 1
    protocols.relax.RelaxScriptManager: repack
    protocols.relax.RelaxScriptManager: min 0.00001
    protocols.relax.RelaxScriptManager: accept_to_best
    protocols.relax.RelaxScriptManager: endrepeat
    protocols.relax.FastRelax: CMD: repeat  -78.6557  0  0  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  -78.6557  0  0  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  -185.388  0  0  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3656 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -412.252  0  0  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  -407.505  0  0  0.02805
    protocols.relax.FastRelax: CMD: min  -620.568  0.970089  0.970089  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  -620.568  0.970089  0.970089  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  -352.147  0.970089  0.970089  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3876 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -382.06  0.970089  0.970089  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  -366.892  0.970089  0.970089  0.154
    protocols.relax.FastRelax: CMD: min  -527.097  0.618397  0.618397  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  -527.097  0.618397  0.618397  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  -458.013  0.618397  0.618397  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3532 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -458.789  0.618397  0.618397  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  -453.414  0.618397  0.618397  0.31955
    protocols.relax.FastRelax: CMD: min  -471.693  0.537161  0.537161  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  -471.693  0.537161  0.537161  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  -408.392  0.537161  0.537161  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3252 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -408.62  0.537161  0.537161  0.55
    protocols.relax.FastRelax: CMD: min  -445.741  0.588547  0.588547  0.55
    protocols.relax.FastRelax: MRP: 0  -445.741  -445.741  0.588547  0.588547
    protocols.relax.FastRelax: CMD: accept_to_best  -445.741  0.588547  0.588547  0.55
    protocols.relax.FastRelax: CMD: endrepeat  -445.741  0.588547  0.588547  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  -445.741  0.588547  0.588547  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  -533.583  0.588547  0.588547  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3502 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -548.245  0.588547  0.588547  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  -544.792  0.588547  0.588547  0.02805
    protocols.relax.FastRelax: CMD: min  -643.364  0.980271  0.980271  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  -643.364  0.980271  0.980271  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  -395.865  0.980271  0.980271  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3713 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -420.722  0.980271  0.980271  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  -406.327  0.980271  0.980271  0.154
    protocols.relax.FastRelax: CMD: min  -542.627  0.737868  0.737868  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  -542.627  0.737868  0.737868  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  -474.575  0.737868  0.737868  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3488 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -475.028  0.737868  0.737868  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  -469.702  0.737868  0.737868  0.31955
    protocols.relax.FastRelax: CMD: min  -485.819  0.643498  0.643498  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  -485.819  0.643498  0.643498  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  -422.461  0.643498  0.643498  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3404 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -423.05  0.643498  0.643498  0.55
    protocols.relax.FastRelax: CMD: min  -447.389  0.636023  0.636023  0.55
    protocols.relax.FastRelax: MRP: 1  -447.389  -447.389  0.636023  0.636023
    protocols.relax.FastRelax: CMD: accept_to_best  -447.389  0.636023  0.636023  0.55
    protocols.relax.FastRelax: CMD: endrepeat  -447.389  0.636023  0.636023  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  -447.389  0.636023  0.636023  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  -536.486  0.636023  0.636023  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3563 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -551.311  0.636023  0.636023  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  -548.675  0.636023  0.636023  0.02805
    protocols.relax.FastRelax: CMD: min  -641.149  0.978113  0.978113  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  -641.149  0.978113  0.978113  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  -404.569  0.978113  0.978113  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3669 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -426.053  0.978113  0.978113  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  -411.929  0.978113  0.978113  0.154
    protocols.relax.FastRelax: CMD: min  -543.188  0.740047  0.740047  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  -543.188  0.740047  0.740047  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  -474.993  0.740047  0.740047  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3558 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -475.207  0.740047  0.740047  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  -469.9  0.740047  0.740047  0.31955
    protocols.relax.FastRelax: CMD: min  -490.224  0.642561  0.642561  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  -490.224  0.642561  0.642561  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  -429.655  0.642561  0.642561  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3353 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -430.433  0.642561  0.642561  0.55
    protocols.relax.FastRelax: CMD: min  -452.917  0.638117  0.638117  0.55
    protocols.relax.FastRelax: MRP: 2  -452.917  -452.917  0.638117  0.638117
    protocols.relax.FastRelax: CMD: accept_to_best  -452.917  0.638117  0.638117  0.55
    protocols.relax.FastRelax: CMD: endrepeat  -452.917  0.638117  0.638117  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  -452.917  0.638117  0.638117  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  -540.728  0.638117  0.638117  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3428 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -551.701  0.638117  0.638117  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  -548.145  0.638117  0.638117  0.02805
    protocols.relax.FastRelax: CMD: min  -652.994  1.01992  1.01992  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  -652.994  1.01992  1.01992  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  -393.244  1.01992  1.01992  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3718 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -417.466  1.01992  1.01992  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  -402.555  1.01992  1.01992  0.154
    protocols.relax.FastRelax: CMD: min  -540.918  0.753817  0.753817  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  -540.918  0.753817  0.753817  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  -470.035  0.753817  0.753817  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3564 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -470.892  0.753817  0.753817  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  -465.376  0.753817  0.753817  0.31955
    protocols.relax.FastRelax: CMD: min  -483.529  0.660045  0.660045  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  -483.529  0.660045  0.660045  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  -419.707  0.660045  0.660045  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3491 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -420.043  0.660045  0.660045  0.55
    protocols.relax.FastRelax: CMD: min  -445.997  0.649713  0.649713  0.55
    protocols.relax.FastRelax: MRP: 3  -445.997  -452.917  0.638117  0.638117
    protocols.relax.FastRelax: CMD: accept_to_best  -445.997  0.649713  0.649713  0.55
    protocols.relax.FastRelax: CMD: endrepeat  -445.997  0.649713  0.649713  0.55
    protocols.relax.FastRelax: CMD: coord_cst_weight  -445.997  0.649713  0.649713  0.55
    protocols.relax.FastRelax: CMD: scale:fa_rep  -535.117  0.649713  0.649713  0.022
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3616 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -550.22  0.649713  0.649713  0.022
    protocols.relax.FastRelax: CMD: scale:fa_rep  -547.503  0.649713  0.649713  0.02805
    protocols.relax.FastRelax: CMD: min  -652.995  1.01647  1.01647  0.02805
    protocols.relax.FastRelax: CMD: coord_cst_weight  -652.995  1.01647  1.01647  0.02805
    protocols.relax.FastRelax: CMD: scale:fa_rep  -399.802  1.01647  1.01647  0.14575
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3705 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -416.27  1.01647  1.01647  0.14575
    protocols.relax.FastRelax: CMD: scale:fa_rep  -401.499  1.01647  1.01647  0.154
    protocols.relax.FastRelax: CMD: min  -541.151  0.719617  0.719617  0.154
    protocols.relax.FastRelax: CMD: coord_cst_weight  -541.151  0.719617  0.719617  0.154
    protocols.relax.FastRelax: CMD: scale:fa_rep  -471.602  0.719617  0.719617  0.30745
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3464 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -473.385  0.719617  0.719617  0.30745
    protocols.relax.FastRelax: CMD: scale:fa_rep  -467.923  0.719617  0.719617  0.31955
    protocols.relax.FastRelax: CMD: min  -485.898  0.64112  0.64112  0.31955
    protocols.relax.FastRelax: CMD: coord_cst_weight  -485.898  0.64112  0.64112  0.31955
    protocols.relax.FastRelax: CMD: scale:fa_rep  -419.854  0.64112  0.64112  0.55
    core.pack.task: Packer task: initialize from command line()
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_GOL
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_ACT
    core.pack.rotamer_set.RotamerSet_: Using simple Rotamer generation logic for pdb_MPD
    core.pack.pack_rotamers: built 3259 rotamers at 151 positions.
    core.pack.interaction_graph.interaction_graph_factory: Instantiating DensePDInteractionGraph
    protocols.relax.FastRelax: CMD: repack  -419.957  0.64112  0.64112  0.55
    protocols.relax.FastRelax: CMD: min  -445.796  0.627885  0.627885  0.55
    protocols.relax.FastRelax: MRP: 4  -445.796  -452.917  0.638117  0.638117
    protocols.relax.FastRelax: CMD: accept_to_best  -445.796  0.627885  0.627885  0.55
    protocols.relax.FastRelax: CMD: endrepeat  -445.796  0.627885  0.627885  0.55
    protocols::checkpoint: Deleting checkpoints of FastRelax


## Rational Flex-DDG from Randomized DARPin

Used pymol to manually combine the DARPin with AIP in 8 different initial configurations, then applied the following code in a .py file on a compute cluster to run Flex-ddG multiple times on each of these 8 configurations in parallel.


```python
import pyrosetta_installer

pyrosetta_installer.install_pyrosetta()
import pyrosetta
from pyrosetta import *
import sys
from tqdm import tqdm
from pyrosetta.toolbox import cleanATOM, mutate_residue
from random import randrange, choice
import copy
from datetime import datetime

job_id = int(sys.argv[1])

pyrosetta.init("-mute all")
# pyrosetta.init("-mute core basic protocols")

AA = [
    "A",
    "R",
    "N",
    "D",
    "C",
    "Q",
    "E",
    "G",
    "H",
    "I",
    "L",
    "K",
    "M",
    "F",
    "P",
    "S",
    "T",
    "W",
    "Y",
    "V",
]
residue_mut = [[32], [33, 34, 36, 44, 45], [41], [57]]
# reduced number of possible mutations: speeds up algorithm and increases DARPin fitness
AA_options = [
    ["D", "N", "S", "T"],
    ["A", "R", "N", "D", "Q", "E", "H", "K", "S", "T", "W", "Y"],
    ["A", "S", "T", "V", "L"],
    ["N", "H", "Y"],
]
all_mutations = [[]]
for i in range(len(residue_mut)):
    for j in range(len(residue_mut[i])):
        for k in range(len(AA_options[i])):
            for l in range(3):
                all_mutations.append([residue_mut[i][j] + 1 + l * 33, AA_options[i][k]])
all_mutations = all_mutations[1:]

sfxn = get_score_function()
fr = pyrosetta.rosetta.protocols.relax.FastRelax(
    scorefxn_in=sfxn, standard_repeats=1
)  # , standard_repeats=1
# fr.constrain_relax_segments()

ligand_params = Vector1(["./Autoinduced_Peptide_1.params"])
pose = pyrosetta.Pose()
pose_old = pyrosetta.Pose()
res_set = pose.conformation().modifiable_residue_type_set_for_conf()
res_set.read_files_for_base_residue_types(ligand_params)
pose.conformation().reset_residue_type_set_for_conf(res_set)
pose_old.conformation().reset_residue_type_set_for_conf(res_set)

pose_from_file(pose, "./input/DARPin_Bound_" + str(job_id // 5 + 1) + ".pdb")
for i in range(10000):  # Make a lot of the allowed mutations to randomize the sequence to start with
    mut = choice(all_mutations)
    mutate_residue(pose, mut[0], mut[1])  # 1-indexed AA to mutate

fr.apply(pose)

pose.dump_pdb("./output/flex_" + str(job_id) + ".pdb")

print("starting loop:<" + str(sfxn(pose)) + "," + str(pose.sequence()) + ">")
start_time = datetime.now()
for i in range(100000):
    pose_from_file(pose, "./output/flex_" + str(job_id) + ".pdb")
    mut = choice(all_mutations)
    mutate_residue(pose, mut[0], mut[1])  # 1-indexed AA to mutate
    fr.apply(pose)
    pose_from_file(pose_old, "./output/flex_" + str(job_id) + ".pdb")
    if sfxn(pose) < sfxn(pose_old):
        pose.dump_pdb("./output/flex_" + str(job_id) + ".pdb")
        print(
            "["
            + str(datetime.now() - start_time)
            + "]saved:<"
            + str(sfxn(pose))
            + ","
            + str(pose.sequence())
            + ">"
        )

```
