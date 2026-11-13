# Entry: decodes the base64 image shipped in this repo to /output/entry.png.
import base64
import os

HERE = os.path.dirname(os.path.abspath(__file__))
out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(HERE, "entry.b64")) as f:
    data = base64.b64decode(f.read())
with open(os.path.join(out_dir, "entry.png"), "wb") as f:
    f.write(data)
