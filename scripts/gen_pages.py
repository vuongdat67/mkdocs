from pathlib import Path
import mkdocs_gen_files

docs_dir = Path("docs")

# Chỉ generate cho study/ và subfolder
for folder in sorted(docs_dir.rglob("*/")):
    # Bỏ qua folder không cần
    skip = ['.obsidian', 'assets', 'css', 'blog', 'templates', 'overrides', 'posts']
    if any(s in folder.parts for s in skip):
        continue
    
    # Bỏ qua docs/ gốc
    if folder == docs_dir:
        continue
    
    # Lấy file .md và subfolder
    md_files = sorted([f for f in folder.glob("*.md") if f.name != "index.md"])
    subfolders = sorted([d for d in folder.glob("*/") if d.is_dir() and d.name not in skip])
    
    if not md_files and not subfolders:
        continue
    
    # Tạo nội dung
    folder_name = folder.name.replace("_", " ").replace("-", " ").title()
    lines = [f"# {folder_name}\n\n"]
    
    if subfolders:
        lines.append("## 📁 Folders\n\n")
        for sf in subfolders:
            name = sf.name.replace("_", " ").replace("-", " ").title()
            lines.append(f"- [{name}]({sf.name}/)\n")
        lines.append("\n")
    
    if md_files:
        lines.append("## 📄 Files\n\n")
        for mf in md_files:
            # Đọc title
            title = mf.stem.replace("_", " ").replace("-", " ").title()
            try:
                content = mf.read_text(encoding="utf-8")
                if content.startswith("---"):
                    fm = content.split("---")[1]
                    for line in fm.split("\n"):
                        if "title:" in line:
                            title = line.split(":", 1)[1].strip().strip('"\'')
                            break
            except:
                pass
            
            lines.append(f"- [{title}]({mf.name})\n")
    
    # Ghi file
    index_path = folder.relative_to(docs_dir) / "index.md"
    with mkdocs_gen_files.open(str(index_path), "w") as f:
        f.writelines(lines)

print("✅ Generated index for study folders")