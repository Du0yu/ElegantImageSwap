import re

file_name = "软件工程导论PPT笔记.md"
new_file_name = "软件工程导论PPT笔记_portable.md"
def replace_image_links(markdown_text):
    # 匹配混合图片链接的模式
    mixed_img_pattern = r'(!\[[^\]]*\]\([^\)]*\))|(<img[^>]*>)'

    # 获取所有混合图片链接
    mixed_img_tags = re.findall(mixed_img_pattern, markdown_text)

    # 替换图片链接
    img_counter = 1
    for mixed_img_tag in mixed_img_tags:
        for img_tag in mixed_img_tag:
            if img_tag:
                new_img_link = f"./path/image({img_counter}).jpg"
                markdown_text = re.sub(re.escape(img_tag), f'![]({new_img_link})', markdown_text, count=1)
                img_counter += 1

    return markdown_text

# 读取 Markdown 文件内容
with open(file_name, 'r', encoding='utf-8') as file:
    markdown_content = file.read()

# 替换图片链接
new_markdown_content = replace_image_links(markdown_content)

# 将替换后的内容写回原始文件
with open(new_file_name, 'w', encoding='utf-8') as file:
    file.write(new_markdown_content)

print("图片链接替换完成！")
