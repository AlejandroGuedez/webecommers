import os
from pathlib import Path
from typing import Protocol
from PIL import Image
from ..core.config import settings

class StorageProvider(Protocol):
    def save(self, tenant: str, file_name: str, data: bytes) -> str: ...

class LocalStorageProvider:
    def __init__(self, base_dir: str | None = None):
        self.base_dir = Path(base_dir or settings.media_root)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def save(self, tenant: str, file_name: str, data: bytes) -> str:
        safe_name = file_name.replace("../", "")
        tenant_dir = self.base_dir / tenant
        tenant_dir.mkdir(parents=True, exist_ok=True)
        dest = tenant_dir / safe_name
        with open(dest, "wb") as f:
            f.write(data)
        # create thumbnail if image
        try:
            img = Image.open(dest)
            img.thumbnail((300,300))
            thumb = tenant_dir / f"thumb_{safe_name}"
            img.save(thumb)
        except Exception:
            pass
        return f"/media/{tenant}/{safe_name}"

storage = LocalStorageProvider()
