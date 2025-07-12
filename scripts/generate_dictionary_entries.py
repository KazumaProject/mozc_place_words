def process_places(file_path):
    result = []
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 2:
                yomi, tango = parts[0], parts[1]
                result.append(f'    Dictionary(yomi = "{yomi}", leftId = 1924, rightId = 1924, cost = 4000, tango = "{tango}")')
    return result

def process_words(file_path):
    result = []
    with open(file_path, encoding="utf-8") as f:
        lines = f.readlines()[1:]
        for line in lines:
            if not line.strip():
                continue
            parts = line.strip().split("\t")
            if len(parts) >= 3:
                yomi, tango, pos = parts[0], parts[1], parts[2]
                if "名詞サ変" in pos:
                    id_val = 1841
                elif "人名" in pos:
                    id_val = 1921
                elif "固有名詞" in pos:
                    id_val = 1920
                elif "名" in pos:
                    id_val = 1922
                elif "姓" in pos:
                    id_val = 1923
                else:
                    id_val = 1851
                result.append(f'    Dictionary(yomi = "{yomi}", leftId = {id_val}, rightId = {id_val}, cost = 4000, tango = "{tango}")')
    return result

def main():
    with open("dictionary_output.kt", "w", encoding="utf-8") as f:
        f.write("val PLACE = listOf(\n")
        f.write(",\n".join(process_places("places.tsv")))
        f.write("\n)\n\n")
        f.write("val WORDS = listOf(\n")
        f.write(",\n".join(process_words("words.tsv")))
        f.write("\n)")

if __name__ == "__main__":
    main()
