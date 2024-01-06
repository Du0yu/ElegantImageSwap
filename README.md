# ElegantImageSwap 重链

轻松替换`markdown`图片链接，使用`Python`实现。/ Effortlessly replace `markdown` image links using Python.

---

## 开发缘由 Reasons for Development

期末复习的时候获取到了学长学姐共享的笔记，开心的是他提供了`markdown`与`pdf`两个版本，不开心的是markdown文件没有提供图片资源。为了恢复图片资源的链接，写了这个小工具。/ During final exam review, I obtained notes shared by senior students. While it was great that they provided both `markdown` and `pdf` versions, I was disappointed to find that the markdown file did not include image resources. To restore the image resource links, I developed this small tool.

## 使用前提 / Prerequisites

1. 同时有 markdown 和 pdf 两版文件。/ Both markdown and pdf versions of the file are available. 
2. 使用 `Adobe Acrobat` 等软件导出 PDF 中的图片。 / Use software like `Adobe Acrobat` to export images from the PDF.   
   1. 点击导出 PDF 选项卡 -> 图像 -> 勾选导出所有图像。 / Click on the export PDF tab -> Images -> Check 'Export All Images'.   
   2. 点击导出。 / Click 'Export'. 
3. 将图片用 `PowerRename` 等工具重命名好，**图片名字里不要有空格**，并且放到一个文件夹里面。 / Rename the images using tools like `PowerRename`, ensuring that **there are no spaces in the image names**, and place them in a single folder.

## 使用方法 Usage

1. 克隆仓库。/ Clone the repository. 

2. 修改`replace_image.py`的代码。 / Modify the code in `replace_image.py`.

   1. 文件头的部分：/ In the file header section:

   ```python
   # Modify to the path of the markdown file to be modified
   file_name = "filename.md" # 修改为待修改markdown文件的路径 
   # Modify to the path for the output markdown file
   new_file_name = "filename_fixed.md" # 修改为输出markdown文件的路径 
   ```

   2. `replace_image_links`中：

   ```python
   # Modify according to your file names, where the {} represents the index value
   new_img_link = f"./path/image({img_counter}).jpg" # 此处按照你的文件名做修改 {}里面的是索引值
   ```

   3. 运行。 / Run the code.

