sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outras = 19849.53

total = sp + rj + mg + es + outras
sp_p = (sp / total) * 100
rj_p = (rj / total) * 100
mg_p = (mg / total) * 100
es_p = (es / total) * 100
outras_p = (outras / total) * 100

print(f'São Paulo: R$ {sp:.2f} ({sp_p:.2f}%)')
print(f'Rio de Janeiro: R$ {rj:.2f} ({rj_p:.2f}%)')
print(f'Minas Gerais: R$ {mg:.2f} ({mg_p:.2f}%)')
print(f'Espírito Santo: R$ {es:.2f} ({es_p:.2f}%)')
print(f'Outras: R$ {outras:.2f} ({outras_p:.2f}%)')
print(f'Total: R$ {total:.2f}')
