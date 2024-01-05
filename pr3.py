import json

json_file = open('eng_data.json', 'r',encoding="utf-8")

json_data = json_file.read()

#parse to class
obj = json.loads(json_data)

global_str = ""
kullanici_counter = 0
#stop_words_arindirilmis.txt'ye yazdırma
without_stop_words = open('without_stop_words.txt', 'w',encoding="utf-8")
last_words = open('last_words_en.txt', 'w',encoding="utf-8")

users = open('users.txt', 'w',encoding="utf-8")

class fake_list_node:
    def __init__(self, a):
        self.a = a
        self.next = None
    def get_a(self):
        return self.a  

class FakeList:
    def __init__(self):
        self.head = None
        self.end = None
    def sona_ekle(self, data):
        new_node = fake_list_node(data)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = new_node



#stop words file to fakeList
stop_words = open('stop_words_en.txt', 'r',encoding="utf-8")
stop_words_data = stop_words.read()
stop_words_list = FakeList()
while stop_words_data.find("\n") != -1:
    stop_words_list.sona_ekle(stop_words_data[:stop_words_data.find("\n")])
    #print(stop_words_data[:stop_words_data.find("\n")] + " eklendi")
    stop_words_data = stop_words_data[stop_words_data.find("\n")+1:]


class stop_words_node:
    def __init__(self, harf, list):
        self.harf = harf
        self.list = list
        self.next = None
    def get_harf(self):
        return self.harf
    def get_list(self):
        return self.list

class stop_words_list_letter:
    def __init__(self):
        self.head = None
        self.end = None
    def sona_ekle(self, harf, list):
        new_node = stop_words_node(harf, list)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = new_node

bas = stop_words_list.head
stop_words_list_2_ = stop_words_list_letter()
str_letter = ""
while bas:
    if bas.get_a()[0] not in str_letter:
        str_letter += bas.get_a()[0]
        stop_words_list_2_.sona_ekle(bas.get_a()[0], FakeList())
    bas2 = stop_words_list_2_.head
    while bas2:
        if bas2.get_harf() == bas.get_a()[0]:
            bas2.get_list().sona_ekle(bas.get_a())
            break
        bas2 = bas2.next
    bas = bas.next


test_stop_words_list = open('test_stop_words_list.txt', 'w',encoding="utf-8")
bas = stop_words_list_2_.head
while bas:
    test_stop_words_list.write(bas.get_harf() + " ")
    bas2 = bas.get_list().head
    while bas2:
        test_stop_words_list.write(bas2.get_a() + " ")
        bas2 = bas2.next
    test_stop_words_list.write("\n")
    bas = bas.next



