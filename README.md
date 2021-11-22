# html_stripper
Recursively strips HTML tags from a given input string. Works with XML too.

**Note:** If there is a < or > character in the desired output data, this function will not work.

```py
def remove_html_tags(string):
    data = string.replace(string[string.find("<"):string.find(">") + 1], '').strip()
    if ">" in data or "<" in data:
        return remove_html_tags(data)
    else:
        return str(data)
```
