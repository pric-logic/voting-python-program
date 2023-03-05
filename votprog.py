#importing mysql connector
import mysql.connector



#USER DEFINED FUNCTION(Analysis of VOTES)

#how many vote from particular division
def division(sub):
    stat1="select vote,class,division,count(*) from voter group by vote,division,class having class in (11,12) and division='{}'".format(sub)
    cursor.execute(stat1)
    data1=cursor.fetchall()
    for row1 in data1:
        print(row1)
        
# how many vote from particular class       
def cla_ss(std):
    stat2="select vote,count(*) from voter group by vote,class={}".format(std)
    cursor.execute(stat2)
    data2=cursor.fetchall()
    for row2 in data2:
        print(row2)
        
# how many vote from particular class and division       
def cla_div(std,sub):
    stat3="select vote,class,division,count(*) from voter group by vote,division,class having division='{}'".format(sub)
    cursor.execute(stat3)
    data3=cursor.fetchall()
    for row3 in data3:
        print(row3)
        
# how many male or female vote       
def Gender():
    stat4="select gender,vote,count(*) from voter group by gender,vote"
    cursor.execute(stat4)
    data4=cursor.fetchall()
    for row4 in data4:
        print(row4)
# no. of absentees
def absentees():
    stat5="select count(*) as 'absentees'from voter where vote is Null"
    cursor.execute(stat5)
    data3=cursor.fetchall()
    for row5 in data3:
        print(row5)
# winner name
def winner(win):
    statement="select name from candidate where C_CODE='{}'".format(win)
    cursor.execute(statement)
    win=cursor.fetchall()
    return win[0][0]

# connecting mysql        
mycon=mysql.connector.connect(host="localhost",user="root",passwd="iitjee@1",database="electoral")
if mycon.is_connected():
    print("successfully connected")
cursor=mycon.cursor()


#termination condition's initialisation( while loop below)
termination_condt=""



#checking if voter exists by voter_id
while termination_condt !="terminate" :
    idd= int(input("voter id"))
    idcheck="select * from voter where voter_id={}".format(idd)
    cursor.execute(idcheck)
    datav=cursor.fetchall()
    c= cursor.rowcount
    if c==0:
        print("not elligible")
    #checking if voter already vote
        #displaying candidate table
    else:
        vote_check="select vote from voter where voter_id='{}'".format(idd)
        cursor.execute(vote_check)
        datac=cursor.fetchall()
        for row in datac:
            print(row)
            if row[0]==None:
                print("candidate table")
                CANDIDATE_TABLE="select C_CODE,name from candidate"
                cursor.execute(CANDIDATE_TABLE)
                data_can=cursor.fetchall()
                opt=[]
                for row in data_can:
                    opt=opt+[row[0]]
                    print(row)
                    # taking vote from the user
                vote=input("enter your vote (use candidate code)")
                #checking if the vote is valid i.e if the candidate exists
                if vote in opt: 
                   #updating vote in the voter table
                    vote_input="UPDATE voter SET vote='{}' where voter_id={}".format(vote,idd)
                    cursor.execute(vote_input)
                    mycon.commit()
                    print("valid vote, THANKYOU FOR VOTING!")
                else:
                    print("candidate does not exist")
                    
                    
                               
                
            else:
                print("your response has already been taken")
    termination_condt=input("continue or terminate")            
 # counting of votes and display of votes won by each candidate   
print("time to count the votes")
count_vote="select vote,count(*)from voter group by vote"
cursor.execute(count_vote)
data_count=cursor.fetchall()
print("VOTE_tally")
for no_of_votes in data_count:
    print(no_of_votes)
#declaring the person with highest votes as CS Seceratary
    #removing null and not interested from the comptetion
dict_result=dict(data_count)
remove_null=dict_result.pop(None,None)
remove_NI=dict_result.pop("NI",None)
print(dict_result)
val=(dict_result.values())
print(val)
m=max(list(val))
print(m)
L=[]
for candid in dict_result:
    if dict_result[candid]==m:
        L=L+[candid]
        print(candid)
print(L)
#removing "NOT INTERESTED" (NI) From winner selection
    
