import schemdraw
import schemdraw.elements as elm
import math
# use IEC style
elm.style(elm.STYLE_IEC)
d = schemdraw.Drawing()
Line = d.add(elm.Line().right().length(1))
Battery = d.add(elm.BatteryCell())
d.add(elm.Switch())
d.add(elm.Line().down().length(6))
DotB = d.add(elm.Dot().label('$B$', loc='right'))
d.push()
d.add(elm.ResistorVarIEC().theta(135).flip().label('$R_0$').length(5))
DotC = d.add(elm.Dot().label('$C$'))
d.push()
Rb = d.add(elm.Resistor().theta(225).length(5).label('$R_b$'))
DotA = d.add(elm.Dot().label('$A$', loc='left'))
d.add(elm.Line().up().toy(Line.start))
d.pop()
# rewrite the MeterA for MeterG
MeterG = elm.MeterA()
d.add(MeterG.down().length(5 * 2 / math.sqrt(2)))
MeterG.segments[2].text = 'G'
DotD = d.add(elm.Dot().label('$D$', loc='bottom'))
d.add(elm.Resistor().theta(135).length(5).label('$R_a$', loc='bottom').hold())
d.add(elm.Resistor().theta(45).length(5).label('$R_x$', loc='bottom'))
# add arrow for current
d.add(elm.Wire('-', arrow='->').at(DotA.center).delta(1, 1).label('$I_b$', loc='top'))
d.add(elm.Wire('-', arrow='->').at(DotC.center).delta(1, -1).label('$I_0$', loc='top'))
d.add(elm.Wire('-', arrow='->').at(DotA.center).delta(1, -1).label('$I_a$', loc='bottom'))
d.add(elm.Wire('-', arrow='->').at(DotD.center).delta(1, 1).label('$I_x$', loc='bottom'))
d.draw()
