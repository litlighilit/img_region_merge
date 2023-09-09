from dataclasses import dataclass


from PIL import Image

from .cal_region import distr_region
from . import Vector2I, vec2i, Deg, Sequence, Collection

Img = Image.Image  # Image class
Size = Vector2I

@dataclass
class NormedImg:
    size: Size
    images: Sequence[Img]


def merge(imgs: Collection[Img], like: Img, *, rotate: Deg = 0.) -> Img:  # get mode from `like`
    return _handle(imgs, like, rotate)


def norm_size(imgs: Collection[Img]) -> Size:
    nsize = 0 + 0J # use as Vector2
    # avg
    for im in imgs: nsize += complex(*im.size)
    nsize /= len(imgs)
    return vec2i(nsize.real, nsize.imag)


def normalize(imgs: Collection[Img]) -> NormedImg:
    size = norm_size(imgs)

    def _resize(im: Img) -> Img:
        return im.resize(size)

    return NormedImg(size, list(map(_resize, imgs)))



def _handle(imgs: Collection[Img], like: Img, rotate: Deg) -> Img:
    nimg = normalize(imgs)
    size = nimg.size
    (w, h) = size

    mid_point = vec2i(w / 2, h / 2)
    region_distr = distr_region(len(imgs), mid_point, rotate)

    nimgs = nimg.images
    result = Image.new(like.mode, size)
    for x in range(w):
        for y in range(h):
            p = (x, y)
            result.putpixel(p, nimgs[region_distr(p)].getpixel(p))
    return result


if __name__ == "__main__":

    def blank_im(size):
        return Image.new("RGB", size)

    def ims(*sizes):
        result = []
        for s in sizes:
            result.append(blank_im(s))
        return result

    i = ims((1, 1), (3, 4))
    print(norm_size(i))
