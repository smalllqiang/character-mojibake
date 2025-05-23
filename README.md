# 亂碼小解

## 原理

### 字符編碼原理

**字符集**(*Character Set*):  
字符集是一組字符的有序集合, 可以包含多種字符. 如`ASCII`中`00-1F` `7F`是控制字符, `20-2F` `3A-40` `5B-60` `7B-7E`是符號, `30-39`是數字, `41-5A`是大寫*Latīna*字母, `61-7A`是小寫*Latīna*字母. 不同字符集中包含的字符往往不盡相同, 順序也不一定相同.  
部分常見字符集: `ASCII`, `GB2313/GBK`, `GB18030`, `Big5`, `Shift_JIS`, `Unicode`.  
其中`GB2313` `GBK` `GB18030`逐步擴展, 後者完全兼容前者.

**編碼**(*Encoding*):  
編碼是將字符集中每一個字符映射到一個唯一的數字的過程, 這是一個單射的過程.

**編碼方案**(*Encoding Scheme*):  
編碼方案是對於某個特定字符集的映射規則.  
部分常見編碼方案: `UTF-8`(Unicode其中一種編碼方案).(有時字符集與編碼的稱呼不好區分)

**解碼**(*Decoding*):
編碼的逆過程.

***

### 亂碼出現過程

因爲歷史遺留問題, 各地 各時期 各平臺等使用的編碼常有差異.  
一處以**字符集A**通過**A的編碼方案**對一串字符`abc`進行編碼, 得到`12 34 56`, 而另一處以**字符集B**通過**B的編碼方式**對`12 34 56`進行解碼, 得到`xyz`.  
因爲這種變化是普通的, 所以`xyz`常常表現爲一般人不認識的字符; 如果以**字符集B**通過**B的編碼方式**解碼的過程中 `12 34 56`不能在**字符集B**中找到對應的字符或對應的碼位沒有字符等, 則會表現爲菱形問號 方形叉號等常見的亂碼符號.  

```
  A     B
a -> 12 -> x
b -> 34 -> y
c -> 56 -> z
```

## 舉例/示例

### 東方Project

**東方紅魔郷　～ the Embodiment of Scarlet Devil.**  
以`Shift_JIS`對**東方紅魔郷**編碼, 得到`93 8c 95 fb 8d 67 96 82 8b bd`, 其中每[兩個] [16進制二位數]是一個漢字字符編碼得到的. 以`GBK`對`93 8c 95 fb 8d 67 96 82 8b bd`解碼, 每[兩個]16進制二位數會(嘗試)被解碼爲GBK內的一個字符, 得到**搶曽峠杺嫿**.

```
  Shift_JIS     GBK
東   ->    93 8c -> 搶
方   ->    95 fb -> 曽
紅   ->    8d 67 -> 峠
魔   ->    96 82 -> 杺
郷   ->    8b bd -> 嫿
```

[兩個]: 在這個例子中是兩個,但是事實上還可能有一字節字符,四字節字符等;具體如何需要看編碼方式的規定.
[16進制二位數]: 即一個字節.

***

### 魔塔

**穝穝臸娥**  
以`Big5`對**新新魔塔**編碼得到`b7 73 b7 73 c5 5d b6 f0`, 以`GBK`解碼得到**穝穝臸娥**.  

**穞堵臸猭畍**  
同上, `Big5`編碼**暗黑魔法師**, `b7 74 b6 c2 c5 5d aa 6b ae 76`, `GBK`解碼, 得到**穞堵臸猭畍**.

***

### 音遊

**闊靛緥婧愮偣**  
`UTF-8`編碼**韵律源点**, `e9 9f b5 e5 be 8b e6 ba 90 e7 82 b9`, `GBK`解碼, 得到**闊靛緥婧愮偣**.

```
  UTF-8
韵  -> e9 9f b5
律  -> e5 be 8b
源  -> e6 ba 90
点  -> e7 82 b9
     GBK
e9 9f -> 闊
b5 e5 -> 靛
be 8b -> 緥
e6 ba -> 婧
90 e7 -> 愮
82 b9 -> 偣
```

**怴婯僾儗僀儎乕僨乕僞嶌惉**  
來自LR2.  
`Shift_JIS`編碼**新規プレイヤーデータ作成**, `90 56 8b 4b 83 76 83 8c 83 43 83 84 81 5b 83 66 81 5b 83 5e 8d ec 90 ac`, `GBK`解碼.

## 解決

### 獲得原始字符串

可用工具:  
[乱码恢复](http://www.mytju.com/classCode/tools/messyCodeRecover.asp)  
[作者自己(還沒寫)的垃圾腳本](https://github.com/smalllqiang/character-mojibake)

***

### 使不呈現亂碼

可用工具:  
[Locale Emulator](https://github.com/xupefei/Locale-Emulator)

***

### (誤)

背過所有字符集所有字符及碼位, 這樣就不是"不認識的字符".  

## 聲明

本文內容不保證正確.  
內容均爲原創, 轉載需遵循[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/), 或向作者本人詢問.

</br></br></br></br></br></br></br></br>
[原文](https://smalllqiang.github.io/note/202411/亂碼小解.html)