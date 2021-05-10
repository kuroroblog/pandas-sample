import pandas as pd

# sample.csvファイルを読み込む。
df = pd.read_csv('./sample.csv')

# お店の一覧を格納する変数を宣言する。
shopNameList = []

# 最終的に出力するデータ群を宣言する。
outputData = [['A', 'B', 'C', 'D', 'E']]

# csv情報を1行ずつ読み出す。
# iterrows参考 : https://note.nkmk.me/python-pandas-dataframe-for-iteration/
for index, row in df.iterrows():
    # A列に含まれるお店の名前を格納する。
    shopName = row[0]
    # B列に含まれる商品の名前を格納する。
    productName = row[1]

    # 既にお店一覧(shopNameList)内にお店が登録されているのか確認する。
    # 登録されている場合
    if shopName in shopNameList:
        # 最終的なデータ形式として、[[A店, 商品A, 商品B], [B店, 商品A, 商品C], [C店, 商品B] ...]を目指す。
        # 既存で登録されているお店が格納される位置をindex関数を利用して探索する。
        # indexについて : https://www.javadrive.jp/python/list/index10.html
        # +1しているのは、outputDataの一行目にA, B, C, D, Eが既に格納されているため。
        # appendを活用して、商品の名前を末尾に格納する。
        outputData[shopNameList.index(shopName) + 1].append(productName)
    # 登録されていない場合
    else:
        # 最終的なデータ形式として、[[A店, 商品A, 商品B], [B店, 商品A, 商品C], [C店, 商品B] ...]を目指す。
        # 新規お店の登録と商品の登録を行う。
        outputData.append([shopName, productName])
        # 新規でお店を登録する。
        shopNameList.append(shopName)

# 2次元配列をデータフレーム形式に変更する。
# csvファイル名をoutput.csvとしてcsvを生成する。
# header, indexを付与しないように、header=False, index=Falseとする。
# to_csvについて : https://note.nkmk.me/python-pandas-to-csv/
pd.DataFrame(outputData).to_csv('./output.csv', header=False, index=False)
