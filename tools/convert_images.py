import os, sys, pathlib
from PIL import Image

def convert_to_webp(src_dir, out_dir, quality=82):
    os.makedirs(out_dir, exist_ok=True)
    for cur, _, files in os.walk(src_dir):
        for fn in files:
            p = os.path.join(cur, fn)
            ext = pathlib.Path(fn).suffix.lower()
            if ext not in [".jpg", ".jpeg", ".png", ".bmp"]:
                continue
            rel = os.path.relpath(p, src_dir)
            out_path = os.path.join(out_dir, os.path.splitext(rel)[0] + ".webp")
            os.makedirs(os.path.dirname(out_path), exist_ok=True)
            try:
                im = Image.open(p).convert("RGB")
                im.save(out_path, "WEBP", quality=quality, method=6)
                print("Converted:", rel, "->", os.path.relpath(out_path, out_dir))
            except Exception as e:
                print("Skip", rel, ":", e)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python tools/convert_images.py <src_dir> <out_dir> [quality]")
        sys.exit(1)
    src = sys.argv[1]
    out = sys.argv[2]
    quality = int(sys.argv[3]) if len(sys.argv) > 3 else 82
    convert_to_webp(src, out, quality)