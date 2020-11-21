#!/usr/bin/env python3
# Kalkulator Pajak OOP
# 2020 - Himawari466
# https://mit-license.org/

from pajak import PajakBujang, PajakMenikah
from plumbum.cmd import clear
from termcolor import colored
from shutil import get_terminal_size
import locale

locale.setlocale(locale.LC_ALL, "id_ID.UTF-8")
kolomlayar = get_terminal_size().columns

def wiper():
  print(clear())

def separator():
  print("=" * kolomlayar)

def rupiah(i):
  return locale.currency(i, grouping=True)

class Main:
  def menu():
    while True:
      wiper()
      separator()
      print(f"{colored('Kalkulator Pajak Karyawan'.center(kolomlayar), 'green')}")
      separator()
      print(f"{colored('[1]', 'white')} {colored('Karyawan Bujang', 'green')}")
      print(f"{colored('[2]', 'white')} {colored('Karyawan Menikah', 'green')}")
      print(f"{colored('[e]', 'white')} {colored('Exit', 'red')}")
      pil = input(">> ")
      if pil == "1":
        Main.bujang()
      elif pil == "2":
        Main.menikah()
      elif pil == "00":
        Main.exit()
      elif pil in ["e", "E"]:
        exit("Terima kasih")
      else:
        input("Pilihan tidak valid")
        continue

  def bujang():
    while True:
      wiper()
      separator()
      print(f"{colored('Pajak Karyawan Bujang'.center(kolomlayar), 'blue')}")
      separator()
      nama = input(f"{colored('Nama karyawan', 'blue')}\t{colored(':', 'blue')} ")
      if nama == "":
        pil = input("/!\ Belum diinput, [enter] Reset, [m] Menu")
        if not pil == "":
          break
        else:
          continue
      gaji = input(f"{colored('Gaji RP', 'blue')}\t\t{colored(':', 'blue')} ")
      if gaji == "":
        input("/!\ Belum diinput")
        continue
      try:
        gaji = int(gaji)
      except ValueError:
        input("/!\ Format angka tidak valid")
        continue
      lembur = input(f"{colored('Total jam lembur:', 'blue')} ")
      try:
        lembur = int(lembur)
      except ValueError:
        input("/!\ Format angka tidak valid")
        continue
      pil = input(f"\nYakin sudah benar?\n{colored('[enter]', 'white')} {colored('Lanjut', 'green')}\n{colored('[r]', 'white')} {colored('Reset', 'green')}\n>> ")
      if not pil == "":
        continue
      hitungan = PajakBujang(nama, gaji, lembur)
      wiper()
      separator()
      print(f"{colored('Total Pajak Karyawan Bujang'.center(kolomlayar), 'blue')}")
      separator()
      print(f"{colored('Nama', 'blue')}\t\t{colored(':', 'blue')} {hitungan.Get_Nama()}")
      print(f"{colored('Gaji', 'blue')}\t\t{colored(':', 'blue')} {hitungan.Get_Gaji()}")
      print(f"{colored('Jam lembur', 'blue')}\t{colored(':', 'blue')} {hitungan.Get_Lembur()} jam")
      print(f"\n\n{colored('Hitungan', 'green')}")
      print(f"{colored('Gaji & lembur', 'green')}\t{colored(':', 'green')} {hitungan.Hitung_Pajak()[0]:>10}")
      print(f"{colored('Pajak', 'green')}\t\t{colored(':', 'green')} -{hitungan.Hitung_Pajak()[1]:>9}")
      print(f"{colored('Asuransi', 'green')}\t{colored(':', 'green')} -{hitungan.Hitung_Pajak()[2]:>9}")
      print(f"\n{colored('Gaji total', 'green')}\t{colored(':', 'green')} {hitungan.Hitung_Pajak()[3]:>10}")
      print(f"\t\t{colored(':', 'green')} {rupiah(round(hitungan.Hitung_Pajak()[3], -2))[:-3]}")
      separator()
      pil = input(f"\n{colored('[enter]', 'white')} {colored('Ulangi', 'green')}\n{colored('[m]', 'white')} {colored('Menu', 'green')}\n>> ")
      if pil == "":
        continue
      elif pil in ["m", "M"]:
        break

  def menikah():
    while True:
      wiper()
      separator()
      print(f"{colored('Pajak Karyawan Menikah'.center(kolomlayar), 'magenta')}")
      separator()
      nama = input(f"{colored('Nama karyawan', 'magenta')}\t{colored(':', 'magenta')} ")
      if nama == "":
        pil = input("/!\ Belum diinput, [enter] Reset, [m] Menu")
        if not pil == "":
          break
        else:
          continue
      gaji = input(f"{colored('Gaji RP', 'magenta')}\t\t{colored(':', 'magenta')} ")
      if gaji == "":
        input("/!\ Belum diinput")
        continue
      try:
        gaji = int(gaji)
      except ValueError:
        input("/!\ Format angka tidak valid")
        continue
      lembur = input(f"{colored('Total jam lembur:', 'magenta')} ")
      try:
        lembur = int(lembur)
      except ValueError:
        input("/!\ Format angka tidak valid")
        continue
      anak = input(f"{colored('Jumlah anak', 'magenta')}\t{colored(':', 'magenta')} ")
      try:
        anak = int(anak)
      except ValueError:
        input("/!\ Format angka tidak valid")
        continue
      pil = input(f"\nYakin sudah benar?\n{colored('[enter]', 'white')} {colored('Lanjut', 'green')}\n{colored('[r]', 'white')} {colored('Reset', 'green')}\n>> ")
      if not pil == "":
        continue
      hitungan = PajakMenikah(nama, gaji, lembur, anak)
      wiper()
      separator()
      print(f"{colored('Total Pajak Karyawan Bujang'.center(kolomlayar), 'magenta')}")
      separator()
      print(f"{colored('Nama', 'magenta')}\t\t{colored(':', 'magenta')} {hitungan.Get_Nama()}")
      print(f"{colored('Gaji', 'magenta')}\t\t{colored(':', 'magenta')} {hitungan.Get_Gaji()}")
      print(f"{colored('Jam lembur', 'magenta')}\t{colored(':', 'magenta')} {hitungan.Get_Lembur()} jam")
      print(f"{colored('Jumlah anak', 'magenta')}\t{colored(':', 'magenta')} {hitungan.Get_Anak()} anak")
      print(f"\n\n{colored('Hitungan', 'green')}")
      print(f"{colored('Gaji & lembur', 'green')}\t{colored(':', 'green')} {hitungan.Hitung_Pajak()[0]:>10}")
      print(f"{colored('Pajak', 'green')}\t\t{colored(':', 'green')} -{hitungan.Hitung_Pajak()[1]:>9}")
      print(f"{colored('Asuransi', 'green')}\t{colored(':', 'green')} -{hitungan.Hitung_Pajak()[2]:>9}")
      print(f"{colored('Tunjangan', 'green')}\t{colored(':', 'green')} +{hitungan.Hitung_Pajak()[3]:>9}")
      print(f"\n{colored('Gaji total', 'green')}\t{colored(':', 'green')} {hitungan.Hitung_Pajak()[4]:>10}")
      print(f"\t\t{colored(':', 'green')} {rupiah(round(hitungan.Hitung_Pajak()[4], -2))[:-3]}")
      separator()
      pil = input(f"\n{colored('[enter]', 'white')} {colored('Ulangi', 'green')}\n{colored('[m]', 'white')} {colored('Menu', 'green')}\n>> ")
      if pil == "":
        continue
      elif pil in ["m", "M"]:
        break



if __name__ == "__main__":
  Main.menu()
