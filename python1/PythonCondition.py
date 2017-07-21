#if 基本用法
flag = False;
name = 'luren';
if name == 'python':    #判断变量是否为'python'
        flag = True;        #条件成立时设置标志位真
        print('Welcome boss');
else:
        print(name);    #条件不成立时输出变量名称

#   elif用法
num = 5;
if num == 3:
    print('boss');
elif num == 2:
    print('user');
elif num == 1:
    print('worker');
elif num < 0:
    print('error');
else:
    print('roadman');

print("-----------------------------------------");
#   if 多个条件语句
num = 9;
if(num >= 0 and num <= 10):
    print('hello');

num = 10;
if(num < 0  or num > 10):
    print('hello');
else:
    print('undefine');

num = 8;
if((num >= 0 and num <= 5) or (num >= 10 and num <= 15)):
    print('hello');
else:
    print('undefine');

print("************************************************");
numbers = [2,12,4,6,7,8,9];
even = [];
odd = [];
while(len(numbers) > 0):
    number = numbers.pop();
    if(number % 2 == 0):
        even.append(number);
    else:
        odd.append(number);
print(even);
print(odd);

print("--------------------------------------");
count = 0;
while (count < 9):
    print('The count is:', count);
    count = count + 1;
print("Good bye");

# continue 和break 用法

i = 1;
while (i < 10):
    i += 1;
    if(i%2 > 0):    #非双数时跳过输出
        continue;
    print(i);       #输出双数2,4,6,8,10
print("重新测试....");
i = 1;
while 1:    #循环条件为1必定成立
    print(i)    #输出1~10
    i += 1
    if(i > 10): #当i大于10时跳出循环
        break;














