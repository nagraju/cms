from django.db import models
import pandas as pd


class StudentClass(models.Model):
    sem = models.IntegerField()
    branch = models.CharField(max_length=10)
    remarks = models.CharField(max_length=20)
   

class Students(models.Model):
    pin = models.CharField(max_length=20)
    sname=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    address=models.CharField(max_length=30)
    village=models.CharField(max_length=20)
    mandal=models.CharField(max_length=20)
    dist=models.CharField(max_length=20)
    phno=models.CharField(max_length=12)
    fphno=models.CharField(max_length=12)
    email=models.CharField(max_length=30)
    dob =  models.DateTimeField()
    gender=models.CharField(max_length=1)
    studentclass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)



class Marks(models.Model):
    pin= models.CharField(max_length=20)
    unit =models.IntegerField()
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
    student = models.ForeignKey(Students, on_delete=models.CASCADE)
    pin=models.CharField(max_length=20)
    month=models.CharField(max_length=20)
    nfw=models.IntegerField()
    npd=models.IntegerField()
    twd=models.IntegerField()
    tpd=models.IntegerField()
    per = models.IntegerField()

   
    @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            a = Attendance(
                pin = row['pin'], 
                month = row['month'],
                nfw = row['nfw'],
                npd =  row['npd'],
                twd =  row['twd'],
                tpd =  row['tpd'],
                per =  row['per'],
            )
            a.save()

class Unit1marks(models.Model):
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
            a = Unit1marks(
                pin = row['pin'], 
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