class Kullanici:
    all_tweets_temp2 = ""
    def init_kelimeler(self,tweets):
        bas = tweets.head
        global global_str
        all_tweets = ""
        while bas:
            all_tweets += bas.get_a()[:-1] + " " #cumle sonundaki noktalari bosluga donusturduk

            bas = bas.next
        
        #tüm noktalama işaretlerini sil
        #text = text.translate(str.maketrans("", "", string.punctuation)) kullanacaktık lakin yasaktır diye tek tek yaptık :D
            
        all_tweets = all_tweets.replace(",","")
        all_tweets = all_tweets.replace(":","")
        all_tweets = all_tweets.replace(";","")
        all_tweets = all_tweets.replace('"', '')
        all_tweets = all_tweets.replace("%", "")
        all_tweets = all_tweets.replace("$", "")
        all_tweets = all_tweets.replace("&", "")
        all_tweets = all_tweets.replace('\\', "")
        all_tweets = all_tweets.replace('/', "")
        all_tweets = all_tweets.replace('(', "")
        all_tweets = all_tweets.replace(')', "")
        all_tweets = all_tweets.replace('=', "")
        all_tweets = all_tweets.replace('*', "")
        all_tweets = all_tweets.replace('+', "")
        all_tweets = all_tweets.replace('-', "")
        all_tweets = all_tweets.replace('<', "")
        all_tweets = all_tweets.replace('>', "")
        all_tweets = all_tweets.replace('@', "")
        all_tweets = all_tweets.replace('[', "")
        all_tweets = all_tweets.replace(']', "")
        all_tweets = all_tweets.replace('^', "")
        all_tweets = all_tweets.replace('_', "")
        all_tweets = all_tweets.replace('`', "")
        all_tweets = all_tweets.replace('{', "")
        all_tweets = all_tweets.replace('}', "")
        all_tweets = all_tweets.replace('~', "")
        all_tweets = all_tweets.replace('|', "")
        all_tweets = all_tweets.replace('\'', "")
        all_tweets = all_tweets.replace('’', "")
        all_tweets = all_tweets.replace('‘', "")
        all_tweets = all_tweets.replace('“', "")
        all_tweets = all_tweets.replace('”', "")
        all_tweets = all_tweets.replace('…', "")
        all_tweets = all_tweets.replace('.', "")
        all_tweets = all_tweets.replace('!', "")
        all_tweets = all_tweets.replace('?', "")
    
               
        all_tweets = all_tweets.lower() # buyuk harfleri kucuk harfe cevirdik
        #print(all_tweets)
        all_tweets_temp = all_tweets
        #self.set_all_teets_str(all_tweets_temp)
        #self.all_tweets_str = all_tweets_temp
        self.all_tweets_temp2 = all_tweets_temp
        global_str += all_tweets_temp

        kelime_list = FakeList() #sonra ayarla ilk stringe
        while all_tweets_temp.find(" ") != -1:
            kelime_list.sona_ekle(all_tweets_temp[:all_tweets_temp.find(" ")])
            all_tweets_temp = all_tweets_temp[all_tweets_temp.find(" ")+1:]
        
        bas_test = kelime_list.head

        global kullanici_counter

        without_stop_words.write(self.name +  " " +str(kullanici_counter)+"\n")
        kullanici_counter += 1
        return_kelime_list = FakeList()
        while kelime_list.head:
            deger = kelime_list.head.get_a()
            #listede gez var mi kontrol et varsa continue
            bas_return = return_kelime_list.head
            inside_flag = 0
            while(bas_return):
                if deger == bas_return.get_a():
                    inside_flag = 1
                    break
                bas_return = bas_return.next
            if(inside_flag == 1):
                kelime_list.head = kelime_list.head.next
                continue

            bas_test = kelime_list.head
            sayac = 0
            while bas_test:
                if bas_test.get_a() == deger:
                    sayac += 1
                bas_test = bas_test.next
            #if sayac == 1:
            #   return_kelime_list.sona_ekle(deger)
            if sayac > 1:
                bas2 = stop_words_list_2_.head
                flag = 0
                while(bas2):
                    if deger != "" and deger[0] == bas2.get_harf():
                        bas3 = bas2.get_list().head
                        while(bas3):
                            if deger == bas3.get_a():
                                flag = 1
                                break
                            bas3 = bas3.next
                        if(flag == 1):
                            break
                    bas2 = bas2.next
                if(flag == 0):
                    return_kelime_list.sona_ekle(deger)
                    without_stop_words.write(deger + " " + str(sayac) + "\n")
            kelime_list.head = kelime_list.head.next
        return return_kelime_list

    def __init__(self,username,name,followers_count,following_count,language,region,tweets,following,followers,ortak_kullanicilar ,hash_vocabs ):
        self.username = username
        self.name = name
        self.followers_count = followers_count
        self.following_count = following_count
        self.language = language
        self.region = region
        
        self.tweets = tweets
        self.following = following
        self.followers = followers
        self.kelimeler = self.init_kelimeler(tweets)
        self.ortak_kullanicilar = ortak_kullanicilar
        self.hash_vocabs = hash_vocabs
        self.all_tweets_str = ""
    def set_all_teets_str(self, all_tweets_str):
        self.all_tweets_str = all_tweets_str
   
user_counter = 0
linked_list = FakeList()
for e in obj:
    users.write(str(user_counter) + " " + str(e['username']) + "\n")
    user_counter += 1
    str1 = str(e['username'])
    str2 = str(e['name'])
    int1 = int(e['followers_count'])
    int2 = int(e['following_count'])
    str3 = str(e['language'])
    str4 = str(e['region'])
    
    list1 = list(e['tweets'])
    linked_list1 = FakeList() #tweetler
    for i in list1: 
        linked_list1.sona_ekle(i) 

    list2 = list(e['following'])
    linked_list2 = FakeList() # takip edilenler
    for i in list2:
        linked_list2.sona_ekle(i)

    list3 = list(e['followers']) #takipciler
    linked_list3 = FakeList()
    for i in list3:
        linked_list3.sona_ekle(i)

    linked_list.sona_ekle(Kullanici(str1,str2,int1,int2,str3,str4,linked_list1,linked_list2,linked_list3, FakeList(), FakeList()))
