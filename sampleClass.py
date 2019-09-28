# 家の設計図を表す House というクラスを定義
# House クラスには、インスタンス化されたあとに、各インスタンス
# すなわち誰か特定の人の家ごとに異なる値を持つ、
# namePlate という変数を持たせる。

# namePlate という変数には、
# 個別の家の表札に表示するための文字列が与えられるが、
# クラスを定義する際には「namePlate という変数を持つことができる」
# ようにしておくだけでよく、
# 実際にその変数に何か具体的な値を与える必要はない。 
# クラスは、設計図であればよく、具体的な値を持たせなくてもよいので。 
# 具体的な値は、個別の家を作成するとき、すなわちインスタンス化の際に与え、
# 各インスタンスが namePlate という値に自分の家の表札の名前を保持するようにする。

# このような、インスタンスに属している変数を属性 (attribute) と呼ぶ。
# 同様に、インスタンスから呼び出すことができる関数のことをメソッド (method) と呼ぶ。

# クラスの定義
class House:
	# __init__()メソッドの定義
	def __init__(self, name):
		self.namePlate = name
	
	# メソッドの定義
	def hello(self):
		print('{}の家です'.format(self.namePlate))

# __init__() : インスタンス化する際に自動的に呼ばれるメソッド
# self というのは
# クラスがインスタンス化されたあと、作成されたインスタンス自身を参照するのに用いられる。 
# これを使って、self.namePlate = name とすることで、
# 作成された個別のインスタンスに属する変数 self.namePlate へ、
# 引数に渡された name が持つ値を代入することができる。 
# self が指すものは、各インスタンスから見た「自分自身」なので、各インスタンスごとに異なる。 
# これによって、self.namePlate は各インスタンスに紐付いた別々の値を持つものとなる。

# メソッドは、インスタンスから呼び出されるとき自動的に第一引数にそのインスタンスへの参照を渡す。 
# そのため、メソッドの第一引数は self とし、渡されてくる自分自身への参照を受け取るようにしている。
# ただし、呼び出す際にはそのインスタンスを引数に指定する必要はない。

house1 = House('sample')
house2 = House('たけし')

house1.hello()
house2.hello()

# ==============================================================
# 継承
# ==============================================================
# あるクラスを定義したとき、その一部の機能だけほしいときがあったり
# 一部の機能だけ付け加えたかったりする時がある。
# これを実現するのが継承。

# 以下のLinkというクラスには、
# 引数を1つも取らないが、中の属性としてa,bの2つの変数を持ち、
# それぞれ1,2という値が代入されている。
class ParentLink:
	def __init__(self):
		self.a = 1
		self.b = 2

linkCheck = ParentLink()
print(linkCheck.a)
print(linkCheck.b)

# 上のLinkを継承したクラスChildrenLinkを生成する。

# a という属性は、ChildrenLink の親クラスである ParentLink の __init__() メソッドで定義されている。 
# ChildrenLink クラスにも __init__() メソッドを定義したため、
# 親クラスである ParentLink の __init__() メソッドが上書きされてしまい実行されなかった。 
# しかし、親クラスの __init__() メソッドを明示的に呼ぶことで、これは解決できる。

# それには、super() という組み込み関数を用いる。 
# これを用いると、子クラスから親クラスを参照することができる。

class ChildrenLink(ParentLink):
	def __init__(self):
		super().__init__() # 親クラスの__init__を呼び出す
		self.c = 5 # cを追加

	def sum(self):
		return self.a + self.b + self.c # cを追加

children = ChildrenLink()
print(children.a)
print(children.b)
print(children.sum())

class ChiChildrenLink(ChildrenLink):
	def mul(self):
		return self.a * self.b * self.c

chichildren = ChiChildrenLink()
print(chichildren.mul())