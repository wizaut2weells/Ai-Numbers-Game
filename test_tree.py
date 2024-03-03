from random import randrange


#Klase, kas atbilst vienai virsotnei spēles kokā
class Virsotne:
    
    #Klases konstruktors, kas izveido virsotnes eksemplāru
    #Katrā virsotnes eksmeplārā glabājas virsotnes unikāls identifikators (id), skaitliskā virkne (virkne)
    #pirmā spēlētāja punkti (p1), otrā spēlētāja punkti(p2), un virsotnes atrašanās līmeņa numurs
    #Glabātie dati tiek padoti kā konstruktora argumenti
    def __init__(self, id, num, p1, p2, bank, limenis):
        self.id=id
        self.num=num
        self.p1=p1
        self.p2=p2
        self.bank=bank
        self.limenis=limenis
               
#Klase, kas atbilst spēles kokam        
class Speles_koks:
    
    #Klases konstruktors, kas izveido spēles koka eksemplāru
    #Spēles koka eksemplārs ietver sevī virsotņu kopu, kas tiek veidota kā Python saraksts un
    #loku kopu, kas tiek veidota kā Python vārdnīca (dictionary)
    #Gan virsotņu kopa, gan loku kopa sākotnējie ir tukšas
    #Virsotņu kopā glabāsies virsotnes viena aiz otras
    #Loku kopā glabāsies virsotnes unikāls identifikators kā vārdnīcas atslēga (key) un
    #ar konkrētu virsotni citu saistītu virsotņu unikālie identifikatori kā vērtības (values)
    def __init__(self):
        self.virsotnu_kopa=[]
        self.loku_kopa=dict()
    
    #Klases Speles_koks metode, kas pievieno spēles kokam jaunu virsotni, kuru saņem kā argumentu
    def pievienot_virsotni(self, Virsotne):
        self.virsotnu_kopa.append(Virsotne)
        
    #Klases Speles_koks metode, kura papildina loku kopu, saņemot kā argumentus
    #virsotnes identifikatoru, no kuras loks iziet, un virsotnes identifikatoru, kurā loks ieiet
    def pievienot_loku(self, sakumvirsotne_id, beiguvirsotne_id):
        self.loku_kopa[sakumvirsotne_id]=self.loku_kopa.get(sakumvirsotne_id,[])+[beiguvirsotne_id]


#Funkcija, kas atbilstoši veiktajam gājienam iegūst jaunu spēles koka virsotni un
#papildina speles koka virsotņu kopu un loku kopu
#Funkcija kā argumentus saņem veiktā gājiena tipu, sarakstu ar jau iepriekš saģenerētajām virsotnēm, kuras apskata 
#vienu pēc otras, un pašreiz apskatāmo virsotni
def gajiena_parbaude (gajiena_tips,generetas_virsotnes,pasreizeja_virsotne):
    # check if it can be devided
    if (pasreizeja_virsotne[1] % gajiena_tips)!=0:
            return
    
    global j
    id_new='A'+str(j)
    j+=1
    num_new= int(pasreizeja_virsotne[1]/gajiena_tips)
    
    # adding points
    if num_new%2==0 :
        if (pasreizeja_virsotne[5] % 2) == 0:
            p1_new=pasreizeja_virsotne[2]
            p2_new=pasreizeja_virsotne[3]-1
        else:
            p1_new=pasreizeja_virsotne[2]-1
            p2_new=pasreizeja_virsotne[3]  
    else:
        if (pasreizeja_virsotne[5] % 2) == 0:
            p1_new=pasreizeja_virsotne[2]
            p2_new=pasreizeja_virsotne[3]+1
        else:
            p1_new=pasreizeja_virsotne[2]+1
            p2_new=pasreizeja_virsotne[3]  

    # increasing bank value
    if str(num_new)[-1]=='0' or str(num_new)[-1]=='5':
        bank_new = pasreizeja_virsotne[4]+1
        print(num_new,bank_new)
    else: 
        bank_new = pasreizeja_virsotne[4]

    limenis_new=pasreizeja_virsotne[5]+1
    # creating new node
    jauna_virsotne=Virsotne(id_new, num_new, p1_new, p2_new, bank_new, limenis_new)

    parbaude=False
    i=0
    # checking if similar node already exists
    while (not parbaude) and (i<=len(sp.virsotnu_kopa)-1):
        if (sp.virsotnu_kopa[i].num==jauna_virsotne.num) and (sp.virsotnu_kopa[i].p1==jauna_virsotne.p1) and (sp.virsotnu_kopa[i].p2==jauna_virsotne.p2)and  (sp.virsotnu_kopa[i].bank==jauna_virsotne.bank) and (sp.virsotnu_kopa[i].limenis==jauna_virsotne.limenis):
            parbaude=True
        else:
            i+=1   

    if not parbaude:
        sp.pievienot_virsotni(jauna_virsotne)
        generetas_virsotnes.append([id_new, num_new, p1_new, p2_new,bank_new, limenis_new])
        sp.pievienot_loku(pasreizeja_virsotne[0],id_new)
    else:
        j-=1
        sp.pievienot_loku(pasreizeja_virsotne[0],sp.virsotnu_kopa[i].id)

#random number divisible by 2, 3, 4
num1 = randrange(20004,30001,12)
#num1=20004
print(num1)
#tiek izsaukts spēles koka konstruktors, lai izveidotu tukšu koku        
sp=Speles_koks()
#tiek izveidots tukšs ģenerēto virsotņu saraksts
generetas_virsotnes=[]
#tiek izveidota sākumvirsotne spēles kokā
sp.pievienot_virsotni(Virsotne('A1', num1, 0, 0,0, 1))             # 20004 - neder
#tiek pievienota pirmā virsotne ģenerēto virsotņu sarakstam
generetas_virsotnes.append(['A1', num1, 0, 0,0, 1])
#mainīgais, kurš skaita virsotnes
j=2
#kamēr nav apskatītas visas saģenerētas virsotnes viena pēc otras
while len(generetas_virsotnes)>0:
    #par pašreiz apskatāmo virsotni kļūst pirmā virsotne saģenerēto virsotņu sarakstā
    pasreizeja_virsotne=generetas_virsotnes[0]
    if pasreizeja_virsotne[1]<10:
        print('end')
        break
    #tiek pārbaudīts gājiens, kad spēlētājs paņem sev vieninieku
    gajiena_parbaude(2,generetas_virsotnes,pasreizeja_virsotne)
    #tiek pārbaudīts gājiens, kad spēlētājs paņem sev divnieku
    gajiena_parbaude(3,generetas_virsotnes,pasreizeja_virsotne)
    #tiek pārbaudīts gājiens, kad spēlētājs sadala divnieku
    gajiena_parbaude(4,generetas_virsotnes,pasreizeja_virsotne)
    #kad visi gājieni no pašreiz apskatāmās virsotnes ir apskatīti, šo virsotni dzēš no ģenerēto virsotņu saraksta
    generetas_virsotnes.pop(0)

#ciklam beidzoties, tiek izvadīta spēles koka virsotņu kopa
for x in sp.virsotnu_kopa:
    print(x.id,x.num,x.p1,x.p2, x.bank ,x.limenis)
#ciklam beidzoties, tiek izvadīta spēles koka loku kopa
for x, y in sp.loku_kopa.items():
    print(x, y)   
        