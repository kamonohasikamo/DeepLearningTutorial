# しゃーぷでコメントが書けるようになる
# 変数の方の宣言は不要。
# 入力すれば自動的に入れてくれる
# 型の確認はtype()関数
a = 1
print(type(a))
print(type(0.5))
print(type(.5))
print(type(5.))
print(a)

# 複数同時変数代入法
k, b, c = 1, 1.2, 'Chainer'
print(k)
print(b)
print(c)

# 算術系(基本は別言語と一緒)
# // は切り捨て除算
print(3 // 2)
print(4 // 2)

# str(string)とintやfloatの演算は基本できない
# ただし、乗算は可能。
# strという文字列をn回繰り返すという意味。
print(c * 3)

# ** は累乗、%は余り
print(2 ** 3)
print(9 % 2)

# strの便利な関数
# lower() : 文字列をすべて小文字に変換
# upper() : 文字列をすべて大文字に変換
name = 'Kaggle'
print(name.lower())
print(name.upper())

# '{}'.format(str) : 引数strを{}に入れる
# C言語の%sのような使い方ができる
print('\n{}さん\nこんにちは.'.format(name))
name1 = 'Chainer'
name2 = 'チュートリアル'
print('{} {}へようこそ'.format(name1, name2))

# 浮動小数点数がもつメソッド
# as_integer_ratio() : float特有のメソッド。
# 与えられた値の比を教えてくれる。
# 例:
# 0.5は分数で表すと1/2．
checkFloat = 0.5
print(checkFloat.as_integer_ratio())

# 複合データについて
# 復号データは以下の3つがある。
# ・リスト型(ほぼ配列)
# ・タプル型(ほぼ配列　ただし、データの書き換えができない)
# ・辞書型(ほぼ構造体)

# ============================
#  リスト
# ============================
# リスト型の変数を定義
numbers = [4, 5, 6, 7]
print(numbers)
print(type(numbers))
print(len(numbers))
print(numbers[2])
numbers[1] = 24
print(numbers)

# インデックスに負値を与えると、「末尾から」の参照となる
print(numbers[-1])
print(numbers[-3])

# [start:end] : リスト型の要素取り出し(slice)
# 開始地点:終了地点を入れるとそこまでの要素をとってくれる
# 省略も可能
print(numbers[0:2])
print(numbers[:3])
print(numbers[:])
checkNumbers = [0, 1]
print(checkNumbers[:2])
print(checkNumbers[2:])

# リスト型に要素を追加するときはappend()
checkNumbers.append(9)
checkNumbers.append('aiueo')
checkNumbers.append([5.5, 'nemui'])
print(checkNumbers)

# 基本は空のリストを宣言しておき、あとから要素を追加する
array = []
array.append('Chainer')
array.append('チュートリアル')
print(array)


# ============================
#  タプル
# ============================
# リストとは違って、変更不可な配列
# 基本はほとんど一緒

# タプル型の変数を宣言
arrayTaple = (8, 9, 10, 11)
print(arrayTaple)
print(type(arrayTaple))

# 要素のアクセス方法もリストと同じ
print(arrayTaple[2])
print(arrayTaple[1:3])

# これはエラー
# arrayTaple[0] = 3
# arrayTaple.append(5)

# ============================
#  辞書型
# ============================
# 構造体のこと

# 辞書型を定義
score = {'数学': 90, 'Science': 75, 'Japanese': 10, '英語': 100}
print(score)

# keyでアクセス
print(score['数学'])
print(score['Japanese'])

# 他人が定義した辞書型で、どのようなキーがあるのか、などを調べるメソッド
# ・key() : キーのリストを取得
# ・values() : 値のリストを取得
# ・items() : 各要素のタプルを並べたリストを取得
print(score.keys())
print(score.values())
print(score.items())

# if文for文の書き方

# 5回繰り返す
for i in range(5):
	print(i)
print(i)

sample = ['佐藤', '鈴木', '高橋']
for i in range(3):
	print(sample[i])

for i in range(3):
	print('{}さん'.format(sample[i]))

for i in range(len(sample)):
	print('{}さんん'.format(sample[i]))

for sampleCount in sample:
	print('{}さん'.format(sampleCount))

for i, name in enumerate(sample):
	message = '{}番目: {}さん'.format(i, name)
	print(message)

# 関数
# double()を定義
def double(input):
	print(2 * input)

double(3)
double(1.5)

def add(a, b):
	print(a + b)

add(1, 2)
add(3, 1.8)
add(1, -5)

def helloWorld():
	print('HelloWorld')

helloWorld()

def helloCheck(message = 'helloCheck'):
	print(message)

helloCheck()
helloCheck('sample')


# 変数のスコープ
t = 1

def change():
	global t
	t = 2
	print('in', t)

print('out', t)
change()