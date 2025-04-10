import os

LEVELS = ["N5", "N4", "N3", "N2", "N1"]

for level in LEVELS:
    path = os.path.join(os.getcwd(), level)
    if not os.path.isdir(path):
        continue

    entries = sorted(os.listdir(path))
    md_links = []

    for file in entries:
        if file.endswith(".md"):
            name = file[:-3]  # 去掉 .md
            md_links.append(f"- [{name}](./{file})")

    if md_links:
        index_path = os.path.join(path, "index.md")
        with open(index_path, "w", encoding="utf-8") as f:
            f.write(f"# 📒 {level} 听力笔记索引\n\n")
            f.write("\n".join(md_links))
        print(f"✅ 已生成：{level}/index.md")
    else:
        print(f"⚠️ 目录 {level} 下无 .md 文件")
