import io
def read_file_list(file_name):
    f = io.open(file_name, 'r', encoding='utf-8')
    ndung = f.read()
    f.close()
    return ndung.split('\n')

if __name__ =="__main__":
    file_name = 'dino.txt'
    L1 = read_file_list(file_name)

    file_name = 'trung_nghia.txt'
    L2 = read_file_list(file_name)
    
    L3 = list(set(L1) & set(L2))