import nltk
import codecs
import re
import csv
from nltk.corpus.reader.plaintext import PlaintextCorpusReader
corpus_root = 'files'
texts = PlaintextCorpusReader(corpus_root, r'.*\.txt', encoding = 'ISO-8859-1')
words = nltk.Text(texts.words('ag4.txt'))
## Número de Tokens (Texto) ##
len(words)
## Números de Types (Texto) ##
len(set(words))
## Densidade Lexical (Texto) ##
print (len(words)/(len(set(words))))
## Separação de Sentenças (Texto) ##
sents = nltk.Text(texts.sents('id2.txt'))
sents[20]
## Separação de palavras (Texto) ##
words[:20]
## Definição de Frequência das Palvras sem as Stopwords (Listagem dos TermosChaves) ##
words_freq.clear()
words_freq = words
stopwords = nltk.corpus.stopwords.words('portuguese')
words_freq = [word for word in words_freq if len(words) > 1]
words_freq = [word for word in words_freq if not word.isnumeric()]
words_freq = [word.lower() for word in words]
words_freq = [word for word in words_freq if word not in stopwords]
fdist = nltk.FreqDist(words_freq)
for word, frequency in fdist.most_common(30):
 print(u'{}: {}'.format(word, frequency))
## Termos-Chaves ##
termos_chaves = []
termos_chaves = ["social","capital","violência","pessoas","estudo"]
## Definição de Concordance (Termos-Chaves) ##
for dados in termos_chaves:
 print (words.concordance(dados))
 print("\n")
 print("\n")
 print("\n")
 print("\n")
# Busca palavras antecessoras (Termos-Chaves)##
words.findall("(<.*>) <capital>")
## Busca palavras sucessoras (Termos-Chaves) ##
words.findall("<estudo> (<.*>)")
## Porcentagem de cada palavra esperada no texto (Termos-Chaves) ##
resultados_esperados = {}
palavras_esperadas = termos_chaves
def percentage(word,text):
 text.count(word)
 conta = text.count(word)
 total = len(text)
 return (100*(conta/total))
for dados in palavras_esperadas:
 resultados_esperados[dados] = percentage(dados,words)
 
print (resultados_esperados)
## Gráfico de frequencias das palavras sem as Stopwords (Termos-Chaves) ##
fdist.plot(35)
## Gráfico de dispersão dos termos-chaves dos textos (termos-chaves) ##
words.dispersion_plot(termos_chaves)
# Collocations dos termos-chaves nos agrupamentos ##
words.collocations()
## Frequências das classes de palavras lematizadas ##
lista_teste5.clear()
lista_teste6.clear()
lista_teste7.clear()
lista_teste5 = []
lista_teste6 = []
lista_teste7 = []
dicio_teste3 = {}
with open(r'C:\Python27\nom_id19.csv', 'r', encoding='utf-8') as csvfile:
 readCSV = csv.reader(csvfile, delimiter=';')
 for row in readCSV:
  lista_teste6.append((row[0],row[2])) ## lista das palavras e suas respectivas frequências ##
  lista_teste5.append(row[2]) ## lista de frequências ##
  lista_teste7.append(row[0]) ## lista de palavras ##
for dados in (set(lista_teste5)):
 print(u'{} | NOM | {}'.format(dados, lista_teste5.count(dados)))
