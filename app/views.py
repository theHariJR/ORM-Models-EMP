from django.shortcuts import render

# Create your views here.

from app.models import *
from django.http import HttpResponse

# get or create method:

# def insert_dept(request):
#     dno=int(input("Enter the Department number: "))
#     dna=input("Enter the Department name: ")
#     location=input("Enter the Location: ")
#     DO=Dept.objects.get_or_create(deptno=dno, dname=dna, loc=location)
#     if DO[1]:
#         return HttpResponse("Department Done newely")
#     else:
#         return HttpResponse("Department already exists")
    

# def insert_emp(request):
#     dno=int(input("Enter the Department number: "))
#     dna=input("Enter the Department name: ")
#     location=input("Enter the Location: ")

    
#     eno=int(input("Enter the Employee number: "))
#     ena=input("Enter the Employee name: ")
#     des=input("Enter the Designation: ")
#     hire=input("Enter the Hiredate: ")
#     salary=int(input("Enter the Department name: "))
#     commi=int(input("Enter the Department name: "))
#     dno=input("Enter the Department name: ")
#     mgrno=int(input("Enter the Department name: "))
#     DO=Dept.objects.get_or_create(deptno=dno, dname=dna, loc=location)[0]
#     EO=Emp.objects.get_or_create(empno=eno, ename=ena, job=des, hiredate=hire, sal=salary, comm=commi, deptno=dno, mgr=mgrno)
#     if EO[1]:
#         return HttpResponse("Employee Done newely")
#     else:
#         return HttpResponse("Employee already exists")


# retrieveing of data:

# def insert_dept(request):
#     d=int(input("Enter the Department number: "))
#     n=input("Enter the Department name: ")
#     l=input("Enter the Location: ")
#     DO=Dept.objects.get_or_create(deptno=d, dname=n, loc=l)
#     if DO[1]:
#         return HttpResponse("Department Done newely")
#     else:
#         return HttpResponse("Department already exists")
    

# def insert_emp(request):
#     # d=int(input("Enter the Department number: "))
#     # n=input("Enter the Department name: ")
#     # l=input("Enter the Location: ")

    
#     eno=int(input("Enter the Employee number: "))
#     ena=input("Enter the Employee name: ")
#     des=input("Enter the Designation: ")
#     hire=input("Enter the Hiredate: ")
#     salary=int(input("Enter the salary: "))
#     commi=int(input("Enter the commission: "))
#     dno=input("Enter the department number: ")
#     mgrno=input("Enter mgr no: ")
#     MO=Emp.objects.get(empno=mgrno)
#     if MO:
#         DO=Dept.objects.filter(deptno=int(dno))[0]
#         EO=Emp.objects.get_or_create(empno=eno, ename=ena, job=des, hiredate=hire, sal=salary, comm=commi, deptno=DO, mgr=MO)
#         if EO[0]:
#             return HttpResponse("Employee details retrieved")
#         else:
#             return HttpResponse("Not retrievable")
#     else:
#              return HttpResponse("No manager number")


def empdept(request):
    details=Emp.objects.select_related('deptno').all()
    details=Emp.objects.select_related('deptno').filter(job='Salesman')
    details=Emp.objects.select_related('deptno').filter(ename='Smith')
    details=Emp.objects.select_related('deptno').filter(ename__startswith='A')
    details=Emp.objects.select_related('deptno').filter(comm__isnull=True)
    details=Emp.objects.select_related('deptno').filter(hiredate__lt='2024-10-04')
    details=Emp.objects.select_related('deptno').filter(ename__startswith='A', comm__gte=4500)
    details=Emp.objects.select_related('deptno', 'mgr').all()
    details=Emp.objects.select_related('deptno', 'mgr').all().values('ename','deptno__dname', 'mgr')
    details=Emp.objects.prefetch_related('deptno', 'mgr').all().values('ename','deptno__dname', 'mgr')


    d={'details': details}
    return render(request,'empdept.html', context=d)



def deptemp(request):
    LDEO= Dept.objects.prefetch_related('emp_set').all()
    d={'LDEO': LDEO}
    return render(request, 'deptemp.html', context=d)

# LDEO = DEPT EMP OBJECT