horas_trabalhadas = [40, 37, 45, 40, 40, 48]
ganho_por_hora = 20
hora_extra = 25

pagamentos = [ganho_por_hora * min(hours, 40) + hora_extra * max(0, hours - 40) 
              for hours in horas_trabalhadas]

print("Pagamentos:", pagamentos)