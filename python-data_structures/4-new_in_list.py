#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Orijinal siyahının kopyasını yaradırıq
    new_list = my_list[:]
    
    # İndeksi yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return new_list
    
    # Dəyişikliyi yalnız kopya üzərində edirik
    new_list[idx] = element
    return new_list
