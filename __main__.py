from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter as DefsFormatter
from .proc_img import merge, Image
from .pathutil import dirname, get_ext, join as join_path
from . import Deg, __doc__ as desc  # get from __init__.py

DEF_OUT_FMT = "merged%s"
parser = ArgumentParser(
    prog=__package__, description=desc, formatter_class=DefsFormatter
)
parser.add_argument("file", action="store", nargs="+", help="image file to be merged")
parser.add_argument("-o", "--output", default=DEF_OUT_FMT,
    help="output file name format, %%s means .ext and defaults to the first image's ext",  # here %% -> %
)
parser.add_argument('-a', '--angle', type=Deg, default=0, help="rotate angle, 0 means the cut-off line is horizontal")
args = parser.parse_args()


fnames: list[str] = args.file
base_path = fnames[0]
ext = get_ext(base_path)
ofname: str = args.output
d = dirname(ofname) or dirname(base_path)
ofname = ofname % ext
opath = join_path(d, ofname)
# l=list(im for im in map(Image.open, fnames));print(l)
imgs = tuple(im for im in map(Image.open, fnames))
base_img = imgs[0]
rotate_ang: Deg = args.angle
om = merge(imgs, base_img, rotate=rotate_ang)
for i in imgs:
    i.close()
om.save(opath)
