'''
Nama   : Move Files By Ekstension
Version: 1.0
Date   : 31-08-2020
Blog   : https://pandasid.blogspot.com
Author : Pandas ID
Deskription: Silahkan kalian pelajari,kalau mau re-upload jangan lupa untuk mencantumkan
github pembuatnya (github saya)
'''


BANNER = '''
    █▀█ ▄▀█ █▄ █ █▀▄ ▄▀█ █▀
    █▀▀ █▀█ █ ▀█ █▄▀ █▀█ ▄█
    -----------------------
    Move Files By Extension
    -----------------------
'''

def get_data(ext):
    data = []
    for w in os.walk('/sdcard'):
        for l in os.listdir(w[0]):
            if ext in l:
                path = os.path.join(w[0], l)
                size = os.path.getsize(path)/1024
                data.append({'name':l, 'path':path, 'size':size})
    return data

def main():
    os.system('clear')
    print(BANNER)
    print('    Contoh: mp3')
    ext = input('    Masukan Extension: ')
    data = get_data('.'+ext)
    total_size = sum([sz['size'] for sz in data])

    # Menampilkan Hasil
    for show in data:
        if show['size'] > 1024:
            size = str(round(show['size']/1024))+' MB'
        else:
            size = str(round(show['size']))+' KB'
        print(f"\n    Nama File  : {show['name']}\n    Direktory  : {show['path']}\n    Ukuran File: {size}")
    print(f'\n    Jumlah File: {len(data)}')
    dest = input('\n    Pindahkan Ke Direktory: ')
    print('\n    NOTE: Memindahkan file secara Manual akan meminta persetujuan dahulu sebelum memindahkan,sedangkan Otomatis akan memindahkannya secara langsung tanpa meminta persetujuan')
    mode = input('    Pindahkan File Secara [M]anual/[O]tomatis: ').lower()
    moved, not_moved, located = [], [], []
    list_dir = os.listdir(dest)
    if mode == 'm' or mode == 'o':
        for x in data:
            if x['name'] in list_dir:
                located.append(x['name'])
            else:
                if mode == 'm':
                    tay = input(f'\n    Pindahkan {x["name"]} [y/t]: ').lower()
                    if tay == 'y':
                        shutil.move(x['path'], dest)
                        moved.append(x['name'])
                        located.append(x['name']+' (Baru Dipindahkan)')
                        print(f'    {x["name"]} Telah Dipindahkan')
                    else:
                        not_moved.append(x['name'])
                        print(f'    {x["name"]} Tidak Dipindahkan')
                elif mode == 'o':
                    shutil.move(x['path'], dest)
                    moved.append(x['name'])
                    located.append(x['name']+' (Baru Dipindahkan)')
                    print(f'    {x["name"]} Telah Dipindahkan')
    else:
        input('    Masukan Pilihan Yang Disediakan')
        main()
    print()
    print('RINCIAN'.center(70))
    print('    '+'-'*60)
    print('\n    File Yang Telah Dipindahkan')
    if len(moved) != 0:
        for m in moved:
            print(f'    {moved.index(m)+1}.) {m}')
        print(f'\n    Total: {len(moved)}')
    else:
        print('    -')
    print('\n    File Yang Tidak Dipindahkan')
    if len(not_moved) != 0:
        for n in not_moved:
            print(f'    {not_moved.index(n)+1}.) {n}')
        print(f'\n    Total: {len(not_moved)}')
    else:
        print('    -')
    print(f'\n    File Telah Berada Di Direktory {dest}')
    if len(located) != 0:
        for l in located:
            print(f'    {located.index(l)+1}.) {l}')
        print(f'\n    Total: {len(located)}')
    else:
        print('    -')
    print('    '+'-'*60)
    print('\n    Terima kasih telah menggunakan Tools kami:)\n    Jangan lupa untuk mengunjungi blog https://pandasid.blogspot.com')
if __name__ == '__main__':
    import os, shutil
    main()
