import re
text="""キリンは大昔から __複数名詞__の興味の対象でした。キ
リンは__複数名詞__の中で一番背が高いですが。科学者たちはそのよ
うな長い__体の一部__をどうやって獲得したのか説明できません。キ
リンの長い身長は__数値__ __単位__ 近くあり、その高さはほとんどは脚と
__体の一部__によるものです"""
def mad_libs(mls):
    """
    :param mls: 文字列で、ユーザーに入力してもらいたい単語(=
    ヒント)の部分は後を二つのアンダースコアで挟んでください。ヒントの単
    語にはアンダースコアを含めないでください。__hint_hint__はだめで
    す。__hint__はokです。
    """
    hints=re.findall("__.*?__",mls)
    if hints is not None:
        for word in hints:
            q="{}を入力:".format(word)
            new=input(q)
            mls=mls.replace(word,new,1)
        print('\n')
        mls=mls.replace("\n", "")
        print(mls)
    else:
        print("引数mlsが無効です")
mad_libs(text)