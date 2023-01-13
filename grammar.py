import nltk
from nltk import CFG
from nltk.draw.tree import draw_trees

grammar = nltk.CFG.fromstring("""
SEnd -> S1 S2 Stop
S1 -> VB NP
VB -> PP Verb | Verb N
PP -> Prep NLoc | Prep QuePron
NP -> NN AdjP | Npl NP | Ngen AdjP 
NN -> Npl Ngen
AdjP -> Comma AdjPron VBP
VBP -> VPassive Ninstrum PRTF
VPassive -> Est Verb
PRTF -> Comma Prtf N Comma
S2 -> PP NPDP VB
NPDP -> N DPO
DPO -> Comma Deepr N Comma

SEnd -> DP NP VB Stop
SEnd -> S1 S2 Stop
DP -> Advb Deepr Comma
NP -> NP AdjP
NP -> N NP | N
NP -> Pron N
NP -> N Ngen
AdjP -> Comma AdjPron VB Comma 
VB -> VB NP | VB N
VB -> Advb Verb
NP -> Num
VB -> VB PP | PP VB | Verb N
VB -> Verb Infn
PP -> PP PRTF
PP -> Prep NP | Prep N | Prep QuePron | Prep NLoc
PRTF -> Comma Prtf NP Advb | Comma Prtf N Comma
NP -> Adj N | Quant N


Prep -> 'на'
NLoc -> 'конференции'
Verb -> 'рассматривались' | 'отмечены' | 'опубликовали' | 'исполнится' | 'решил'
N ->  'задания' | 'организаторы' | 'результаты' | 'сборник' | 'друг' | 'университет' | 'лет' | 'брата'
Npl -> 'работы'
Ngen -> 'студентов'
Comma -> ','
AdjPron -> 'которые' | 'которому'
Est ->  'были'
Ninstrum -> 'преподавателями'
Prtf -> 'оценивавшими'
Prep -> 'после'
QuePron -> 'чего'
Deepr -> 'проанализировав' | 'раздумывая' 
Stop -> '.' 
Advb -> 'недолго' | 'завтра' | 'назад'
Pron -> 'моего'
Num -> 'двадцать'
Infn -> 'поступить'
Prep -> 'в'
Adj -> 'медицинский'
Prtf -> 'построенный'
Adj -> 'много'

""")



sent = ['на', 'конференции', 'рассматривались', 'работы','студентов',',', 'которые', 'были', 'отмечены', 'преподавателями',
        ',', 'оценивавшими', 'задания',',', 'после', 'чего', 'организаторы',',', 'проанализировав', 'результаты',',',
        'опубликовали', 'сборник', '.']

sent2 = ['недолго', 'раздумывая', ',', 'друг','моего',
        'брата', ',', 'которому', 'завтра', 'исполнится',
        'двадцать', ',', 'решил', 'поступить', 'в', 'медицинский',
        'университет', ',', 'построенный', 'много', 'лет', 'назад', '.']

parser = nltk.ChartParser(grammar)
draw_trees(*(tree for tree in parser.parse(sent)))