#CS scretary declaration
if len(L)==1:
    print("CS SECRETARY", L[0],winner(L[0]))




    #for joint secretary calculation we need to remove CS secretary from the joint secretary
    del (dict_result[L[0]])
    print(dict_result)
    L2=dict_result.values()
    max2=max(L2)
    list_of_jointsec=[]
    for val in dict_result:
        if dict_result[val]==max2:
            list_of_jointsec+=[val]
        if len(list_of_jointsec)==1:
            print("JOINT SECRETARY",list_of_jointsec[0])

            
        else: #tie for joint secretary
            #update teacher_panel set vote=null;
            print("TIE BETWEEN",list_of_jointsec)
            print("TIE BREAKER FOR JOINT SECRETARY")
            i=0
            while i<3:
                idd= int(input("teacher id"))
                idcheck="select * from teacher_panel where teacher_id={}".format(idd)
                cursor.execute(idcheck)
                datav=cursor.fetchall()
                c= cursor.rowcount
                if c==0:
                    print("invalid id")
                else:
                    vote_check="select vote from teacher_panel where teacher_id='{}'".format(idd)
                    cursor.execute(vote_check)
                    datac=cursor.fetchall()
                    for row in datac:
                        print(row)
                        if row[0]==None:
                            print("cast your vote")
                            print("vote for",list_of_jointsec)
                            vote=input("enter your vote (use candidate code)")
                    print(list_of_jointsec)
                    if vote in list_of_jointsec:
                        #updating vote in the teacher_panel table
                        vote_input="UPDATE teacher_panel SET vote='{}' where teacher_id={}".format(vote,idd)
                        cursor.execute(vote_input)
                        mycon.commit()
                        print("valid vote, THANKYOU FOR VOTING!")
                        i=i+1
                        
                    else:
                        print("your response has already been taken")
     # counting of votes and display of votes won by each candidate in teacher panel
            count_votes="select vote,count(*) from teacher_panel group by vote"
            cursor.execute(count_votes)
            data_count=cursor.fetchall()
            print("VOTE_tally")
            c=0
            for row in data_count:
                print(row)
                c+=1
            if c==1:
        #declaring the person with highest votes as CS Seceratary
                print("CS JOINT SECRETARY",data_count[0][0],winner(data_count[0][0]))
            else:
                if data_count[0][1]>data_count[1][1]:
                    print("CS joint SECRETARY",data_count[0][0],winner(data_count[0][0]))
                else:
                    print("CS joint SECRETARY",data_count[1][0],winner(data_count[0][0]))
                    
    
#if there's a case of tie between two people - teacher's panel will give thier votes and act as a tie breaker    
#conducting voting for the teachers_panel
# update teacher_panel set vote = NULL;    
else:
    print("tie between " ,L)
    i=0
    while i<3:
       
        idd= int(input("teacher id"))
        idcheck="select * from teacher_panel where teacher_id={}".format(idd)
        cursor.execute(idcheck)
        datav=cursor.fetchall()
        c= cursor.rowcount
        if c==0:
            print("invalid id")
        else:
            vote_check="select vote from teacher_panel where teacher_id='{}'".format(idd)
            cursor.execute(vote_check)
            datac=cursor.fetchall()
            for row in datac:
                print(row)
                if row[0]==None:
                    print("cast your vote")
                    print("vote for",L)
                    vote=input("enter your vote (use candidate code)")
                    print(L)
                    if vote in L:
                        #updating vote in the teacher_panel table
                        
                        vote_input="UPDATE teacher_panel SET vote='{}' where teacher_id={}".format(vote,idd)
                        cursor.execute(vote_input)
                        mycon.commit()
                        print("valid vote, THANKYOU FOR VOTING!")
                        i=i+1
            
                    else:
                        print("candidate does not exist")
                else:
                    print("your response has already been taken")
     # counting of votes and display of votes won by each candidate
    count_votes="select vote,count(*) from teacher_panel group by vote"
    cursor.execute(count_votes)
    data_count=cursor.fetchall()
    print("VOTE_tally")
    c=0
    lmn=L[:]
    for row in data_count:
        print(row)
        c+=1
        lmn.remove(row[0])
    print(lmn)
    if c==1:#declaring the person with highest votes as CS Seceratary
        print("CS SECRETARY",data_count[0][0],winner(data_count[0][0]))
        print("CS JOINT SECRETARY",lmn[0],winner(lmn[0]))
    else:
        if data_count[0][1]>data_count[1][1]:
            print("CS SECRETARY",data_count[0][0],winner(data_count[0][0]))
            print("CS JOINT SECRETARY",data_count[1][0],winner(data_count[1][0]))
        else:
            print("CS SECRETARY",data_count[1][0],winner(data_count[1][0]))
            print("CS JOINT SECRETARY",data_count[0][0],winner(data_count[0][0]))



















