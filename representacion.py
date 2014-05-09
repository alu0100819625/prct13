import errorpi
import matplotlib.pyplot as pl
pl.figure(figsize=(10,10),dpi=80)

pl.subplot(2,1,1)
medida=[1, 2, 3, 4, 5]
errores=['1e-4','1e-5','1e-6','1e-7']
y10=l_e[0]
pl.plot(medida,y10,'-rh')
y50=l_e[1]
pl.plot(medida,y50, '-bo')
y100=l_e[2]
pl.plot(medida,y100,'-m+')
y150=l_e[3]
pl.plot(medida,y150,'-kd')
y500=l_e[4]
pl.plot(medida,y500,'-wp')
y550=l_e[5]
pl.plot(medida,y550,'-gs')
y1000=l_e[6]
pl.plot(medida,y1000,'-c*')
pl.xlim(0.0,7.9)
pl.ylim(-10.0,110.0)
pl.xticks(medida, errores,rotation=45)
pl.legend(['10','50','100','150','500','550','1000'],numpoints=1)
pl.title('Porcentajes de fallo')

pl.subplot(2,1,2)
medidat
size
time=
pl.plot(medidat,time,'-r')
pl.xlim(-40,1500)
pl.ylim(-0.1,0.5)
pl.xticks(medidat, ,rotation=45)

pl.show()
pl.savefig(dibujo.eps)
pl.savefig(dibujo.png)