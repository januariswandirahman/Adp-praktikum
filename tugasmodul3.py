modal=float(input('masukan modal awal:='))
bunga=float(input("masukan suku bunga pertahun(%):="))
target=float(input("masukan target investasi:="))

tahun= 0
while modal<target:
    tahun+=1
    modal+=modal*(bunga/100)
    print(f"tahun ke-{tahun}:Rp{int(modal)}")
    print(f"target tercapai dalam{tahun} tahun")
    