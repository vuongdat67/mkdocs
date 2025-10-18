# scripts/gen_index.py
from pathlib import Path
import mkdocs_gen_files

docs_dir = Path("docs")
index_lines = [
    "# Home\n",
    "## 📚 Documentation Overview\n",
    "---\n",
    "<div class='bar-list' markdown>\n"
]

for md_path in sorted(docs_dir.rglob("*.md")):
    if md_path.name == "index.md":
        continue

    rel_path = md_path.relative_to(docs_dir)
    title = md_path.stem.replace("_", " ").title()
    index_lines.append(f"- [{title}]({rel_path.as_posix()})\n")

index_lines.append("</div>\n")

# Ghi tạm vào bộ nhớ build của MkDocs
with mkdocs_gen_files.open("index.md", "w") as f:
    f.write("\n".join(index_lines))
