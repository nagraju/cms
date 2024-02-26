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
    SEMS = {"1YEAR":"1 YEAR","3SEM":"3 SEM","4SEM":"4 SEM","5SEM":"5 SEM","6SEM":"6 SEM","COMPLETED":"COMPLETED","DETAINED":"DETAINED"}    
    begining_date = models.DateTimeField(blank=True, null=True)
    branch = models.CharField(max_length=5, default="CME")
    ending_date = models.DateTimeField(blank=True, null=True)
    sem = models.CharField(max_length=10, primary_key=True, choices=SEMS)
    remarks = models.CharField(max_length=20)



class Students(models.Model):
    pin = models.CharField(max_length=20, primary_key=True)
    sname=models.CharField(max_length=50, default='student')
    fname=models.CharField(max_length=50, default='father')
    mname=models.CharField(max_length=50, default='mother')
    sem = models.CharField(max_length=10, null=True, choices=StudentClass.SEMS,)
    phno=models.CharField(max_length=12, null = True)
    fphno=models.CharField(max_length=12, null=True)
    dob=models.DateTimeField(blank=True, null=True)
    gender=models.CharField(max_length=1,default='M')
    category=models.CharField(max_length=5,blank=True, null=True)
    scategory=models.CharField(max_length=10,blank=True, null=True)
    religion=models.CharField(max_length=20,blank=True, null=True)
    sacno=models.CharField(max_length=20, blank=True, null=True)
    sifsc=models.CharField(max_length=20,blank=True, null=True)
    sbranch=models.CharField(max_length=20,blank=True, null=True)
    macno=models.CharField(max_length=22, blank=True, null=True)
    mifsc=models.CharField(max_length=20,blank=True, null=True)
    mbranch=models.CharField(max_length=20,blank=True, null=True)
    email=models.CharField(max_length=30,blank=True, null=True)
    sscrank=models.IntegerField(default=1234, blank=True, null=True)
    sschallticketno=models.CharField(max_length=20, blank=True, null=True)
    address=models.CharField(max_length=30, blank=True, null=True)
    village=models.CharField(max_length=20, blank=True, null=True)
    mandal=models.CharField(max_length=20, blank=True, null=True)
    dist=models.CharField(max_length=20, blank=True,null=True)
    allotedcategory=models.CharField(max_length=20,blank=True, null=True)
    dateofjoining=models.DateTimeField(blank=True, null=True)
    polycetrank=models.IntegerField(blank=True,null=True)
    polycetno=models.IntegerField(blank=True,null=True)
    aadharno=models.CharField(max_length=22, blank=True,null=True)
    rationno=models.CharField(max_length=20,blank=True,null=True)
    tcno=models.IntegerField(blank=True, null=True)
    discontinueddate=models.DateTimeField(blank=True, null=True)
    odno=models.IntegerField(blank=True,null=True)
    odissueddate=models.DateTimeField(blank=True, null=True)
    tcissueddate=models.DateTimeField(blank=True, null=True)
    studycertificateissueddate=models.DateTimeField(blank=True, null=True)
    
    studentimage = models.ImageField(
        ("Title Image"), 
        upload_to='static/Images/student_image/',
         max_length=None,
         blank = True,null = True)
    #studentclass = models.ForeignKey(StudentClass, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null= True)

    

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

                      