#frekans denemesi

from collections import Counter
import re

kelimeler = re.findall(r'\b\w+\b', global_str.lower())
sayac = Counter(kelimeler)
l_temp = sayac.most_common(500)
#print(type(sayac.most_common(1000)))
#print(l_temp)

#print("yaziyorr!!!")
for e in l_temp:
    bas = stop_words_list.head
    flag = 0
    while(bas):
        if e[0] == bas.get_a():
            flag = 1
            break
        bas = bas.next
    if flag == 0: 
        last_words.write(e[0] + "\n")

#close users.txt
users.close()

#YENİ

import networkx as nx
import matplotlib.pyplot as plt
kullanici_name = input("users.txt dosyasına bakarak grafını örnek istediğiniz kullanici ismini giriniz: ")


G = nx.DiGraph()

node_label_options = {
    "font_size": 5,
    "font_color": "blue",
    "verticalalignment": "bottom",
    "horizontalalignment": "left"
}

node_options = {"node_color": "red", "node_size": 50}

edge_options = {"width": .50, "alpha": .5, "edge_color": "black"}

selected_user = open('selected_user.txt', 'w',encoding="utf-8")

bulundu = 0
bas = linked_list.head
while bas:
    if bas.get_a().username == kullanici_name:
        bulundu = 1
        G.add_node(bas.get_a().username, pos=(100, 100))
        selected_user.write("SECİLEN KULLANICI: ")
        selected_user.write(bas.get_a().username + "\n")
        bas2 = bas.get_a().following.head
        selected_user.write("TAKİP ETTİKLERİ: \n")
        while bas2:
            G.add_edge(bas.get_a().username, bas2.get_a())
            selected_user.write(bas2.get_a() + "\n")
            bas2 = bas2.next
        bas3 = bas.get_a().followers.head
        selected_user.write("TAKIPCILERI: \n")
        while bas3:
            G.add_edge(bas3.get_a(),bas.get_a().username)
            selected_user.write(bas3.get_a() + "\n")
            bas3 = bas3.next
        break
    bas = bas.next

selected_user.close()


if bulundu == 0:
    print("Kullanıcı bulunamadı.")
    exit(0)

plt.figure(figsize=(10,8))
pos = nx.circular_layout(G)
center = (0, 0)
pos[bas.get_a().username] = center

nx.draw_networkx_nodes(G, pos, **node_options)
nx.draw_networkx_edges(G, pos, **edge_options)
nx.draw_networkx_labels(G, pos, **node_label_options)
plt.show()

print("hash node giris")

class hash_node:
    def __init__(self, key, fake_list):
        self.key = key
        self.fake_list = fake_list
        self.next = None
    def get_key(self):
        return self.key
    def get_fake_list(self):
        return self.fake_list

class HashTable:
    def __init__(self):
        self.head = None
        self.end = None
        self.size = 0
    def hash_node_ekleme(self, key, fake_list):
        new_node = hash_node(key, fake_list)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            self.size += 1
            return
        self.end.next = new_node
        self.end = new_node
        self.size += 1


last_words.close()

last_words_read = open('last_words_en.txt', 'r',encoding="utf-8")
last_words_read_data = last_words_read.read()
last_words_list = FakeList()
while last_words_read_data.find("\n") != -1:
    last_words_list.sona_ekle(last_words_read_data[:last_words_read_data.find("\n")])
    #print(last_words_read_data[:last_words_read_data.find("\n")])
    last_words_read_data = last_words_read_data[last_words_read_data.find("\n")+1:]

print("hash node ekleme basliyor")
hash_table = HashTable()
bas = last_words_list.head
while bas:
    hash_table.hash_node_ekleme(bas.get_a(), FakeList())
    bas = bas.next

print("hash node ekleme list ayarlama")#alttakinde ariza var!! onsuz döngü
bas = linked_list.head
while bas:
    bas2 = bas.get_a().kelimeler.head
    while bas2:
        bas3 = hash_table.head
        while bas3:
            if bas2.get_a() == bas3.get_key():
                bas3.get_fake_list().sona_ekle(bas.get_a().username)
                break
            bas3 = bas3.next
        bas2 = bas2.next
    bas = bas.next

