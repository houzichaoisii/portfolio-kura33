pop=[] #洋楽ポップを保存するリスト
jpop=[] #jpopソングを保存するリスト
def collect_songs():
    song="曲名を入力してください->"
    ask="pかjのどちらかを入力して下さい、qで終わります->"
    while True:
        genre=input(ask)
        if genre=="q":
            break
        if genre=="p":
            p=input(song)
            pop.append(p)
        elif genre=="j":
            j=input(song)
            jpop.append(j)
        else:
            print("pかjのどちらかを入力して下さい、qで終わります")
    print("pop songs:",pop)
    print("jpop songs:",jpop)
collect_songs()