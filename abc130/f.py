N = int(input())

x = [0] * N
y = [0] * N
d = [0] * N
Lx, Rx, Dx, Ux = [], [], [], []
Ly, Ry, Dy, Uy = [], [], [], []
xsort = []
ysort = []
for i in range(N):
    tx, ty, td = input().split()
    tx = int(tx)
    ty = int(ty)
    x[i], y[i], d[i] = tx, ty, td
    if td == 'L':
        Lx.append(tx)
        Ly.append(ty)
    elif td == 'R':
        Rx.append(tx)
        Ry.append(ty)
    elif td == 'D':
        Dx.append(tx)
        Dy.append(ty)
    elif td == 'U':
        Ux.append(tx)
        Uy.append(ty)
    xsort.append([tx, td])
    ysort.append([ty, td])
Lx.sort()
Rx.sort()
Dx.sort()
Ux.sort()
Ly.sort()
Ry.sort()
Dy.sort()
Uy.sort()
    
xsort.sort()
ysort.sort()

t = [0]

# lside
if xsort[0][1] == 'R' and (Lx or Ux or Dx):
    xlside = xsort[0][0]
    lt = 10**16 + 1
    if Lx:
        lt = min(lt, (Lx[0] - xlside) / 2)
    if Ux:
        lt = min(lt, Ux[0] - xlside)
    if Dx:
        lt = min(lt, Dx[0] - xlside)
    t.append(lt)

# rside
if xsort[-1][1] == 'L' and (Rx or Ux or Dx):
    xrside = xsort[-1][0]
    lt = 10**16 + 1
    if Rx:
        lt = min(lt, (xrside - Rx[-1]) / 2)
    if Ux:
        lt = min(lt, xrside - Ux[-1])
    if Dx:
        lt = min(lt, xrside - Dx[-1])
    t.append(lt)

# tail
if ysort[0][1] == 'U' and (Dy or Ly or Ry):
    ytail = ysort[0][0]
    lt = 10**16 + 1
    if Dy:
        lt = min(lt, (Dy[0] - ytail) / 2)
    if Ly:
        lt = min(lt, Ly[0] - ytail)
    if Ry:
        lt = min(lt, Ry[0] - ytail)
    t.append(lt)

# top
if ysort[-1][1] == 'D' and (Uy or Ly or Ry):
    ytop = ysort[-1][0]
    lt = 10**16 + 1
    if Uy:
        lt = min(lt, (ytop - Uy[-1]) / 2)
    if Ly:
        lt = min(lt, ytop - Ly[-1])
    if Ry:
        lt = min(lt, ytop - Ry[-1])
    t.append(lt)

ans = 10**32+1
for time in t:
    xl = 10**32 + 1
    if Lx:
        xl = min(xl, Lx[0] - time)
    if Rx:
        xl = min(xl, Rx[0] + time)
    if Dx:
        xl = min(xl, Dx[0])
    if Ux:
        xl = min(xl, Ux[0])
 
    xr = -(10**32 + 1)
    if Lx:
        xr = max(xr, Lx[-1] - time)
    if Rx:
        xr = max(xr, Rx[-1] + time)
    if Dx:
        xr = max(xr, Dx[-1])
    if Ux:
        xr = max(xr, Ux[-1])
 
    yd = 10**32 + 1
    if Ly:
        yd = min(yd, Ly[0])
    if Ry:
        yd = min(yd, Ry[0])
    if Dy:
        yd = min(yd, Dy[0] - time)
    if Uy:
        yd = min(yd, Uy[0] + time)
 
    yu = -(10**32 + 1)
    if Ly:
        yu = max(yu, Ly[-1])
    if Ry:
        yu = max(yu, Ry[-1])
    if Dy:
        yu = max(yu, Dy[-1] - time)
    if Uy:
        yu = max(yu, Uy[-1] + time)

    rec = (xr-xl)*(yu-yd)
    ans = min(ans, rec)
print(ans)

#ans = 10**32+1
#for time in t:
#    xl = xsort[0][0]
#    if xsort[0][1] == 'L':
#        xl -= time
#    elif xsort[0][1] == 'R':
#        xl += time
#
#    xr = xsort[-1][0]
#    if xsort[-1][1] == 'L':
#        xr -= time
#    elif xsort[-1][1] == 'R':
#        xr += time
#
#    yd = ysort[0][0]
#    if ysort[0][1] == 'D':
#        yd -= time
#    elif ysort[0][1] == 'U':
#        yd += time
#
#    yu = ysort[-1][0]
#    if ysort[-1][1] == 'D':
#        yu -= time
#    elif ysort[-1][1] == 'U':
#        yu += time
#
#    rec = (xr-xl)*(yu-yd)
#    ans = min(ans, rec)
#    
#print(ans)
