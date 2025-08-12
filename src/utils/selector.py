def xPathSelector(attr: str, key: str) -> str:
    return f"//*[@{attr}='{key}']"

def xPathByElementKey(key: str) -> str:
    return xPathSelector('data-element-key', key)