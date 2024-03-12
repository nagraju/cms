from django.db import models
import pandas as pd
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver

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
    email=models.CharField(max_length=30)
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


class TotalAttendance(models.Model):
    student = models.ForeignKey(Students, to_field="pin", on_delete=models.CASCADE)
    sem = models.CharField(max_length=10)
    nwd=models.IntegerField(default=0)
    npd=models.IntegerField(default=0)
    twd=models.IntegerField(default=0)
    tpd=models.IntegerField(default=0)




@receiver(models.signals.pre_save, sender=Students)
def execute_after_save(sender, instance, *args, **kwargs):
    if instance.user_id is None:
        TotalAttendance.objects.create(student=instance, sem=instance.sem)
        u = User.objects.create(username=instance.email)        
        u.set_password('asdf@123')
        u.save()
        instance.user = u
        
        
    

class Marks(models.Model):
    #studentclass = models.ForeignKey(StudentClass, on_delete= models.CASCADE,default='SOME STRING')
    pin= models.CharField(max_length=20)   
    sem = models.CharField(max_length=5) 
    s1=models.IntegerField() 
    s1i=models.IntegerField() 
    s1e=models.IntegerField() 
    s1t=models.IntegerField() 
    s1s=models.CharField(max_length=30,default='pass or fail')
    s2=models.IntegerField()
    s2i=models.IntegerField() 
    s2e=models.IntegerField() 
    s2t=models.IntegerField() 
    s2s=models.CharField(max_length=30,default='pass or fail')
    s3=models.IntegerField()
    s3i=models.IntegerField() 
    s3e=models.IntegerField() 
    s3t=models.IntegerField() 
    s3s=models.CharField(max_length=30,default='pass or fail')
    s4=models.IntegerField()
    s4i=models.IntegerField() 
    s4e=models.IntegerField() 
    s4t=models.IntegerField() 
    s4s=models.CharField(max_length=30,default='pass or fail') 
    s5=models.IntegerField()
    s5i=models.IntegerField() 
    s5e=models.IntegerField() 
    s5t=models.IntegerField() 
    s5s=models.CharField(max_length=30,default='pass or fail') 
    s6=models.IntegerField()
    s6i=models.IntegerField() 
    s6e=models.IntegerField() 
    s6t=models.IntegerField() 
    s6s=models.CharField(max_length=30,default='pass or fail') 
    s7=models.IntegerField()
    s7i=models.IntegerField() 
    s7e=models.IntegerField() 
    s7t=models.IntegerField() 
    s7s=models.CharField(max_length=30,default='pass or fail') 
    s8=models.IntegerField()
    s8i=models.IntegerField() 
    s8e=models.IntegerField() 
    s8t=models.IntegerField() 
    s8s=models.CharField(max_length=30,default='pass or fail') 
    s9=models.IntegerField()
    s9i=models.IntegerField() 
    s9e=models.IntegerField() 
    s9t=models.IntegerField() 
    s9s=models.CharField(max_length=30,default='pass or fail') 
    s10=models.IntegerField()
    s10i=models.IntegerField() 
    s10e=models.IntegerField() 
    s10t=models.IntegerField() 
    s10s=models.CharField(max_length=30,default='pass or fail') 
    s11=models.IntegerField() 
    s11i=models.IntegerField() 
    s11e=models.IntegerField() 
    s11t=models.IntegerField() 
    s11s=models.CharField(max_length=30,default='pass or fail')
    s12=models.IntegerField()
    s12i=models.IntegerField() 
    s12e=models.IntegerField() 
    s12t=models.IntegerField() 
    s12s=models.CharField(max_length=30,default='pass or fail')
    student = models.ForeignKey(Students, to_field="pin", on_delete=models.CASCADE,default='SOME STRING')

    def to_subjects(self):
        subjects = []
        for i in range(1,11):  
            s = {}          
            s["sub_code"] = getattr(self,'s%s'%i)
            s["sub_int"] = getattr(self,'s%si'%i)
            s["sub_ext"] = getattr(self,'s%se'%i)
            s["sub_total"] = getattr(self,'s%st'%i)
            s["sub_status"] = getattr(self,'s%ss'%i)
            subjects.append(s)       
        return {'sem':self.sem,'subjects':subjects}



    @staticmethod
    def import_csv(sem,filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            s = Students.objects.get(pin=row['pin'])
            a = Marks(
                student = s, 
                sem = sem,
                s1 =row['s1'],
                s1i=row['s1i'],
                s1e=row['s1e'],
                s1t=row['s1t'],
                s1s=row['s1s'],
                s2 =row['s2'],
                s2i=row['s2i'],
                s2e=row['s2e'],
                s2t=row['s2t'],
                s2s=row['s2s'],
                s3 =row['s3'],
                s3i=row['s3i'],
                s3e=row['s3e'],
                s3t=row['s3t'],
                s3s=row['s3s'],
                s4 =row['s4'],
                s4i=row['s4i'],
                s4e=row['s4e'],
                s4t=row['s4t'],
                s4s=row['s4s'],
                s5 =row['s5'],
                s5i=row['s5i'],
                s5e=row['s5e'],
                s5t=row['s5t'],
                s5s=row['s5s'],
                s6 =row['s6'],
                s6i=row['s6i'],
                s6e=row['s6e'],
                s6t=row['s6t'],
                s6s=row['s6s'],
                s7=row['s7'],
                s7i=row['s7i'],
                s7e=row['s7e'],
                s7t=row['s7t'],
                s7s=row['s7s'],
                s8=row['s8'],
                s8i=row['s8i'],
                s8e=row['s8e'],
                s8t=row['s8t'],
                s8s=row['s8s'],
                s9=row['s9'],
                s9i=row['s9i'],
                s9e=row['s9e'],
                s9t=row['s9t'],
                s9s=row['s9s'],
                s10=row['s10'],
                s10i=row['s10i'],
                s10e=row['s10e'],
                s10t=row['s10t'],
                s10s=row['s10s'],
                s11=row['s11'],
                s11i=row['s11i'],
                s11e=row['s11e'],
                s11t=row['s11t'],
                s11s=row['s11s'],
                s12=row['s12'],
                s12i=row['s12i'],
                s12e=row['s12e'],
                s12t=row['s12t'],
                s12s=row['s12s'],
                    
                
            )
            a.save()

class Attendance(models.Model):        
    #studentclass = models.ForeignKey(StudentClass, on_delete= models.CASCADE)
    sem = models.CharField(max_length=10)
    month=models.CharField(max_length=20)
    nfw=models.IntegerField(default=0)
    npd=models.IntegerField(default=0)
    twd=models.IntegerField(default=0)
    tpd=models.IntegerField(default=0)
    per = models.IntegerField(default=0)
    student = models.ForeignKey(Students, to_field="pin", on_delete=models.CASCADE)
    

   
    @staticmethod
    def import_csv(filename, sem):      
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
                #studentclass_id = '4SEM', 
                sem = sem                         
            )
            a.save()



@receiver(models.signals.post_save, sender=Attendance)
def attendance_after_save(sender, instance, created, *args, **kwargs):
    if created:
        a = TotalAttendance.objects.filter(student=instance.student, sem=instance.sem).first()
        a.twd= a.twd + instance.nfw
        a.tpd= a.tpd + instance.npd
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

                      





