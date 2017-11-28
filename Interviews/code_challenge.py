pattern = "abcdefghijklmnopqrstuvwxyz"


def decrypt(encrypted_message):
    global pattern
    key = cal_key()
    print(key)
    index_key = 0
    message = list()
    for i in range(len(encrypted_message)):
        letter = encrypted_message[i]
        if letter.lower() not in pattern:
            message.append(letter)
            continue
        message.append(rotate(letter, key[index_key]))
        index_key = index_key + 1 if index_key + 1 < len(key) else 0
    return ''.join(message)


# Calculate the whole key which encrypt "Your friend, Alice" into "Atvt hrqgse, Cnikg"
def cal_key():
    global pattern
    signature = "-Atvt hrqgse, Cnikg".lower()
    text = "yourfriendalice"
    i_text = 0
    key = list()
    for letter in signature:
        if letter not in pattern:
            continue
        index_sig = pattern.index(letter)
        index_text = pattern.index(text[i_text])
        rotate_times = abs(index_sig - index_text)
        rotate_times = rotate_times if rotate_times < 10 else 26 - rotate_times
        # print(f"from {text[i_text]} to {letter} rotate {rotate_times}")
        i_text += 1
        key.append(str(rotate_times))
    return refine_key(''.join(key))


# Calculate the exact key.
def refine_key(key):
    count = len(key)
    pattern_start = False
    un_rotated_key = ""
    for i in range(1, len(key)):
        if pattern_start and key.count(key[:i]) < count:
            un_rotated_key = key[:i-1]
            break
        if key.count(key[:i]) == count:
            pattern_start = True
        count = key.count(key[:i])
    text = "Otjfvknou kskgnl K mbxg iurtsvcnb ksgq hoz atv Vje xcxtyqrl vt ujg smewfv vrmcxvtg rwqr ju vhm ytsf elwepuqyez"
    delta_index_from_end = (len(text) - text.count(' ')) % len(un_rotated_key)
    index_start = len(un_rotated_key) - delta_index_from_end
    return un_rotated_key[index_start:] + un_rotated_key[:index_start]


def rotate(letter, times):
    global pattern
    lower_letter = letter.lower()
    index_new = pattern.index(lower_letter) - int(times)
    index_new = index_new + 26 if index_new < 0 else index_new
    return pattern[index_new] if letter == lower_letter else pattern[index_new].upper()


decrypt("")