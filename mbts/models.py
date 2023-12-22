from django.db import models
import pandas as pd

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



class Marks(models.Model):
    pin= models.CharField(max_length=20)
    semister=models.CharField(max_length=20)
    101=models.IntegerField() 
    102=models.IntegerField() 
    103=models.IntegerField() 
    104=models.IntegerField() 
    105=models.IntegerField() 
    106=models.IntegerField() 
    107=models.IntegerField() 
    108=models.IntegerField() 
    109=models.IntegerField() 
    110=models.IntegerField() 
    301=models.IntegerField() 
    302=models.IntegerField() 
    303=models.IntegerField() 
    304=models.IntegerField() 
    305=models.IntegerField() 
    306=models.IntegerField() 
    307=models.IntegerField() 
    308=models.IntegerField() 
    309=models.IntegerField() 
    310=models.IntegerField() 
    311=models.IntegerField() 
    401=models.IntegerField() 
    402=models.IntegerField() 
    403=models.IntegerField() 
    404=models.IntegerField() 
    405=models.IntegerField() 
    406=models.IntegerField() 
    407=models.IntegerField() 
    408=models.IntegerField() 
    409=models.IntegerField() 
    410=models.IntegerField() 
    411=models.IntegerField() 
    412=models.IntegerField() 
    501=models.IntegerField()
    502=models.IntegerField()
    503=models.IntegerField()
    504=models.IntegerField()
    505=models.IntegerField()
    506=models.IntegerField()
    507=models.IntegerField()
    508=models.IntegerField()
    509=models.IntegerField()
    510=models.IntegerField()
    511=models.IntegerField()
    512=models.IntegerField()

   

   
     @staticmethod
    def import_csv(filename):      
        tmp_data=pd.read_csv(filename,sep=',')    
        row_iter = tmp_data.iterrows()    
        for i,row in row_iter:
            a = Marks(
                pin = row['pin'], 
                semister = row['sem'],
                s101 =row['101'],
                s102=row['102'], 
                s103=row['103'],
                s104=row['104'],
                s105=row['105'],
                s106=row['106'],
                s107=row['107'],
                s108=row['108'],
                s109=row['109'], 
                s110=row['110'],
                s301=row['301'],
                s302=row['302'],
                s303=row['303'],
                s304=row['304'],
                s305=row['305'],
                s306=row['306'],
                s307=row['307'],
                s308=row['308'],
                s309=row['309'],
                s310=row['310'],
                s311=row['311'],
                s401=row['401'],
                s402=row['402'],
                s403=row['403'],
                s404=row['404'],
                s405=row['405'],
                s406=row['406'],
                s407=row['407'],
                s408=row['408'],
                s409=row['409'],
                s410=row['410'],
                s411=row['411'],
                s412=row['412'],
                s501=row['501'],
                s502=row['502'],
                s503=row['503'],
                s504=row['504'],
                s505=row['505'],
                s506=row['506'],
                s507=row['507'],
                s508=row['508'],
                s509=row['509'],
                s510=row['510'],
                s511=row['511'],
                s512=row['512'],
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

