print(36%5) #餘數
print(3**4) #次方
print(81//4) #商
import math
print(math.copysign(10, -5))  #根據 y 的正負符號，改變「x 絕對值」之後的正負值。
print((3+4)*5)
import math
print(math.factorial(8)) #8階(8!)
X=3*10
Y=4*5
print(X*X)

X=12
X=6
print(X)  #6,輸出下方最新賦值
a=12
b=a
print(b*a)     #144
print(a,b,b,a) #12 12 12 12
help("keywords")
#elif=6   #elif不能變數

#函數
X=1000 #餐點費
Y=0.1 #服務費
Z=0.05 #稅
print(X*(1+Y)*(1+Z)) #1155
cost=X+X*Y+X*Y*Z
print(cost)   #1105

#變數
Apple=1
iPad5=2
#8bit=3 #變數時數字不能在前
#if=4 #if不能變數
ifan=5
only_you=6 #底線可當變數
#~rabbit~=7 #~不能當變數
print(Apple)

print("Hello world") #字串雙引號,字元單引號
print('Morning')
DD='123'
print(DD)
ab="abc"
print(ab)
print(ab+'def') #字串加法
print(ab*3) #字串乘法
#字串可以加減,無法減除
#可以 字串+字串, 字串*數字
#不可以 字串+數字, #print(ab+3)不行

#索引(選取)[]
print('abcdef'[0]) #第一字元是0
print('abcdef'[1])
T="ABCDEFGH"
print(T[3])   #第1+3字元
print(T[-4])  #倒數第4位字元
print(T[2+4]) #選取第1+2+4字元
#print(T[3/2]) #只能選取整數 
print(T[2:5]) #含前不含後,選2~4(3~5字元)
print(T[:5]) 
print(T[2:])
print(T[2:][2]) #先選2之後,再選2
print(T[2:6:3]) #先選2~6,然後間隔3
print(T[2:6:2]) #先選2~6,然後間隔2
print(T[2:6:-1])

alp="abcdefghijklmnopqrstuvwxyz"
print(alp[3:8:2]) #dfh
print(alp[2:15:3]) #cfilo
print(alp[-3:-19:-5]) #xsni
print(alp[-3:7:-5])  #xsni
print(alp[::-1])    #26字母全部反過來

inp1=input("請輸入數字")  #input裡頭為提示詞,可單純()不填提示詞
inp2=input("請輸入數字")
#print(inp)
#print(type(inp))  #inp是字串str
inp1=int(inp1)     #將inp轉為int整數數字
inp2=int(inp2)     #將inp轉為int整數數字   
print(type(inp1))  #inp1是int數字
print(inp1+inp2)   #數字inp1+數字inp2

inp1=input()
inp2=input()
inp3=input()
inp1=int(inp1)
inp2=int(inp2)
inp3=int(inp3)
print(inp1+inp2*inp3)
#等於以下
inp1=int(input())
inp2=int(input())
inp3=int(input())
print(inp1+inp2*inp3)

#list列表/清單,格式是[],避免與'選取'搞混
li=[1,3,5,'a','c','e',3.14,7.8]
print(li)
print(li[4]) #輸出清單li第5位
print(li[:4]) #輸出清單li第1~4位
print([4])  #輸出清單4
print([1,3,5,'a','c','e',3.14,7.8,['s',9]])  #清單中含清單
print(li+[0,'z'])  #清單相加
print(li*3)   #重複清單3次
li[2]='r'    #修改清單第3位,5變成r
print(li)
del li[5]   #刪除清單第6位,'e'刪除
print(li)
li.append('j')    #append增加/延伸資料,是行為(method),要再print產出(function)
print(li)

month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
inp=input("請輸入要查詢的數字月份")       
inp1=int(inp)-1
print(month[inp1]+'有'+str(days[inp1])+'天')
#等於下列
month=["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
days=[31,28,31,30,31,30,31,31,30,31,30,31]
nu=int(input("請輸入要查詢的數字月份"))-1
print(month[nu]+'有',days[nu],'天')
print(month[nu]+'有',str(days[nu]),'天')
print(month[nu]+'有',str(days[nu]),'天',sep='')  #指定清單間隔不間隔
print(month[nu]+'有',str(days[nu]),'天',sep='',end="$")   #$句尾不換行
print(nu)
print("{}有{}天".format(month[nu],days[nu]))   #字串格式化,填入相對應空格

print("{:5}有{:6}天".format(month[nu],days[nu]))   #插入空格
print("{:<5}有{:^6}天".format(month[nu],days[nu]))   #靠左<和置中^和靠右>
print("{m:>5}有{d:^6}天".format(m=month[nu],d=days[nu]))   #指定格式代號
print("{m:<5}有{d:^6}天".format(d=month[nu],m=days[nu]))    #代號可交換相對位置

#dict字典{key:value} key限數字或字串,value則隨意
#dic可以放在清單裡
dic={"Jan":31,"Feb":28,"Mar":31}

#movie={"名稱","年份","演員名單"}
list1=["謝盈萱","楊謹華","薛仕凌","陳庭妮","謝瓊煖","楊貴媚","鍾欣凌","曾莞婷"]
movie={"名稱":"影后","年份":2024,"演員名單":list1}
print(movie)               #輸出整個字典
print(movie["演員名單"])   #指定輸出字典裡的key:value
print(movie["演員名單"][3:5])   #指定輸出該key:value的號位
movie["集數"]=12              #新增清單欄位
print(movie)
movie["集數"]="十二集"        #新增清單欄位
del movie["集數"]             #刪除清單欄位
print(movie)

dic={"pi":3.14,3.14:"pi","pi":3.141592,3.141592:"pi"}
print(dic)   #{'pi': 3.141592, 3.14: 'pi', 3.141592: 'pi'}  
#同key不能多value,但可以多個key同value
print(dic[3.14])    #pi

#請幫我選取並合併成完整的python
list1=["a","b,c","d","e",{"f":["g","h"],"i":"j","k,l":{"m":["n","o","p"]},"q":"r"},"s",["t,u","v","w"],"x","y,z"]
#ans=>python
dic1={"f":["g","h"],"i":"j","k,l":{"m":["n","o","p"]},"q":"r"}
dic2={"m":["n","o","p"]}
print(list1[4]["k,l"]['m'][2]+list1[-1][0]+list1[6][0][0]+list1[4]["f"][1]+list1[4]["k,l"]["m"][1]+list1[4]["k,l"]["m"][0])

