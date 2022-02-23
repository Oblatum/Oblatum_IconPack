import re
import os

drawable_path = os.path.join(os.getcwd(), os.path.dirname('app/src/main/assets/'), 'drawable.xml')
iconpack_path = os.path.join(os.getcwd(), os.path.dirname('app/src/main/res/values/'), 'icon_pack.xml')

if not os.path.exists(drawable_path):
    print("没有找到 drawable.xml，请确认当前工作目录为图标包根目录，其中应该包含 gradle, app 文件夹。")
    exit()

file_template = """
<?xml version="1.0" encoding="UTF-8"?>
<resources xmlns:tools="http://schemas.android.com/tools" tools:ignore="MissingTranslation">
    <string-array name="icons_preview">
{array_item}
    </string-array>
</resources>
"""

item_template = "\t<item>{icon_name}</item>\n"

file_content = ""

with open(drawable_path, 'r') as f:
    regex = r"^\s+<item\sdrawable=\"(\S+)\" \/>$"
    matches = re.finditer(regex, f.read(), re.MULTILINE)

    array = []

    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            array.append(item_template.format(icon_name=match.group(groupNum)))

    array = list(dict.fromkeys(array))
    array.sort()

    file_content = file_template.format(array_item=str.join("", array)).strip()

with open(iconpack_path, "w") as f:
    f.write(file_content)

print(iconpack_path)
