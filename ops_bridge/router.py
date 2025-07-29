from .connectors import shopify, etsy, site
def get_connector(platform: str):
    p = platform.lower()
    if p == "shopify": return shopify
    if p == "etsy":    return etsy
    if p in ("site", "website"): return site
    raise ValueError(f"Unsupported platform: {platform}")
