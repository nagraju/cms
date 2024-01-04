from mbts.models import StudentClass

s = StudentClass(sem = "1YEAR",remarks = "1st year")
s.save()
s = StudentClass(sem = "3SEM",remarks = "3 Sem")
s.save()
s = StudentClass(sem = "4SEM",remarks = "4 Sem")
s.save()
s = StudentClass(sem = "5SEM",remarks = "5 Sem")
s.save()