print("the voting is over")
print(" ")
print("ANALYSIS")
#functions for analysis
def gender(year):
    if year==2020:
        yr='voter_2020'
    if year==2019:
        yr='voter_2019'
    if year==2018:
        yr='voter_2018'
    cursor.execute("select gender,count(*) from voter_2020 where gender='M'")
    total_M=cursor.fetchall()
    cursor.execute("select gender,count(*) from voter_2020 where gender='F'")
    total_F=cursor.fetchall()
    cursor.execute("select VOTE,count(*) from voter_2020 where VOTE not in ('NULL','NI') and gender='M'")
    vote_M=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2020 where VOTE not in ('NULL','NI') and gender='F'")
    vote_F=cursor.fetchall()
    per_MV_CY=(vote_M[0][1]/total_M[0][1])*100 #PERCENTAGE OF MALE WHO vote
    print("MALE vote:",per_MV_CY,'%')
    per_FV_CY=(vote_F[0][1]/total_F[0][1])*100 #PERCENTAGE OF FEMALE WHO vote
    print("FFMALE vote:",per_FV_CY,'%')

    cursor.execute("select vote,count(*) from voter_2020 where vote is NULL and gender='M'")
    absent_m=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2020 where vote is NULL and gender='F'")
    absent_f=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2020 where vote='NI'and gender='M'")
    ni_m=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2020 where vote='NI'and gender='F'")
    ni_f=cursor.fetchall()
    print("MALE ABSENTEES:",(absent_m[0][1]/total_M[0][1])*100,'%')
    print("FEMALE ABSENTEES:",(absent_f[0][1]/total_F[0][1])*100,'%')
    print("MALE NI:",(ni_m[0][1]/total_M[0][1])*100,'%')
    print("FEMALE NI:",(ni_f[0][1]/total_F[0][1])*100,'%')
    
    

    cursor.execute("select gender,count(*) from voter_2019 where gender='M'")
    total_M=cursor.fetchall()
    cursor.execute("select gender,count(*) from voter_2019 where gender='F'")
    total_F=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2019 where vote not in ('NULL','NI') and gender='M'")
    vote_M=cursor.fetchall()
    cursor.execute("select vote,count(*) from voter_2019 where vote not in ('NULL','NI') and gender='F'")
    vote_F=cursor.fetchall()
    per_MV_PY=(vote_M[0][1]/total_M[0][1])*100
    per_FV_PY=(vote_F[0][1]/total_F[0][1])*100


    if per_MV_CY>per_MV_PY:
        print("participation of male increased w.r.t to last year")
    else:
        print("participation of male decreased w.r.t to last year")
    if per_FV_CY>per_FV_PY:
        print("participation of female increased w.r.t to last year")
    else:
        print("participation of female decreased w.r.t to last year")


def Class(year):

    if year==2020:
        yr='voter_2020'
    if year==2019:
        yr='voter_2019'
    if year==2018:
        yr='voter_2018'
    
    cursor.execute("select class,count(*) from {} where class=11 and vote not in ('NULL','NI')".format(yr))
    voted_11=cursor.fetchall()
    cursor.execute("select class,count(*) from {} where class=12 and vote not in ('NULL','NI')".format(yr))
    voted_12=cursor.fetchall()
    
    cursor.execute("select class,count(*) from {} where class=11".format(yr))
    total_11=cursor.fetchall()
    cursor.execute("select class,count(*) from {} where class=12".format(yr))
    total_12=cursor.fetchall()
    
    per_11V_CY=(voted_11[0][1]/total_11[0][1])*100 #PERCENTAGE OF 11 WHO vote
    print("11 vote:",per_11V_CY,'%')
    per_12V_CY=(voted_12[0][1]/total_12[0][1])*100 #PERCENTAGE OF 12 WHO vote
    print("12 vote:",per_12V_CY,'%')

    cursor.execute("select class,count(*) from {} where class=11 and vote is NULL".format(yr))
    absent_11=cursor.fetchall()
    cursor.execute("select class,count(*) from {} where class=12 and vote is NULL".format(yr))
    absent_12=cursor.fetchall()
    
    cursor.execute("select class,count(*) from {} where class=11 and vote='NI'".format(yr))
    ni_11=cursor.fetchall()
    cursor.execute("select class,count(*) from {} where class=12 and vote='NI'".format(yr))
    ni_12=cursor.fetchall()
    print("11 ABSENTEES:",(absent_11[0][1]/total_11[0][1])*100,'%')
    print("12 ABSENTEES:",(absent_12[0][1]/total_12[0][1])*100,'%')
    print("11 NI:",(ni_11[0][1]/total_11[0][1])*100,'%')
    print("12 NI:",(ni_12[0][1]/total_12[0][1])*100,'%')
    
    
    if year==2020:
        pyr='voter_2019'
    if year==2019:
        pyr='voter_2018'

    if year!=2018:
       cursor.execute("select class,count(*) from {} where class=11 and vote not in ('NULL','NI')".format(pyr))
       voted_11=cursor.fetchall()
       cursor.execute("select class,count(*) from {} where class=12 and vote not in ('NULL','NI')".format(pyr))
       voted_12=cursor.fetchall()
       cursor.execute("select class,count(*) from {} where class=11".format(pyr))
       total_11=cursor.fetchall()
       cursor.execute("select class,count(*) from {} where class=12".format(pyr))
       total_12=cursor.fetchall()
       per_11V_PY=(voted_11[0][1]/total_11[0][1])*100
       per_12V_PY=(voted_12[0][1]/total_12[0][1])*100
       if per_11V_CY>per_11V_PY:
           print("participation of 11 increased w.r.t to last year")
       else:
           print("participation of 11 decreased w.r.t to last year")
       if per_12V_CY>per_12V_PY:
           print("participation of 12 increased w.r.t to last year")
       else:
           print("participation of 12 decreased w.r.t to last year")


        

