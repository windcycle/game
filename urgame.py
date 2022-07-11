import random
pilihan='y'

while pilihan.lower()=="y":
    list=["gunting", "batu", "kertas"]
    bot=random.choice(list)
    
    print()
    print("="*30)
    print("Game Gunting Batu Kertas")
    print("="*30, "\n")
    player=input("Masukkan pilihan: ")
    if player.lower()==bot:
        print()
        print("="*30)
        print("Hasil sulit seri")
        print('='*30, "\n")
    elif player.lower()=="gunting":
        if bot=="batu":
            print()
            print("="*30)
            print("kamu kalah :", player, "\n COM:", bot)
            print('='*30, "\n")
        else:
            print()
            print("="*30)
            print("kamu menang :", player, "\n COM:", bot)
            print('='*30, "\n")
    elif player.lower()=="batu":
        if bot=="kertas":
            print()
            print("="*30)
            print("kamu kalah :", player, "\n COM:", bot)
            print('='*30, "\n")
        else:
            print()
            print("="*30)
            print("kamu menang :", player, "\n COM:", bot)
            print('='*30, "\n")
    elif player.lower()=="kertas":
        if bot=="gunting":
            print()
            print("="*30)
            print("kamu kalah :", player, "\n COM:", bot)
            print('='*30, "\n")
        else:
            print()
            print("="*30)
            print("kamu menang :", player, "\n COM:", bot)
            print('='*30, "\n")
    else:
        print("Pilihan kamu salah")
    pilihan =input("apakah anda ingin bermain kembali? [y/n]: ")
print("anda keluar dari permainan")
