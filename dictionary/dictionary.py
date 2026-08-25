from pathlib import Path
import json
import re


# 加载词典
path = Path("dictionary.json")
english_dict = json.loads(path.read_text(encoding='utf-8'))

# 正则匹配参数格式：空格+参数 或 逗号+参数
pattern = re.compile(r"^(.+?)\s+-(e|c|i)$|^(.+?),(e|c|i)$")

while True:
    cmd = input("请输入要查询的词: ").strip()
    
    if cmd.lower() == "quit":
        break
    
    # 解析指令
    m = pattern.search(cmd)
    if m:
        if m.group(1):  # 空格格式
            search_word, mode = m.group(1), m.group(2)
        else:  # 逗号格式
            search_word, mode = m.group(3), m.group(4)
    else:
        # 无参数，默认英查中
        search_word, mode = cmd, "e"
    
    if mode == "e":
        # 英文精确查中文
        result = english_dict.get(search_word)
        print(f"{search_word}: {result if result else '没有这个单词呢...'}\n\n")
    elif mode == "i":
        # 英文模糊查中文（包含匹配）
        found = False
        for k, v in english_dict.items():
            if search_word.lower() in k.lower():
                print(f"{k}: {v}\n")  # 每个结果后面空1行（print自带的换行 + \n = 显示空1行）
                found = True
        if not found:
            # 没有结果：提示语后面直接空两行
            print(f"没有包含 '{search_word}' 的单词呢...\n\n")
        else:
            # 有结果：最后一个结果已经有\n了，再补一个print()（等价于再空1行）
            # 注意这里不要用print("\n")，因为print()本身会换行
            print()
    else:  # mode == "c"
        # 中文反向查英文
        found = False
        for k, v in english_dict.items():
            if search_word in v:
                print(f"{k}: {v}\n")
                found = True
        if not found:
            # 没有结果：提示语后面直接空两行
            print("没有这个单词呢...\n\n")
        else:
            # 有结果：最后一个结果已经有\n了，再补一个print()
            print()