def Division(year):
    if year==2020:
        yr='voter_2020'
    if year==2019:
        yr='voter_2019'
    if year==2018:
        yr='voter_2018'
    d={}
    for div in ['MATHS','BIO','COMMERCE']:
        cursor.execute("select division,count(*) from {} where division='{}' and vote NOT IN ('NULL','NI')".format(yr,div))
        vote_div=cursor.fetchall()
        cursor.execute("select division,count(*) from {} where division='{}'".format(yr,div))
        total_div=cursor.fetchall()
        cursor.execute("select division,count(*) from {} where division='{}' and vote='NI'".format(yr,div))
        absentee_div=cursor.fetchall()
        cursor.execute("select division,count(*) from {} where division='{}' and vote is NULL".format(yr,div))
        ni_div=cursor.fetchall()
        print(div,'division vote:',(vote_div[0][1]/total_div[0][1])*100)
        print(div,'absentees:',(absentee_div[0][1]/total_div[0][1])*100)
        print(div,'ni:',(ni_div[0][1]/total_div[0][1])*100)
        d[(vote_div[0][1]/total_div[0][1])*100]=div
    highest=max(d)
    print(d[highest],'members have highest participation:',highest)
    

def house(year):
    if year==2020:
        yr='voter_2020'
    if year==2019:
        yr='voter_2019'
    if year==2018:
        yr='voter_2018'
    d={}
    for h in ['TAPI','KAVERI','GODAVARI','NARMADA']:
        cursor.execute("select house,count(*) from {} where house='{}' and vote NOT IN ('NULL','NI')".format(yr,h))
        vote_h=cursor.fetchall()
        cursor.execute("select house,count(*) from {} where house='{}'".format(yr,h))
        total_h=cursor.fetchall()
        cursor.execute("select house,count(*) from {} where house='{}' and vote='NI'".format(yr,h))
        absentee_h=cursor.fetchall()
        cursor.execute("select house,count(*) from {} where house='{}' and vote is NULL".format(yr,h))
        ni_h=cursor.fetchall()
        print(h,'house vote:',(vote_h[0][1]/total_h[0][1])*100)
        print(h,'absentees:',(absentee_h[0][1]/total_h[0][1])*100)
        print(h,'ni:',(ni_h[0][1]/total_h[0][1])*100)
        d[(vote_h[0][1]/total_h[0][1])*100]=h
    highest=max(d)
    print(d[highest],'memebers have highest participation:',highest)



