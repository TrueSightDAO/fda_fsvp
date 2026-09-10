"""Site-visit PDF media helper — EXIF-safe image embedding for reportlab.

WHY THIS EXISTS (incident, 2026-09-10, Sí­tio Torres FDA FSVP record)
-------------------------------------------------------------------
Photo IMG_9682.HEIC rendered rotated 90 degrees in the site-visit PDF.

Root cause: Apple's HEIC->JPEG export already writes the pixels UPRIGHT but
leaves a *stale* EXIF Orientation tag (e.g. 6 = "rotate 90 CW"). Two defects
then compounded:
  1. The ad-hoc converter called ImageOps.exif_transpose() on pixels that were
     ALREADY upright -> rotated them into the ground (sideways).
  2. It resized every image to a fixed landscape box (1500x1125) -> squashed
     portrait frames and destroyed the aspect the PDF box was computed from.

reportlab's RLImage never consults EXIF and never rescales: the caller must
pass the TRUE pixel width/height or the photo is stretched.

THE RULE
--------
* Embed the pixels AS-IS (no exif_transpose) for TrueSight media-archive
  derivatives (frames/*.jpg exported from Apple HEIC) — those pixels are
  authoritative and already upright; the orientation tag is stale.
* Preserve aspect ratio on downscale, and return the true size so the PDF
  layout box matches the image geometry.
* Strip EXIF on write (PIL does this by default when no exif= is passed).
* Only pass respect_exif=True for RAW sensor JPEGs whose tag genuinely
  describes not-yet-rotated pixels (some third-party phone JPEGs). Never for
  the Apple HEIC derivatives in this pipeline.

USAGE
-----
    from tools.site_visit_images import img_flow
    for flowable in img_flow("frames/IMG_9673.jpg", 118, "caption ..."):
        story.append(flowable)
"""
from __future__ import annotations

from PIL import Image as _PILImage, ImageOps
from reportlab.lib.units import mm
from reportlab.platypus import Image as RLImage, Spacer, Paragraph

MAXPX = 1400          # longest edge after downscale
MAXH_MM = 165.0        # cap rendered height so a tall photo fits one page

_CACHE: dict[str, tuple[str, tuple[int, int]]] = {}


def prepare_for_pdf(path: str, maxpx: int = MAXPX, respect_exif: bool = False) -> tuple[str, tuple[int, int]]:
    """Downscale `path` aspect-preserving and return (normalized_path, (w, h)).

    Pixels are embedded AS-IS by default (see module docstring). Set
    respect_exif=True only for raw JPEGs whose orientation tag is authoritative.
    """
    if path in _CACHE:
        return _CACHE[path]
    im = _PILImage.open(path)
    if respect_exif:
        im = ImageOps.exif_transpose(im)
    if im.mode not in ("RGB", "L"):
        im = im.convert("RGB")
    w, h = im.size
    if max(w, h) > maxpx:
        if w >= h:
            nw, nh = maxpx, max(1, int(round(h * maxpx / w)))
        else:
            nh, nw = maxpx, max(1, int(round(w * maxpx / h)))
        im = im.resize((nw, nh), _PILImage.LANCZOS)
    w, h = im.size
    out = f"/tmp/_pdfimg_{abs(hash((path, w, h)))}.jpg"
    im.save(out, quality=82)          # no exif= -> stale orientation tag dropped
    _CACHE[path] = (out, (w, h))
    return _CACHE[path]


def img_flow(path: str, w_mm: float, caption: str, caption_style=None,
             maxpx: int = MAXPX, respect_exif: bool = False) -> list:
    """Return a list of reportlab flowables: image + caption, aspect-correct."""
    out, (w, h) = prepare_for_pdf(path, maxpx=maxpx, respect_exif=respect_exif)
    tw = w_mm * mm
    th = tw * h / w
    if th > MAXH_MM * mm:
        th = MAXH_MM * mm
        tw = th * w / h
    flows = [RLImage(out, width=tw, height=th), Spacer(1, 2)]
    if caption:
        flows.append(Paragraph(caption, caption_style) if caption_style else Paragraph(caption))
    flows.append(Spacer(1, 8))
    return flows