print("dosya cikti gosterme")
hash_cikti = open('hash_cikti.txt', 'w',encoding="utf-8")
bas = hash_table.head
while bas:
    hash_cikti.write(bas.get_key() + " ")
    bas2 = bas.get_fake_list().head
    while bas2:
        hash_cikti.write(bas2.get_a() + " ")
        bas2 = bas2.next
    hash_cikti.write("\n\n\n")
    bas = bas.next

#bölgeler- last_words listesinden varsa en çok geçen 10 kelimeyi yazdırma
   
class region_or_lang_node:
    def __init__(self, region_name):
        self.region_name = region_name
        self.region_str = ""
        self.next = None
    def get_region_name(self):
        return self.region_name
    def get_region_str(self):
        return self.region_str
    def set_region_str(self, region_str):
        self.region_str = region_str

    
class region_or_lang_list:
    def __init__(self):
        self.head = None
        self.end = None
    def sona_ekle(self, region_name):
        new_node = region_or_lang_node(region_name)
        if self.head is None:
            self.head = new_node
            self.end = new_node
            return
        self.end.next = new_node
        self.end = new_node

region_test = open('region_test.txt', 'w',encoding="utf-8")
region_test2 = open('region_test2.txt', 'w',encoding="utf-8")
region_tweet = open('region_tweet.txt', 'w',encoding="utf-8")

bas = linked_list.head
region_list_ = region_or_lang_list()
while bas:
    #region_test2.write(bas.get_a().all_tweets_str + "\n")
    bas2 = region_list_.head
    flag = 0
    while bas2:
        if bas.get_a().region == bas2.get_region_name():
            region_str = bas2.get_region_str()  
            region_str += bas.get_a().all_tweets_temp2+ " "
            region_test.write(bas.get_a().all_tweets_temp2 + "\n")
            bas2.set_region_str(region_str)  
            flag = 1
            break
        bas2 = bas2.next
    if flag == 0:
        region_list_.sona_ekle(bas.get_a().region)
        region_end = region_list_.end
        region_str = bas.get_a().all_tweets_temp2 + " "
        region_test.write(bas.get_a().all_tweets_temp2 + "\n") 
        region_end.set_region_str(region_str)
    bas = bas.next

bas = region_list_.head
while bas:
    region_test2.write(bas.get_region_name() + " -> " + bas.get_region_str() + "\n")
    ona_kadar = 0
    region_tweet.write(bas.get_region_name() + " -> ")
    str_temp = bas.get_region_str()
    kelimeler = re.findall(r'\b\w+\b', str_temp.lower())
    sayac = Counter(kelimeler)
    l_temp = sayac.most_common(100)
    words_only = [word for word, count in l_temp]
    for s in words_only:
        bas2 = stop_words_list_2_.head
        on_kontrol = 0
        while bas2:
            if s[0] == bas2.get_harf():
                bas3 = bas2.get_list().head
                flag = 0
                while bas3:
                    if s == bas3.get_a():
                        flag = 1
                        break
                    bas3 = bas3.next
                if flag == 0:
                    region_tweet.write(s + " ")
                    ona_kadar += 1
                    if(ona_kadar == 10):
                        on_kontrol = 1
                        break
            bas2 = bas2.next
        if(on_kontrol == 1):
            break        
            
       
    region_tweet.write("\n\n")
    bas = bas.next

print("region bitti")

lang_write = open('lang_write.txt', 'w',encoding="utf-8")

bas = linked_list.head
lang_list_ = region_or_lang_list()
while bas:
    #region_test2.write(bas.get_a().all_tweets_str + "\n")
    bas2 = lang_list_.head
    flag = 0
    while bas2:
        if bas.get_a().language == bas2.get_region_name():
            region_str = bas2.get_region_str()  
            region_str += bas.get_a().all_tweets_temp2+ " "
            bas2.set_region_str(region_str)  
            flag = 1
            break
        bas2 = bas2.next
    if flag == 0:
        lang_list_.sona_ekle(bas.get_a().language)
        region_end = lang_list_.end
        region_str = bas.get_a().all_tweets_temp2 + " "
        region_end.set_region_str(region_str)
    bas = bas.next

