from django.db import models
import pandas as pd
from django.contrib.auth.models import AbstractUser

'''class StudentClass(models.Model):
    sem = models.IntegerField()
    branch = models.CharField(max_length=10)
    remarks = models.CharField(max_length=20)'''



class User(AbstractUser): 
    TEACHER = 1
    STUDENT = 2  
    ROLE_CHOICES = ((TEACHER, 'Teacher'), (STUDENT, 'Student'),)
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True, default=STUDENT)

    
  

class StudentClass(models.Model):
    SEMS = {"1YEAR":"1 YEAR","3SEM":"3 SEM","4SEM":"4 SEM","5SEM":"5 SEM","6SEM":"6 SEM"}    
    begining_date = models.DateTimeField(blank=True, null=True)
    branch = models.CharField(max_length=5, default="CME")
    ending_date = models.DateTimeField(blank=True, null=True)
    sem = models.CharField(max_length=10, primary_key=True, choices=SEMS)
    remarks = models.CharField(max_length=20)



class Students(models.Model):
    pin = models.CharField(max_length=20, primary_key=True)
    sname=models.CharField(max_length=20,default='student')
    fname=models.CharField(max_length=20,default='father')
    mname=models.CharField(max_length=20,default='mother')
    phno=models.CharField(max_length=12, default='123456')
    fphno=models.CharField(max_length=12, default='123445654')
    dob=models.DateTimeField(blank=True, null=True)
    gender=models.CharField(max_length=1,default='M')
    category=models.CharField(max_length=5,default='category')
    scategory=models.CharField(max_length=10,default='subcategory')
    religion=models.CharField(max_length=20,default='religion')
    sacno=models.CharField(max_length=20, default='1111')
    sifsc=models.CharField(max_length=20,default='1234')
    sbranch=models.CharField(max_length=20,default='CME')
    macno=models.CharField(max_length=22, default='1234')
    mifsc=models.CharField(max_length=20,default='ifsc')
    mbranch=models.CharField(max_length=20,default='motherac')
    email=models.CharField(max_length=30,default='@gmail.com')
    sscrank=models.IntegerField(default=1234)
    sschallticketno=models.CharField(max_length=20, default='123456')
    address=models.CharField(max_length=30,default='address')
    village=models.CharField(max_length=20,default='village')
    mandal=models.CharField(max_length=20,default='mandal')
    dist=models.CharField(max_length=20,default='district')
    allotedcategory=models.CharField(max_length=20,default='general')
    dateofjoining=models.DateTimeField(blank=True, null=True)
    polycetrank=models.IntegerField(default=1234)
    polycetno=models.IntegerField(default=1234)
    aadharno=models.CharField(max_length=22, default='111111111111')
    rationno=models.CharField(max_length=20,default='1234')
    tcno=models.IntegerField(default='1234')
    discontinueddate=models.DateTimeField(blank=True, null=True)
    odno=models.IntegerField(default='1234')
    odissueddate=models.DateTimeField(blank=True, null=True)
    tcissueddate=models.DateTimeField(blank=True, null=True)
    studycertificateissueddate=models.DateTimeField(blank=True, null=True)
    studentimage = models.ImageField(
        ("Title Image"), 
        upload_to='static/Images/student_image/',
         max_length=None,
         blank = True,null = True)
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
                mname=row['MNAME'],
                phno=row['PHNO'],
                fphno=row['FPHONE'],
                #dob=row['DOB'],
                gender=row['GENDER'],
                category=row['CATEGORY'],
                scategory=row['SCATEGORY'],
                religion=row['RELIGION'],
                sacno=row['SACNO'],
                sifsc=row['SIFSC'],
                sbranch=row['SBRANCH'],
                macno=row['MACNO'],
                mifsc=row['MIFSC'],
                mbranch=row['MBRNACH'],
                email=row['EMAIL'],
                #sscrank=row['SSCRANK'],
                sschallticketno=row['SSCHALLTICKETNO'],
                address=row['ADDRESS'],
                village=row['VILLAGE'],
                mandal=row['MANDAL'],
                dist=row['DIST'],
                allotedcategory=row['ALLOTEDCATEGORY'],
                #dateofjoining=row['DATEOFJOINING'],
                #polycetrank=row['POLYCETRANK'],
                #polycetno=row['POLYCETNO'],
                aadharno=row['AADHARNO'],
                rationno=row['RATIONNO'],
                #tcno=row['TCNO'],
                #tcissueddate=row['TCISSUEDDATE'],
                #discontinueddate=row['DISCOUNTINUEDDATE'],
                #odno=row['ODNO'],
                #odissueddate=row['ODISSUEDDATE'],
                #studycertificateissueddate=row['STUDYCERTIFICATEISSUEDDATE'],
    
               
    

            )
            a.save()


class Marks(models.Model):
    studentclass = models.ForeignKey(StudentClass, on_delete= models.CASCADE,default='SOME STRING')
    pin= models.CharField(max_length=20)    
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
            a = Marks(
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

class Unit2marks(models.Model):
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
            a = Unit2marks(
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

class Unit3marks(models.Model):
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
            a = Unit3marks(
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

                      





