import importlib.metadata
import sys

def get_version(package_name):
    try:
        return importlib.metadata.version(package_name)
    except importlib.metadata.PackageNotFoundError:
        return "Не установлен"

print(f"""
Версии пакетов:
- PyQt5: {get_version('PyQt5')}
- Plotly: {get_version('plotly')}
- Pandas: {get_version('pandas')}
- Requests: {get_version('requests')}
- Websocket-client: {get_version('websocket-client')}
Python: {sys.version}
""")