#analysis output
while True:
    print('1.2021 analysis')
    print('2.past 3 year analysis')
    print('3.winner analysis')
    print('4.exit')
    opt=int(input("(1/2/3/4):"))
    if opt==1:
        while True:
            print('1.how many voted from particular division')
            print('2.how many voted from particular class')
            print('3.how many voted from particular class and division')
            print('4.how many male or female voted')
            print('5.no. of absentees')
            print('6.exit')
            o=int(input('choose any of the above'))
            if o==1:
                sub=input("division name:")
                division(sub)
            elif o==2:
                std=int(input("class:"))
                cla_ss(std)
            elif o==3:
                std=int(input("class:"))
                sub=input("division name:")
                cla_div(std,sub)
            elif o==4:
                Gender()
            elif o==5:
                absentees()
            elif o==6:
                break
            else:
                print('incorrect option')
            
        
    elif opt==2:
        while True:
            print('1.2020 analysis')
            print('2.2019 analysis')
            print('3.2018 analysis')
            print('4.exit')
            o1=int(input('(1/2/3/4):'))
            if o1==1:
                year=2020
                print('1.gender wise')
                print('2.house wise')
                print('3.class wise')
                print('4.division wise')
                oin=int(input('choose any of the above'))
                if oin==1:
                    gender(year)
                if oin==2:
                    house(year)
                if oin==3:
                    Class(year)
                if oin==4:
                    Division(year)
            elif o1==2:
                year=2019
                print('1.gender wise')
                print('2.house wise')
                print('3.class wise')
                print('4.division wise')
                oin=int(input('choose any of the above'))
                if oin==1:
                    gender(year)
                if oin==2:
                    house(year)
                if oin==3:
                    Class(year)
                if oin==4:
                    Division(year)
            if o1==3:
                year=2018
                print('1.gender wise')
                print('2.house wise')
                print('3.class wise')
                print('4.division wise')
                oin=int(input('choose any of the above'))
                if oin==1:
                    gender(year)
                if oin==2:
                    house(year)
                if oin==3:
                    Class(year)
                if oin==4:
                    Division(year)
            if o1==4:
                break
            
                    #winner analysis
    if opt==3:
        while True:
            print('1.2020 data analysis')
            print('2.2019 data analysis')
            print('3.2018 data analysis')
            print("4.exit")
            c=int(input("user pls select"))
            if c==1:
                print('a.gender wise')
                print('b.house wise')
                m=input("user pls")
                if m=='a':
                    query_gen_f=''' select Candidate_Name,count(*) from candidate_2020,voter_2020 where candidate_2020.C_Code=voter_2020.vote and Position='cs sec' and voter_2020.gender='F' '''
                    query_gen_m=''' select Candidate_Name,count(*) from candidate_2020,voter_2020 where candidate_2020.C_Code=voter_2020.vote and Position='cs sec' and voter_2020.gender='M' '''
                    cursor.execute(query_gen_f)
                    data=cursor.fetchall()
                    print(data)
                    cursor.execute(query_gen_m)
                    data1=cursor.fetchall()
                    print(data1)
                if m=='b':
                    query_house='''select Candidate_Name,House,count(*) from candidate_2020,voter_2020 where candidate_2020.C_Code=voter_2020.vote and Position='cs sec' group by House'''
                    cursor.execute(query_house)
                    data=cursor.fetchall()
                    print(data)
            if c==2:
                print('a.gender wise')
                print('b.house wise')
                m=input("user pls")
                if m=='a':
                    query_gen_f='''select Candidate_Name,count(*) from candidate_2019,voter_2019 where candidate_2019.C_Code=voter_2019.vote and Position='cs sec' and voter_2019.gender='F' '''
                    query_gen_m=""" select Candidate_Name,count(*) from candidate_2019,voter_2019 where candidate_2019.C_Code=voter_2019.vote and Position='cs sec' and voter_2019.gender='M' """
                    cursor.execute(query_gen_f)
                    data=cursor.fetchall()
                    print(data)
                    cursor.execute(query_gen_m)
                    data1=cursor.fetchall()
                    print(data1)
                if m=='b':
                    query_house='''select Candidate_Name,House,count(*) from candidate_2019,voter_2019 where candidate_2019.C_Code=voter_2019.vote and Position='cs sec' group by House'''
                    cursor.execute(query_house)
                    data=cursor.fetchall()
                    print(data)
            if c==3:
                print('a.gender wise')
                print('b.house wise')
                m=input("user pls")
                if m=='a':
                    query_gen_f=''' select Candidate_Name,count(*) from candidate_2018,voter_2018 where candidate_2018.C_Code=voter_2018.vote and Position='cs sec' and voter_2018.gender='F' '''
                    query_gen_m=""" select Candidate_Name,count(*) from candidate_2018,voter_2018
                       where candidate_2018.C_Code=voter_2018.vote
                       and Position='cs sec' and voter_2018.gender='M' """
                    cursor.execute(query_gen_f)
                    data=cursor.fetchall()
                    print(data)
                    cursor.execute(query_gen_m)
                    data1=cursor.fetchall()
                    print(data1)
                if m=='b':
                    query_house=''' select Candidate_Name,House,count(*) from candidate_2018,voter_2018
                      where candidate_2018.C_Code=voter_2018.vote
                      and Position='cs sec'
                      group by House '''
                    cursor.execute(query_house)
                    data=cursor.fetchall()
                    print(data)
            if c==4:
                break
    if opt==4:
        break
