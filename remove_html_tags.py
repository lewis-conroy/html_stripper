def remove_html_tags(string):
    data = string.replace(string[string.find("<"):string.find(">") + 1], '').strip()
    if ">" in data or "<" in data:
        return remove_html_tags(data)
    else:
        return str(data)
