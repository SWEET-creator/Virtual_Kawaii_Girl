import pandas as pd

def add_comment_to_csv(user_comment):
    file_path = "./comment.csv"
    # CSVファイルを読み込む
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=['index', 'comment'])
    
    # 新しいコメントをDataFrameに追加
    new_index = df['index'].max() + 1 if not df.empty else 0
    new_row = pd.DataFrame({'index': [new_index], 'comment': [user_comment]})
    df = pd.concat([df, new_row], ignore_index=True)
    
    # 変更をCSVファイルに保存
    df.to_csv(file_path, index = False)
    print(f"Comment '{user_comment}' has been added.")


text = input()
add_comment_to_csv(text)
