from mbts.models import StudentClass]

s = StudentClass(sem = "1YEAR",remarks = "1st year", begining_date = "2023-12-01")
s.save()
s = StudentClass(sem = "3SEM",remarks = "3 Sem", begining_date = "2023-12-01")
s.save()
s = StudentClass(sem = "4SEM",remarks = "4 Sem", begining_date = "2023-12-01")
s.save()
s = StudentClass(sem = "5SEM",remarks = "5 Sem", begining_date = "2023-12-01")
s.save()



from mbts.models import User, Students
u = User(username="suviswas")

u.set_password("asd@123")


superuser
admin
admin


