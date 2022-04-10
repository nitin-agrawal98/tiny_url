def get_base62_string_from_id(pk_id):
    characters_to_be_present = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    short_url = ''
    while pk_id > 0:
        short_url += characters_to_be_present[pk_id % 62]
        pk_id = pk_id // 62
    return short_url[::-1]


def get_pk_id_from_base62_string(base62_string):
    pk_id = 0
    for c in base62_string:
        if 'a' <= c <= 'z':
            pk_id = pk_id * 62 + ord(c) - ord('a')
        elif 'A' <= c <= 'Z':
            pk_id = pk_id * 62 + ord(c) - ord('A') + 26
        else:
            pk_id = pk_id * 62 + ord(c) - ord('0') + 52
    return pk_id
