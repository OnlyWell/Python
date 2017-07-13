print("HelloWorld!");
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

print (counter);
print (miles);
print (name);

str = "Hello World!";
print(str);
print(str[0]+ "   "+str[1]);#
print("输出第一到三个字符:"+str[1:3]);#el
print("输出字符串两次:"+str * 2);#输出字符串两次

list = ['Hello', 'world', 'welcome'];
list1 = [123, 'jhon'];


print(list);
print (list[0]);            # 输出列表的第一个元素
print (list[1:3]);          # 输出第二个至第三个的元素
print (list[2:]);           # 输出从第三个开始至列表末尾的所有元素
print (list1 * 2);       # 输出列表两次
print (list + list1);    # 打印组合的列表

#元组
tuple = ('曾经这样','天机','YES','对面');
tinytuple = ('是的', '对');

print(tuple);
print(tuple[2:]);# 输出从第三个开始至列表末尾的所有元素


dict = {};
dict['one'] = "This is one";
dict[2] = "This is two";
tinydict = {'name':'jhon','code':6734,'dept':'sales'}

print( dict['one']);  # 输出键为'one' 的值
print (dict[2]); #输出键为2的值
print(tinydict.keys()); #输出所有键
print(tinydict.values());#输出所有值