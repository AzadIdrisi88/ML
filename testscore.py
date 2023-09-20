import matplotlib.pyplot as plt
import numpy as np
salesman=[1,2,3,4,5,6,7,8,9,10]
testscore=[40,70,50,60,80,50,90,40,60,60]
sales=[2.5,6.0,4.5,5.0,4.5,2.0,5.5,3.0,4.5,3.0]

n=len(testscore)
mean_testscore=np.mean(testscore)
print("mean_x",mean_testscore)
mean_sales=np.mean(sales)
print("meany",mean_sales)
mean_sales=4.5
# mean_testscore=sum(testscore)/len(testscore)
# print(mean_testscore)
# mean_sales=sum(sales)/len(sales)
# print(mean_sales)

# avrt=(40+70+50+60+80+50+90+40+60+60)/10
# print(avrt)
# avrs=(2.5+6.0+4.5+5.0+4.5+2.0+5.5+3.0+4.5+3.0)/10
# print(avrs)

dx=[i-mean_testscore for i in testscore]
dy=[i-mean_sales for i in sales]
print("dx ",dx)
print("dy ",dy)

sigmadxdy=0
sigmadx=0
sigmady=0
sigmadx2=0
sigmady2=0

for i in range(n):
    sigmadx+=dx[i]
    sigmady+=dy[i]
    sigmadxdy+=dx[i]*dy[i]
    sigmadx2+=dx[i]*dx[i]
    sigmady2+=dy[i]*dy[i]
print("sigma dx ",sigmadx,"sigma dy ",sigmady,"sigma dx2 ",sigmadx2,"sigma dy2 ",sigmady2,"sigma dxXdy",sigmadxdy)   

r=(sigmadxdy-((sigmadx*sigmady)/n))/(sigmadx2-((sigmadx**2)/n))
print('value of r alpha_y/alpha_x=',r)


y=r*(70-mean_testscore)+mean_sales
print('y= ',y)

# plt.plot(70,y)
plt.bar(70,y ,color='red',linestyle='--')
plt.xlabel('Testscore')
plt.ylabel('Sales')
plt.show()

