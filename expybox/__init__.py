import warnings
from .expybox import ExpyBox

# enable RuntimeWarnings (some imports just break filters I think, so just restore it)
# this is not very nice, but I'm not sure how to do this otherwise :(
warnings.filterwarnings(action='always', module='expybox')