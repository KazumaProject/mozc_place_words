#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
places.tsv と words.tsv を読み込み、
Kotlin の Dictionary リスト形式のファイルを出力します。
"""

def process_places(file_path):
    result = []
    with open(file_path, encoding="utf-8") as f:
        # ヘッダー行をスキップ
        for line in f.readlines()[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) >= 2:
                yomi, tango = parts[0], parts[1]
                result.append(
                    f'    Dictionary(yomi = "{yomi}", leftId = 1924, rightId = 1924, cost = 4000, tango = "{tango}")'
                )
    return result

def process_words(file_path):
    result = []
    with open(file_path, encoding="utf-8") as f:
        # ヘッダー行をスキップ
        for line in f.readlines()[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) >= 3:
                yomi, tango, pos = parts[0], parts[1], parts[2]
                # 品詞に応じて ID を選択
                if "名詞サ変" in pos:
                    id_val = 1841
                elif "人名" in pos:
                    id_val = 1921
                elif "固有名詞" in pos:
                    id_val = 1920
                elif "姓" in pos:
                    id_val = 1923
                elif "名" in pos:
                    id_val = 1922
                else:
                    id_val = 1851
                result.append(
                    f'    Dictionary(yomi = "{yomi}", leftId = {id_val}, rightId = {id_val}, cost = 4000, tango = "{tango}")'
                )
    return result

def main():
    with open("dictionary_output.kt", "w", encoding="utf-8") as f:
        # PLACE セクション
        f.write("val PLACE = listOf(\n")
        f.write(",\n".join(process_places("places.tsv")))
        f.write("\n)\n\n")

        # WORDS セクション
        f.write("val WORDS = listOf(\n")
        f.write(",\n".join(process_words("words.tsv")))
        f.write("\n)\n")

if __name__ == "__main__":
    main()
