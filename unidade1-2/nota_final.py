# Universidade Federal de Campina Grande - UFCG
# Programação - 1
# Guilherme Aureliano
# Nota na Final

print('== Estágio 1 ==')
peso1 = float(input('Peso? '))
nota1 = float(input('Nota? '))

print('== Estágio 2 ==')
peso2 = float(input('Peso? '))
nota2 = float(input('Nota? '))

print('== Estágio 3 ==')
peso3 = float(input('Peso? '))
nota3 = float(input('Nota? '))

print('== Resultados ==')
media_parcial = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)
print('Média parcial: {:.1f}'.format(media_parcial)) 

desejo_5 = (5 - (media_parcial * 0.6)) / 0.4
desejo_7 = (7 - (media_parcial * 0.6)) / 0.4
print('Nota na final, pra média 5.0 = {:.1f}'.format(desejo_5))
print('Nota na final, pra média 7.0 = {:.1f}'.format(desejo_7))

     
    
    
    
    
    
