def get_sum_of_all_integers_in_file(file_path=r"C:\Users\ak\Desktop\kodutoo_8.txt"):
    with open(file_path) as f:
        data = f.read() 
    split_data = data.split("\n")
    split_data
    a = []
    for i in split_data:
        try:
            a.append(int(i))
        except:
            pass
    return sum(a)