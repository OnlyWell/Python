# Python数据类型转换
print(int(4.6));  # 将x转换为一个整数
# print(long(3));//当前版本没有long
print(float(4));  # 将x转换到一个浮点数
# complex(real [,imag])  //创建一个复数

print(type('333'));
print(type(12.3));
print(type(222));

print(type({1,2,3,5}));
print(type({'name':'zhangsan','age':'19'}));
#--------------------------------------------------
a =21;
b = 10;
c = 0;

c = a + b;


print ("1-c的值为:", c);

print("a的b次幂",a**b);

if(a == b):
    print("相等呀");
else:
    print("NONONO");

if(a != b):
    print("啦啦啦");
else:
    print("嘎嘎嘎");

print("/n/n/n/n/n")
print(a^b);
print(a|b);
print(a&b);
print(~a);
print(2<<2);
print(18>>2);

a = 10;
b = 20;
list = [1,23,4,6,7];

if(a in list):
    print("Yeah")
else:
    print("No");

if( a not in list):
    print("不在啦");
else:
    print("哈哈哈");



print("****************************");

a = 2.0;
b = 2.0;

print(a is b);#true   比较的是对象地址
print(a == b);#true    比较的是值

#为了提高内存利用效率对于一些简单的对象,如一些数值较小的Int对象,python
#采用重用对象内存的办法
a = 2;
b = 2;
print(a is b);
print(a == b);

c = 2131231234213;
d = 2131231234213;
print(c is d);#true   is比较的是内存地址, is  和 ==  类似于编译原理中的传值与传地址
print(c == d);#true


