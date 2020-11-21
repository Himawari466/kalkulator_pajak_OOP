#!/usr/bin/env python3
# Kalkulator Pajak OOP
# 2020 - Himawari466
# https://mit-license.org/

class Pajak(object):
  def __init__(self, nama, gaji, lembur):
    self._nama = nama
    self._gaji = gaji
    self._lembur = lembur

  def Get_Nama(self):
    return self._nama

  def Get_Gaji(self):
    return self._gaji

  def Get_Lembur(self):
    return self._lembur

class PajakBujang(Pajak):
  def Hitung_Pajak(self):
    gaji = self._gaji
    lembur = self._lembur
    lembur_perjam = 8000
    gaji_perbulan = gaji + (lembur *lembur_perjam)
    if gaji >= 3000000:
      pajak = gaji_perbulan * (15 / 100)
      asuransi = 120000
    else:
      pajak = gaji_perbulan * (10 / 100)
      asuransi = 100000
    gaji_akhir = gaji_perbulan - round(pajak) - asuransi
    return [gaji_perbulan, round(pajak), round(asuransi), round(gaji_akhir)]

class PajakMenikah(Pajak):
  def __init__(self, nama, gaji, lembur, anak):
    Pajak.__init__(self, nama, gaji, lembur)
    self._anak = anak

  def Get_Anak(self):
    return self._anak

  def Hitung_Pajak(self):
    gaji = self._gaji
    lembur = self._lembur
    lembur_perjam = 9000
    tunjangan = 40000
    tunjangan_anak = self._anak * 30000
    total_tunjangan = tunjangan + tunjangan_anak
    gaji_perbulan = gaji + (lembur *lembur_perjam)
    if gaji >= 3000000:
      pajak = gaji_perbulan * (15 / 100)
      asuransi = 150000
    else:
      pajak = gaji_perbulan * (10 / 100)
      asuransi = 120000
    gaji_akhir = gaji_perbulan - round(pajak) - asuransi + total_tunjangan
    return [gaji_perbulan, round(pajak), round(asuransi), total_tunjangan, round(gaji_akhir)]



if __name__ == "__main__":
  exit("File adalah module")
