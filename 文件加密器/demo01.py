def transform(input_path, output_path, shift=3):
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()

    result = []
    for ch in text:
        if 'a' < ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' < ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    string = ''.join(result)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(string)

    print(f"加密完成，新文件：{output_path}")

transform("test.txt", "res.txt", 3)
