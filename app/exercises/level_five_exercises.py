
employees = []

for i in range(1):
  name = input("Ingrese el nombre del empleado: ")
  last_name = input("Ingrese el apellido del empleado: ")
  base_salary = input("Ingrese el sueldo base del empleado: ")
  afap = input("Ingrese la AFAP del empleado: ")
  hire_date = input("Ingrese la fecha de ingreso del empleado (en formato dd/mm/yyyy): ")
  children = input("Ingrese la cantidad de hijos del empleado: ")

  employee = {
    "name": name,
    "last_name": last_name,
    "base_salary": base_salary,
    "afap": afap,
    "hire_date": hire_date,
    "children": children
  }

  employees.append(employee)


for employee in employees:
  base_salary = int(employee["base_salary"])
  afap = int(employee["afap"])
  children = int(employee["children"])

  # Calculamos la base imponible
  taxable_base = base_salary - (base_salary * afap) - (children * 10000)

  # Calculamos el pago a FONASA y AFAP
  fonasa_payment = taxable_base * 0.07
  afap_payment = afap * base_salary

  # Actualizamos el diccionario del empleado con los nuevos valores
  employee["taxable_base"] = taxable_base
  employee["fonasa_payment"] = fonasa_payment
  employee["afap_payment"] = afap_payment

print
# Podemos calcular el promedio de pago a los empleados de la siguiente manera:# stop