bas = lang_list_.head
while bas:
    ona_kadar = 0
    lang_write.write(bas.get_region_name() + " -> ")
    str_temp = bas.get_region_str()
    kelimeler = re.findall(r'\b\w+\b', str_temp.lower())
    sayac = Counter(kelimeler)
    l_temp = sayac.most_common(100)
    words_only = [word for word, count in l_temp]
    for s in words_only:
        bas2 = stop_words_list_2_.head
        on_kontrol = 0
        while bas2:
            if s[0] == bas2.get_harf():
                bas3 = bas2.get_list().head
                flag = 0
                while bas3:
                    if s == bas3.get_a():
                        flag = 1
                        break
                    bas3 = bas3.next
                if flag == 0:
                    lang_write.write(s + " ")
                    ona_kadar += 1
                    if(ona_kadar == 10):
                        on_kontrol = 1
                        break
            bas2 = bas2.next
        if(on_kontrol == 1):
            break        
    lang_write.write("\n\n")
    bas = bas.next


print("bitti")

#ortak özellik - takip edilenler - takipciler - tweet icerikleri
#   
#takipci - takip edilen ortak 5
common_types = open('common_types.txt', 'w',encoding="utf-8")

#ilerleme_kontrol = open('ilerleme_kontrol.txt', 'w',encoding="utf-8")

#liste uzunluğu tutarak bunu yarısına kadar ilerlesen de yetebilir
print("follow kontrol")
def fake_list_to_set(fake_list):
    bas = fake_list.head
    set_ = set()
    while bas:
        set_.add(bas.get_a())
        bas = bas.next
    return set_

kullanici_counter = int(kullanici_counter)
if(kullanici_counter % 2 == 1):
    kullanici_counter += 1
print(str(kullanici_counter) + "*")

ilk_kontrol = 0
bas = linked_list.head
kullanici_sayar = 0
while bas:
    if(kullanici_sayar == kullanici_counter/2):
        break
    kullanici_sayar += 1
    common_types.write("\n" +  str(kullanici_sayar) + "-" +bas.get_a().username + "->")
    set1 = fake_list_to_set(bas.get_a().following)
    set2 = fake_list_to_set(bas.get_a().followers)
    ortak_follow1 = set(set1)
    ortak_follow2 = set(set2)
    bas2 = linked_list.head
    while bas2:
        #ilerleme_kontrol.write(bas.get_a().username + " " + bas2.get_a().username + "\n")
        bas3 = bas2.get_a().ortak_kullanicilar.head
        flag = 0
        while bas3:
            if bas3.get_a() == bas.get_a().username:
                flag = 1
                break
            bas3 = bas3.next
        if(flag == 0):
            bas4 = bas.get_a().ortak_kullanicilar.head
            while bas4:
                if bas4.get_a() == bas2.get_a().username:
                    flag = 1
                    break
                bas4 = bas4.next
        if flag == 1:
            bas2 = bas2.next
            continue
        if bas.get_a().username != bas2.get_a().username:
            set3 = fake_list_to_set(bas2.get_a().following)
            set4 = fake_list_to_set(bas2.get_a().followers)
            ortak_follow3 = set(set3)
            ortak_follow4 = set(set4)
            if len(ortak_follow1.intersection(ortak_follow3)) > 5 or len(ortak_follow2.intersection(ortak_follow4)) > 5:
                bas.get_a().ortak_kullanicilar.sona_ekle(bas2.get_a().username)
                bas2.get_a().ortak_kullanicilar.sona_ekle(bas.get_a().username)
                common_types.write(bas2.get_a().username + " ")
        bas2 = bas2.next
    bas = bas.next


#kullanici-yeni list ayarlama
print("hash kullanici degisken ayarlama")
bas = linked_list.head
while bas:
    bas2 = hash_table.head
    while bas2:
        bas3 = bas2.get_fake_list().head
        while bas3:
            if bas.get_a().username == bas3.get_a():
                bas.get_a().hash_vocabs.sona_ekle(bas2.get_key())
                break
            bas3 = bas3.next
        bas2 = bas2.next
    bas = bas.next

ortak_alan = open('ortak_alan.txt', 'w',encoding="utf-8")
bas = linked_list.head
while bas:
    ortak_alan.write(bas.get_a().username + " ")
    bas2 = bas.get_a().hash_vocabs.head
    while bas2:
        ortak_alan.write(bas2.get_a() + " ")
        bas2 = bas2.next
    ortak_alan.write("\n\n")
    bas = bas.next

