from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    dname=models.CharField(max_length=100, null=False)
    loc=models.CharField(max_length=100)

    def __str__(self):
        return self.dname + " " + str(self.deptno)
    
class Emp(models.Model):
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100, null= False)
    job=models.CharField(max_length=50)
    hiredate=models.DateField(auto_now_add=True)
    sal=models.DecimalField(max_digits=8, decimal_places=2, null=False)
    comm=models.DecimalField(max_digits=8,decimal_places=2,null=True, blank=True)
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    mgr=models.ForeignKey('self',on_delete=models.SET_NULL,null=True, blank=True)

    def __str__(self):
        return self.ename