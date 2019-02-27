segundos = int(input('Por favor, entre com o número de segundos que deseja converter: '))

dias = segundos // (24 * 60 * 60)
seg_rest = segundos % (24 * 60 * 60)
horas = seg_rest // (60 * 60)
minutos = seg_rest // 60
seg = seg_rest % 60

print('{} dias, {} horas, {} minutos, {} segundos.'.format(dias, horas, minutos, seg))