#ortak ilgi listesi

ortak_hiz_test = open('ortak_hiz_test.txt', 'w',encoding="utf-8")

print("hash karsilastirmasi")
sayac41 = 0
bas = linked_list.head
while bas:
    ortak_hiz_test.write(str(sayac41) + "-" + bas.get_a().username + "-> ")
    sayac41 += 1
    bas2 = linked_list.head
    while bas2:
        if(bas.get_a().username == bas2.get_a().username):
            bas2 = bas2.next
            continue
        ortak_kelime = 0
        bas5 = bas.get_a().ortak_kullanicilar.head
        flag = 0
        while bas5:
            if bas5.get_a() == bas2.get_a().username:
                flag = 1
                break
            bas5 = bas5.next
        if flag == 1:
            bas2 = bas2.next
            continue
        bas3 = bas.get_a().hash_vocabs.head
        on_dort_flag = 0
        while bas3:
            bas4 = bas2.get_a().hash_vocabs.head
            while bas4:
                if bas3.get_a() == bas4.get_a():
                    ortak_kelime += 1
                    if(ortak_kelime >= 14):
                        on_dort_flag = 1
                        break
                bas4 = bas4.next
            if(on_dort_flag == 1):
                break
            bas3 = bas3.next
        if(ortak_kelime >= 14):
                bas.get_a().ortak_kullanicilar.sona_ekle(bas2.get_a().username)
                bas2.get_a().ortak_kullanicilar.sona_ekle(bas.get_a().username)
                ortak_hiz_test.write(bas2.get_a().username + " ")
        bas2 = bas2.next
    ortak_hiz_test.write("\n")
    bas = bas.next

ortak_insanlar = open('ortak_insanlar.txt', 'w',encoding="utf-8")

bas = linked_list.head
while bas:
    ortak_insanlar.write(bas.get_a().username + " ")
    bas2 = bas.get_a().ortak_kullanicilar.head
    while bas2:
        ortak_insanlar.write(bas2.get_a() + " ")
        bas2 = bas2.next
    ortak_insanlar.write("\n\n")
    bas = bas.next

print("bitis")

print("test")
test_1 = open('test_1.txt', 'w',encoding="utf-8")

bas = linked_list.head
while bas:
    bas2 = bas.get_a().ortak_kullanicilar.head
    test_1.write(bas.get_a().username + " -> ")
    while bas2:
        test_1.write(bas2.get_a() + " ")
        bas2 = bas2.next
    test_1.write("\n")
    bas = bas.next

print("test sonu")
print("dfs basliyor ")

ortak_insanlar.close()

dfs_kullanici = input("ortak_insanlar.txt dosyasına bakarak DFS için kullanıcı adı giriniz: ")
bas = linked_list.head
temp_dfs = None
bulundu = 0
while bas:
    if bas.get_a().username == dfs_kullanici:
        bulundu = 1
        temp_dfs = bas.get_a()
        break
    bas = bas.next
if(bulundu == 0):
    print("Kullanıcı bulunamadı.")
    exit(0)


dfs_cikti = open('dfs_cikti.txt', 'w',encoding="utf-8")
ziyaret_edilenler = set()

