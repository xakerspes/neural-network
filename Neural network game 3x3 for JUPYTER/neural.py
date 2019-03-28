import re 
import numpy as np 
 

#///////////--- etu chast mojno nekomplirovat----//////////////////////////////////////
f=open('input.txt', 'r')
o=open('output.txt', 'w+')
a=[]
b=[] 
c=[]
import abc 
with open('input.txt') as f:
  for line in f:
    line = (line.strip())
    result = re.sub(r'\.','0 ', line)
    line = result.rstrip()
    result = re.sub(r'O','-2 ', line)
    line = result
    result = re.sub(r'X','1 ', line)
    line = result.strip()
    a=(line.split())
    for j in range(len(a)):
      b.append(int(a[j]))
    c=b
d=np.array(c)
d.shape= 20,4
print(d)
 

e=np.vsplit(d, 5)
input_po_strok=e 
        
for i in range(5):
        X_10 = e[i]
        X_0 = np.zeros((2,4), dtype=int)
        X_0[0] = X_10[0,0],X_10[1,1],X_10[2,2],X_10[3,3]
        X_0[1] = X_10[0,3],X_10[1,2],X_10[2,1],X_10[3,0]
        
        input_1=np.vstack((e[i],e[i].T,X_0))
         
        
        def nonlin(x, deriv=False):   
            if(deriv==True):
                return (x*(1-x))
        
            return 1/(1+np.exp(-x))  
        
        syn0 =  np.array( [[ 0.854553, 0.713213, -3.878386, 0.464796, -3.563713, 0.587628, 0.948467, -0.962040, -1.867612, 0.682878],
        [0.944612, 0.993458, -3.788060, 1.218916, -3.505234, 0.874482, 0.657949, -0.650333, -1.919282, 0.308433],
        [1.188166, 0.817043, -5.648590, 0.587150, 5.258754, 0.761897, 0.319946, -0.597483, 2.671046, 0.594678],
        [-0.669696, -0.371799, 5.799050, -0.176844, -5.222500, -0.160767, 0.168532, 0.035326, -3.361088, 0.233326]])
        syn1 = np.array([[2.161306],
                          [2.006227],
                          [-12.623126],
                          [1.932463],
                          [-10.790417],
                          [1.432479],
                          [1.702968],
                          [-3.426684],
                          [-6.159724],
                          [0.814876]])
                                  
        q1 = nonlin(np.dot(input_1, syn0))
        q2 = nonlin(np.dot(q1, syn1))
        q2 = np.around(q2)
        q2 = np.int_(q2)
      
      
        
        v = np.argwhere(q2==1)
        
        h  = v.ravel()
        h= int(h.sum())
 
        
        input_1_1 =  input_1[h]
       
        
        syn0_1 =  np.array([[0.616534, 0.685752, -1.703184, -0.837880],
                            [0.475788, 0.430166, -0.273104, -0.086818],
                            [0.682685, 0.736416, 0.509457, 0.523616],
                            [0.671174, 1.031270, 1.148550, 1.205951]]) 
        syn1_1 =  np.array([[0.333633],
                            [0.217512],
                            [-2.068893],
                            [-1.224288]])
        
       
        
        
        q1_1 = nonlin(np.dot(input_1_1, syn0_1))
        q2_1 = nonlin(np.dot(q1_1, syn1_1))
			 
        a=int(np.round(q2_1*10))
        #print (h)
        #print(a)
        if (h==8):
          if(a==1):
            print(1,1)
          elif(a==2):
            print(2,2)
          elif(a==3):
            print(3,3)
          elif(a==4):
            print(4,4)
        elif (h==9):
          if(a==1):
            print(1,4)
          elif(a==2):
            print(2,3)
          elif(a==3):
            print(3,2)
          elif(a==4):
            print(4,1)
        elif (h>3 & h<8):
        	print(a, h-3)
        else:
          print ('%.d' %(h+1), a)
			#np.savetxt(o, 2342)
            