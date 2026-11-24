# LWIR objektif + govde geometrisi (SpaceClaim Script Editor)
# Optik eksen: +Y, birimler: mm (MM() fonksiyonu metreye cevirir)
# Kaynak: Zemax v1_nominal.zmx (f = 50 mm, f/1.25, Ge / ZnSe / Ge)
part = GetRootPart()
N = Direction.DirZ
M = Direction.DirX

# ---------- MERCEKLER VE DEDEKTOR ----------
# Mercek 1 (Germanyum): D41 x 5, Y = 0..5
pl = Plane.Create(Frame.Create(Point.Create(0, MM(0), 0), N, M))
DesignBody.Create(part, "Mercek1_Ge", Body.ExtrudeProfile(CircleProfile(pl, MM(20.5), PointUV.Origin), MM(5)))

# Mercek 2 (ZnSe): D30 x 4, Y = 26.1..30.1
pl = Plane.Create(Frame.Create(Point.Create(0, MM(26.1), 0), N, M))
DesignBody.Create(part, "Mercek2_ZnSe", Body.ExtrudeProfile(CircleProfile(pl, MM(15), PointUV.Origin), MM(4)))

# Mercek 3 (Germanyum): D16.4 x 5, Y = 62..67
pl = Plane.Create(Frame.Create(Point.Create(0, MM(62), 0), N, M))
DesignBody.Create(part, "Mercek3_Ge", Body.ExtrudeProfile(CircleProfile(pl, MM(8.2), PointUV.Origin), MM(5)))

# Dedektor (Silisyum): D12 x 1, Y = 71.9..72.9
pl = Plane.Create(Frame.Create(Point.Create(0, MM(71.9), 0), N, M))
DesignBody.Create(part, "Dedektor_Si", Body.ExtrudeProfile(CircleProfile(pl, MM(6), PointUV.Origin), MM(1)))

# ---------- ALUMINYUM GOVDE ----------
# Mercek 1 halkasi: D41-D52, Y = 0..5
pl = Plane.Create(Frame.Create(Point.Create(0, MM(0), 0), N, M))
b = Body.ExtrudeProfile(CircleProfile(pl, MM(26), PointUV.Origin), MM(5))
b.Subtract(Body.ExtrudeProfile(CircleProfile(pl, MM(20.5), PointUV.Origin), MM(5)))
DesignBody.Create(part, "Govde_Halka1", b)

# Tup: D46-D52, Y = 5..80
pl = Plane.Create(Frame.Create(Point.Create(0, MM(5), 0), N, M))
b = Body.ExtrudeProfile(CircleProfile(pl, MM(26), PointUV.Origin), MM(75))
b.Subtract(Body.ExtrudeProfile(CircleProfile(pl, MM(23), PointUV.Origin), MM(75)))
DesignBody.Create(part, "Govde_Tup", b)

# Mercek 2 halkasi: D30-D46, Y = 26.1..30.1
pl = Plane.Create(Frame.Create(Point.Create(0, MM(26.1), 0), N, M))
b = Body.ExtrudeProfile(CircleProfile(pl, MM(23), PointUV.Origin), MM(4))
b.Subtract(Body.ExtrudeProfile(CircleProfile(pl, MM(15), PointUV.Origin), MM(4)))
DesignBody.Create(part, "Govde_Halka2", b)

# Mercek 3 halkasi: D16.4-D46, Y = 62..67
pl = Plane.Create(Frame.Create(Point.Create(0, MM(62), 0), N, M))
b = Body.ExtrudeProfile(CircleProfile(pl, MM(23), PointUV.Origin), MM(5))
b.Subtract(Body.ExtrudeProfile(CircleProfile(pl, MM(8.2), PointUV.Origin), MM(5)))
DesignBody.Create(part, "Govde_Halka3", b)

# Dedektor halkasi: D12-D46, Y = 71.9..72.9
pl = Plane.Create(Frame.Create(Point.Create(0, MM(71.9), 0), N, M))
b = Body.ExtrudeProfile(CircleProfile(pl, MM(23), PointUV.Origin), MM(1))
b.Subtract(Body.ExtrudeProfile(CircleProfile(pl, MM(6), PointUV.Origin), MM(1)))
DesignBody.Create(part, "Govde_HalkaDet", b)

# Arka kapak: D52 dolu disk, Y = 80..83
pl = Plane.Create(Frame.Create(Point.Create(0, MM(80), 0), N, M))
DesignBody.Create(part, "Govde_Kapak", Body.ExtrudeProfile(CircleProfile(pl, MM(26), PointUV.Origin), MM(3)))
