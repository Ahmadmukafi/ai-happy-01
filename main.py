# Entry: decodes the base64 image shipped in this repo to /output/entry.png.
import base64
import os
from pathlib import Path

here = Path(__file__).resolve().parent
out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
out_dir.mkdir(parents=True, exist_ok=True)
data = base64.b64decode((here / "entry.b64").read_text())
if not (data[:4] == b"\x89PNG" or data[:3] == b"\xff\xd8\xff"):
    raise ValueError("decoded entry.b64 is not a PNG or JPEG image")
(out_dir / "entry.png").write_bytes(data)
