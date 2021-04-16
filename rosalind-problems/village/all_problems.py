# Variables and Some Arithmetic
from os import write


def find_hypotenuse(a, b):
    return (a**2) + (b**2)
# print(find_hypotenuse(844, 871))

# Working with String


def slice_string(str, a, b, c, d):
    return f"{str[a:b+1]} {str[c:d+1]}"


STR = "fkFw27n5O3KvoyoNW4IRAtheneXmmr9Q8fWahrFThifbeMB0RrJA0VN75IyBMMVvHkEjy0qHRHfan0bhIsubcinctusOBW0onu3KD1KhSv4roIUKCtR5vd2BD01Fw3zj8d60LVpKCtvvNBRAet1TSz10BcwgcjTnCmCbRLGPbOSbb4D."
# print(slice_string(STR, 20, 25, 81, 90))

# Conditions and Loops


def sum_odd_int(a, b):
    res = 0
    for i in range(a, b):
        if i % 2 == 1:
            res += i
    return res
# print(sum_odd_int(4264, 8780))

# Working with Files

def even_lines():
    f = open('file.txt', 'r')
    n = open("new_file.txt", "w")
    lines = f.readlines()
    count = 1

    for line in lines:
        if count % 2 == 0:
            n.write(line)
        count += 1

    n.close()
    f.close()
    return ""
# =========================


# Dictionaries
def word_count(str):
    count = {}
    for word in str.split(' '):
        if word not in count:
            count[word] = 1
        else:
            count[word] += 1
    for key, value in count.items():
        print(f"{key} {value}")


STR = "When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be"

word_count(STR)
# ==============================================================