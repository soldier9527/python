#python

## python

### 数组:

 1. list

    append(item)
    insert(index,item)
    pop() ----delete last item
    pop(index)  -----delete index item

 2. tuple（onlyread,can't change）

    当只有一个元素时， such as 

    t=(1,)
    t=("d",)
    
    类似js里面的const 
    指向不变 即可 
 --------
  3. range(num) 生成数组  list(range(num)) 生成list

  4. dict dictionary 字典
  something in dict    return false 
  dict.get(something,return SomeThing)

eg: dict和list比较
 - dict 查找和插入速度快，不会随着key的增加而增加
 - dict 需要占用大量内存，内存浪费多
 - list则相反
dict的key必须是不可变对象

  5. set 集合
  set和dict唯一不同的就是没有存对应的value
  key和dict是一样的，独一的，并且不可以放入可变对量

  6. def 声明方法，  pass 直接过，预留函数空间

  from 文件名 import 方法名

  方法内部参数检查 isinstance(检查变量,（符合的属性，整数，小数，其他）)

  7. 递归 
  普通递归
  
  - 每当函数调用 增加一个栈桢，函数返回 减少一个栈桢 
  由于栈的大小不是无限，则当调用过多，栈桢过多，会导致堆栈溢出。这时就产生了尾递归

  尾递归
  每次都能return，计算结果当时就计算出来了

  但python没有对尾递归做优化，结果还是不能解决堆栈溢出的问题

  8. iteration 
  
  python 迭代比c高级，只要时可迭代对象都可以，比如list，dict，字符串

  9. 列表生成式 list [n.lower() for n in interation if n xxx ]

  10. generator 和列表生成式类似 把 [] 变成（）
   一个函数中包含 yield，那这个函数就是generator
   每次执行会从上一次的yield处执行
   有时候需要捕获异常

   11. 迭代器

### 总结

 iteration: list tuple dict set str
  判断可迭代对象： iterable 
  from collections import Iterable
  isinstance(xxxxx,Iterable)

  将可叠戴对象转成 索引-队列  enumerate()

  generator: next() StopInteration yield


  #### Iterable/Iterator

  生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。

  把list、dict、str等Iterable变成Iterator可以使用iter()函数：

  for => Iterable

  next() => Iterator

  ## Functional Programming  面向过程的程序设计的基本单元