from django.db import models
import pandas as pd


'''class StudentClass(models.Model):
    sem = models.IntegerField()
    branch = models.CharField(max_length=10)
    remarks = models.CharField(max_length=20)'''
   
class StudentClass(models.Model):
    sem = models.CharField(max_length=10, primary_key=True)
    remarks = models.CharField(max_length=20)

class Students(models.Model):
    pin = models.CharField(max_length=20, primary_key=True)
    sname=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    village=models.CharField(max_length=20)
    mandal=models.CharField(max_length=20)
    dist=models.CharField(max_length=20)
    phno=models.CharField(max_length=12)
    fphno=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    dob =  models.DateTimeField(default='2020-1-1')
    gender=models.CharField(max_length=1)
    #studentclass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    
    @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            a = Students(
                pin = row['PIN'], 
                sname=row['NAME'],
                fname=row['FNAME'],
                address=row['ADDRESS'],
                village=row['VILLAGE'],
                mandal=row['MANDAL'],
                dist=row['DIST'],
                phno=row['PHNO'],
                fphno=row['FPHNO'],
                email=row['EMAIL'],
                dob=row['DOB'],
                gender=row['GENDER'],

            )
            a.save()


class Marks(models.Model):
    pin= models.CharField(max_length=20)    
    semister=models.CharField(max_length=20)
    s1=models.IntegerField() 
    s2=models.IntegerField() 
    s3=models.IntegerField() 
    s4=models.IntegerField() 
    s5=models.IntegerField() 
    s6=models.IntegerField() 
    s7=models.IntegerField() 
    s8=models.IntegerField() 
    s9=models.IntegerField() 
    s10=models.IntegerField() 
    s11=models.IntegerField() 
    s12=models.IntegerField() 


    @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            a = Marks(
                pin = row['pin'], 
                unit=row['unit'], 
                semister=row['semister'],
                s1 =row['s1'],
                s2=row['s2'], 
                s3=row['s3'],
                s4=row['s4'],
                s5=row['s5'],
                s6=row['s6'],
                s7=row['s7'],
                s8=row['s8'],
                s9=row['s9'], 
                s10=row['s10'],
                s11=row['s11'],
                s12=row['s12'],
                
            )
            a.save()

class Attendance(models.Model):        
    studentclass = models.ForeignKey(StudentClass, on_delete= models.CASCADE)
    month=models.CharField(max_length=20)
    nfw=models.IntegerField()
    npd=models.IntegerField()
    twd=models.IntegerField()
    tpd=models.IntegerField()
    per = models.IntegerField()
    student = models.ForeignKey(Students, to_field="pin", on_delete=models.CASCADE)
    

   
    @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            s = Students.objects.get(pin=row['PIN'])
            a = Attendance(
                student = s, 
                month = row['MONTH'],
                nfw = row['NFW'],
                npd =  row['NPD'],  
                twd = 0,
                tpd = 0,
                per = 0,
                studentclass_id = '4SEM',                          
            )
            a.save()

class Unit1marks(models.Model):
    studentclass = models.ForeignKey(StudentClass, on_delete= models.CASCADE,default='SOME STRING')
    s1=models.IntegerField() 
    s2=models.IntegerField() 
    s3=models.IntegerField() 
    s4=models.IntegerField() 
    s5=models.IntegerField() 
    s6=models.IntegerField() 
    s7=models.IntegerField() 
    s8=models.IntegerField() 
    s9=models.IntegerField() 
    s10=models.IntegerField() 
    s11=models.IntegerField() 
    s12=models.IntegerField()
    student = models.ForeignKey(Students, to_field="pin", on_delete=models.CASCADE,default='SOME STRING') 

    @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            s = Students.objects.get(pin=row['PIN'])
            a = Unit1marks(
                student=s,
                s1 =row['s1'],
                s2=row['s2'], 
                s3=row['s3'],
                s4=row['s4'],
                s5=row['s5'],
                s6=row['s6'],
                s7=0,
                s8=0,
                s9=0, 
                s10=0,
                s11=0,
                s12=0,
                studentclass_id = '4SEM', 
                
            )
            a.save()


