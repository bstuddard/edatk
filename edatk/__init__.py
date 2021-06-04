import warnings
warnings.filterwarnings("ignore", module = "matplotlib\..*" )
warnings.filterwarnings("ignore", module = "seaborn\..*" )
warnings.filterwarnings("ignore", message="FixedFormatter should only be used together with FixedLocator")
warnings.filterwarnings("ignore", message="Converting input from bool to <class 'numpy.uint8'> for compatibility.")

from ._core import get_fig_ax
from ._auto_eda import auto_eda

__all__ = [
    "auto_eda",
    "get_fig_ax"
]

__version__ = '0.0.4'
