
import hashlib
import json
import sys
from pathlib import Path

def get_hash(path):
    sha = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha.update(chunk)
    return sha.hexdigest()

def scan(folder):
    result = {}
    for path in sorted(Path(folder).rglob("*")):
        if path.is_file() and not path.is_symlink():
            result[str(path.relative_to(folder))] = get_hash(path)
    return result

def main():
    if len(sys.argv) != 4:
        print("Usage: python integrity_monitor.py "
              "baseline/check folder baseline.json")
        return

    command, folder, baseline = sys.argv[1:]
    folder = Path(folder)

    if not folder.is_dir():
        print("Folder not found.")
        return

    if command == "baseline":
        data = scan(folder)
        Path(baseline).write_text(json.dumps(data, indent=2))
        print("Baseline created:", len(data), "files")
    elif command == "check":
        saved = json.loads(Path(baseline).read_text())
        current = scan(folder)

        for name in sorted(saved.keys() | current.keys()):
            if name not in saved:
                print("ADDED:", name)
            elif name not in current:
                print("MISSING:", name)
            elif saved[name] != current[name]:
                print("MODIFIED:", name)

        if saved == current:
            print("PASS: No file changes detected.")
    else:
        print("Use baseline or check.")

if __name__ == "__main__":
    main()
