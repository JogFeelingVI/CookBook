#### 使用巴科斯範式(BNF/EBNF)定義語言

-------

``` 語法定義了一種語言(A grammar defines a language)。
每種語言的背後都有一種語法，它決定了語言的結構。
上下文無關語法(context-free grammar)是在計算機科學中最常見的語法類型。
上下文無關語法能描述語言的遞歸語法結構。
```

##### 上下文無關語法語法的構成元件

一組規則(rules)是語法的核心組成部分。
規則都有兩個部分：

1. 名稱
2. 名稱的擴充

定義英文名詞語法的規則：
> 名詞片語(noun-phrase) 可能擴充為 文章名詞(article noun)

* dog是名詞片語。

描述一種編程語言的規則：
> 表達式(expression) 可能擴充為 表達式 + 表達式

若以數學符號來表示「可以擴充為」:
> noun-phrase article noun
>
> expression expression + expression

以下是經典的精確表達式語法, 由第2,3,4,6,7規則可以得出 3*7 是有效的表達式：
1. expr : 表達式
2. term : 項
3. factor : 因子
4. const : 常數
5. integer : 整數

> * expr → term+expr(1)
> * expr → term(2)
> * term → term∗factor(3)
> * term → factor(4)
> * factor → (expr)(5)
> * factor → const(6)
> * const → integer(7)

#### Backus-Naur Form (BNF) notation

-------
```
在描述語言時，巴科斯範式(Backus-Naur Form)是正式表示法，應用於供人類消耗的編碼語法。
每個規則都具有以下結構
   name ::= expansion
```