def dfs(kullanici):
    ziyaret_edilenler.add(kullanici)
    bas = linked_list.head
    while bas:
        if bas.get_a().username == kullanici:
            break
        bas = bas.next
    #tweet olayi
    bas10 = bas.get_a().tweets.head
    dfs_cikti.write(kullanici.upper() + "\n")
    while bas10:
        text = bas10.get_a()
        text = text.replace(",","")
        text = text.replace(":","")
        text = text.replace(";","")
        text = text.replace('"', '')
        text = text.replace("%", "")
        text = text.replace("$", "")
        text = text.replace("&", "")
        text = text.replace('\\', "")
        text = text.replace('/', "")
        text = text.replace('(', "")
        text = text.replace(')', "")
        text = text.replace('=', "")
        text = text.replace('*', "")
        text = text.replace('+', "")
        text = text.replace('-', "")
        text = text.replace('<', "")
        text = text.replace('>', "")
        text = text.replace('@', "")
        text = text.replace('[', "")
        text = text.replace(']', "")
        text = text.replace('^', "")
        text = text.replace('_', "")
        text = text.replace('`', "")
        text = text.replace('{', "")
        text = text.replace('}', "")
        text = text.replace('~', "")
        text = text.replace('|', "")
        text = text.replace('\'', "")
        text = text.replace('’', "")
        text = text.replace('‘', "")
        text = text.replace('“', "")
        text = text.replace('”', "")
        text = text.replace('…', "")
        text = text.replace('.', "")
        text = text.replace('!', "")
        text = text.replace('?', "")
        text = text.lower()

        kelime_list = FakeList() #sonra ayarla ilk stringe
        while text.find(" ") != -1:
            kelime_list.sona_ekle(text[:text.find(" ")])
            text = text[text.find(" ")+1:]

        bas3= kelime_list.head
        while bas3:
            bas4 = last_words_list.head
            flag = 0
            while bas4:
                if bas3.get_a() == bas4.get_a():
                    flag = 1
                    break
                bas4 = bas4.next
            if flag == 1:
                dfs_cikti.write(bas10.get_a() + "\n")
                break
            bas3 = bas3.next
        bas10 = bas10.next

    bas11 = bas.get_a().ortak_kullanicilar.head
    while bas11:
        if bas11.get_a() not in ziyaret_edilenler:
            dfs(bas11.get_a())
        bas11 = bas11.next
    dfs_cikti.write("\n")

dfs(temp_dfs.username)


print("dfs bitti")


kullanici1 = input("Belirli iki kullanıcı için ilk kullanıcı adı #giriniz: ")

kullanici2 = input("Belirli iki kullanıcı için ikinci kullanıcı adı #giriniz: ")

tum_takipciler = FakeList()

bas = linked_list.head
flag1 = 0
flag2 = 0
while bas:
    if bas.get_a().username == kullanici1:
        flag1 = 1
        bas100 = bas.get_a().followers.head
        while bas100:
            tum_takipciler.sona_ekle(bas100.get_a())
            bas100 = bas100.next
    if bas.get_a().username == kullanici2:
        flag2 = 1
        bas101 = bas.get_a().followers.head
        while bas101:
            bas102 = tum_takipciler.head
            flag = 0
            while bas102:
                if bas101.get_a() == bas102.get_a():
                    flag = 1
                    break
                bas102 = bas102.next
            if flag == 0:
                tum_takipciler.sona_ekle(bas101.get_a())
            bas101 = bas101.next
    bas = bas.next
if(flag1 == 0):
    print("İlk girdiğiniz kullanıcı bulunamadı.")
    exit(0)
if(flag2 == 0):
    print("İkinci girdiğiniz kullanıcı bulunamadı.")
    exit(0)

#yeni graf oluşturma
    
tum_takipciler2 = open('tum_takipciler.txt', 'w',encoding="utf-8")
bas = tum_takipciler.head
while bas:
    tum_takipciler2.write(bas.get_a() + "\n")
    bas = bas.next

G2 = nx.DiGraph()

node_label_options2 = {
    "font_size": 5,
    "font_color": "blue",
    "verticalalignment": "bottom",
    "horizontalalignment": "left"
}

node_options2 = {"node_color": "red", "node_size": 50}

edge_options2 = {"width": .50, "alpha": .5, "edge_color": "black"}

bas = tum_takipciler.head
while(bas):
    bas2 = linked_list.head
    while(bas2):
        if bas.get_a() == bas2.get_a().username:
            G2.add_node(bas.get_a(), pos=(100, 100))
            break
        bas2 = bas2.next
    bas = bas.next

bas = tum_takipciler.head
while(bas):
    bas2 = linked_list.head
    flag = 0
    while(bas2):
        if bas.get_a() == bas2.get_a().username:
            flag = 1
            break
        bas2 = bas2.next
    if(flag == 1):
        bas3 = bas2.get_a().ortak_kullanicilar.head
        while(bas3):
            bas4 = tum_takipciler.head
            flag2 = 0
            while(bas4):
                if bas3.get_a() == bas4.get_a():
                    flag2 = 1
                    break
                bas4 = bas4.next
            if(flag2 == 1):
                G2.add_edge(bas.get_a(), bas3.get_a())
            bas3 = bas3.next
    bas = bas.next
plt.figure(figsize=(10,8))
pos2 = nx.circular_layout(G2)




