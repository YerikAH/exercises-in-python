import datetime


BONUS_PERCENTAGE = 0.01
FAMILY_ALLOWANCE_PERCENTAGE = 0.05
HEALTH_INSURANCE_PERCENTAGE = 0.07
AFP_1_PERCENTAGE = 0.12
AFP_2_PERCENTAGE = 0.114

employee_data = []
total_base_taxable = 0
total_health_insurance = 0
total_afp_1 = 0
total_afp_2 = 0

def calculate_months_worked(hire_date):
  today = datetime.date.today()
  hire_year, hire_month, hire_day = map(int, hire_date.split("/"))
  hire_date = datetime.date(hire_year, hire_month, hire_day)
  months_worked = (today.year - hire_date.year) * 12 + today.month - hire_date.month
  return months_worked

for i in range(1):
  try:
    name = input("Ingresa el nombre del empleado: ")
    surname = input("Ingresa el apellido del empleado: ")
    base_salary = float(input("Ingresa el sueldo base del empleado: "))
    afp = int(input("Ingresa el número de la AFP del empleado (1 o 2): "))
    hire_date = input("Ingresa la fecha de ingreso del empleado (en formato dd/mm/yyyy): ")
    children = int(input("Ingresa la cantidad de hijos del empleado: "))

    months_worked = calculate_months_worked(hire_date)
    bonus = base_salary * BONUS_PERCENTAGE * months_worked
    family_allowance = base_salary * FAMILY_ALLOWANCE_PERCENTAGE * children
    health_insurance = base_taxable * HEALTH_INSURANCE_PERCENTAGE
    if afp == 1:
      afp = base_taxable * AFP_1_PERCENTAGE
    elif afp == 2:
      afp = base_taxable * AFP_2_PERCENTAGE
    else:
      raise ValueError("El número de AFP debe ser 1 o 2")

    employee_data.append({
      "name": name,
      "surname": surname,
      "base_salary": base_salary,
      "bonus": bonus,
      "family_allowance": family_allowance,
      "base_taxable": base_taxable,
      "health_insurance": health_insurance,
      "afp": afp
    })

    total_base_taxable += base_taxable
    total_health_insurance += health_insurance
    total_afp_1 += afp
  except ValueError as e:
    print("Error de entrada de datos:", e)
  average_base_taxable = total_base_taxable / 10
  average_health_insurance = total_health_insurance / 10
  average_afp_1 = total_afp_1 / 10
  average_afp_2 = total_afp_2 / 10

  print("Promedio de base imponible:", average_base_taxable)
  print("Promedio de seguro de salud:", average_health_insurance)
  print("Promedio de AFP 1:", average_afp_1)
  print("Promedio de AFP 2:", average_afp_2)

