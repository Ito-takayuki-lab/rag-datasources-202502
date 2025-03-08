import os
import sys

def get_total_pdf_size(folder_path):
    """
    指定したフォルダ内のPDFファイルのサイズを取得し、合計サイズを返す関数

    Parameters:
        folder_path (str): フォルダのパス

    Returns:
        int: PDFファイルの合計サイズ（バイト単位）
    """
    total_size = 0
    
    folder_path = os.path.abspath(folder_path) 

    if not os.path.exists(folder_path):
        print(f"エラー: 指定されたフォルダ '{folder_path}' は存在しません。")
        return 0   
    total_count = 0
    # フォルダ内のファイルを走査
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename, f"{filename}.md")

        # PDFファイルかつファイルであることを確認
        if file_path.lower().endswith(".md") and os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            print("ファイル名: ", file_path)
            print("ファイルサイズ(バイト): ", file_size)
            total_size += file_size
            total_count += 1

    return total_size, total_count

# 使用例
if __name__ == "__main__":
    # コマンドライン引数のチェック
    if len(sys.argv) < 2:
        print("使い方: python script.py <フォルダの相対パス>")
        sys.exit(1)

    folder_path = sys.argv[1]
    total_size, total_count = get_total_pdf_size(folder_path)

    print("フォルダパス: ",folder_path)
    print("ファイルの数", total_count)
    print(f"PDFファイルの合計サイズ: {total_size} バイト")
    print(f"PDFファイルの合計サイズ: {total_size / 1024:.2f} KB")
    print(f"PDFファイルの合計サイズ: {total_size / (1024*1024):.2f} MB")