nx.draw_networkx_nodes(G2, pos2, **node_options2)
nx.draw_networkx_edges(G2, pos2, **edge_options2)
nx.draw_networkx_labels(G2, pos2, **node_label_options2)
plt.show()

   
topluluk = open('topluluk.txt', 'w',encoding="utf-8")
ziyaret_edilenler2 = set()
topluluk_counter = 1
sayac = 0

def dfs2(kullanici, topluluk_str):
    global sayac
    sayac += 1
    ziyaret_edilenler2.add(kullanici)
    topluluk.write(kullanici + " ")
    if(sayac > 1):
        gercek_topluluk.write(kullanici + " ")
    bas = linked_list.head
    while bas:
        if bas.get_a().username == kullanici:
            break
        bas = bas.next

    bas2 = bas.get_a().tweets.head
    while bas2:
        text = bas2.get_a()
        text = text.replace(",","")
        text = text.replace(":","")
        text = text.replace(";","")
        text = text.replace('"', '')
        text = text.replace("%", "")
        text = text.replace("$", "")
        text = text.replace("&", "")
        text = text.replace('\\', "")
        text = text.replace('/', "")
        text = text.replace('(', "")
        text = text.replace(')', "")
        text = text.replace('=', "")
        text = text.replace('*', "")
        text = text.replace('+', "")
        text = text.replace('-', "")
        text = text.replace('<', "")
        text = text.replace('>', "")
        text = text.replace('@', "")
        text = text.replace('[', "")
        text = text.replace(']', "")
        text = text.replace('^', "")
        text = text.replace('_', "")
        text = text.replace('`', "")
        text = text.replace('{', "")
        text = text.replace('}', "")
        text = text.replace('~', "")
        text = text.replace('|', "")
        text = text.replace('\'', "")
        text = text.replace('’', "")
        text = text.replace('‘', "")
        text = text.replace('“', "")
        text = text.replace('”', "")
        text = text.replace('…', "")
        text = text.replace('.', "")
        text = text.replace('!', "")
        text = text.replace('?', "")
        text = text.lower()
        topluluk_str += text + " "
        bas2 = bas2.next
    bas11 = bas.get_a().ortak_kullanicilar.head
    while bas11:
        #print(bas11.get_a() + "*")
        if bas11.get_a() not in ziyaret_edilenler2:
            #print(bas11.get_a())
            dfs2(bas11.get_a(),topluluk_str)
        bas11 = bas11.next
    return topluluk_str

gercek_topluluk = open('gercek_topluluk.txt', 'w',encoding="utf-8")

bas = linked_list.head
ilk = 0
while bas:
    if bas.get_a().username not in ziyaret_edilenler2:
        sayac = 0
        topluluk_str = ""
        if(ilk == 0):
            topluluk.write(str(topluluk_counter) + ". TOPLULUK\n")
        else:
            topluluk.write("\n" + str(topluluk_counter) + ". TOPLULUK\n")
        
        topluluk_str += dfs2(bas.get_a().username, topluluk_str)
        #print(sayac)
        gercek_topluluk.write(bas.get_a().username + " ")
        if(sayac > 1):
            gercek_topluluk.write("\n" + str(topluluk_counter) + ". TOPLULUK\n")
        topluluk.write("\nTOPLULUK KELİMELERİ\n")
        if(sayac > 1):
            gercek_topluluk.write("TOPLULUK KELİMELERİ\n")
        kel = re.findall(r'\b\w+\b', topluluk_str)
        say = Counter(kel)
        l_temp = say.most_common(100)
        words_only2 = [word for word, count in l_temp]
        on_kelime = 0
        for s in words_only2:
            bas2 = stop_words_list_2_.head
            on_kontrol = 0
            while bas2:
                if s[0] == bas2.get_harf():
                    bas3 = bas2.get_list().head
                    flag = 0
                    while bas3:
                        if s == bas3.get_a():
                            flag = 1
                            break
                        bas3 = bas3.next
                    if flag == 0:
                        topluluk.write(s + " ")
                        if(sayac > 1):
                            gercek_topluluk.write(s + " ")
                        on_kelime += 1
                        if(on_kelime == 10):
                            on_kontrol = 1
                            break
                bas2 = bas2.next
        
        ilk += 1
        topluluk_counter += 1
        topluluk.write("\n")
        if(sayac > 1):
            gercek_topluluk.write("\n")
    bas = bas.next



