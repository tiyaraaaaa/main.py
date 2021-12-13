import os

print("+---------------------------------------------------+")
print("|\tSelamat Datang di Aplikasi Sistem Pakar \t\t|")
print("|\tDeteksi Penyakit Anthrax & Scabies Pada Sapi \t|")
print("+---------------------------------------------------+")
hewan = input("Nama Hewan\t: ")
pilihan = input("\nApakah Anda Ingin Melakukan Diagnosa pada Ternak Sapi ? (y/n) : ")

os.system("clear")

while pilihan == "y" :
  print("\nApakah Ternak Sapi Anda Mengalami Gejala Berikut Ini ?")
  print("1. Demam")
  print("2. Lemah")
  print("3. Diare")
  diag1 = input("Jawab (y/n) : ")

  if diag1 == "y" :
    print("\nApakah Ternak Sapi Anda Mengalami Gejala Berikut Ini ? ")
    print("1. Timbulnya bengkak pada bagian perut")
    print("2. Pendarahan pada mulut, lubang hidung dan juga anus")
    print("3. Gusar karena depresi")
    print("4. Hewan terlihat gelisah")
    diag2 = input("Jawab (y/n) : ")

    if diag2 == "y" :
      print("Hasil awal diagnosa Hewan Ternak adalah :")
      print("Sapi anda terkena gejala penyakit Anthrax, Segera Periksakan ke Dokter Hewan!")
    elif diag2 == "n" :
      print("\nApakah Ternak Sapi Anda Mengalami Gejala Berikut Ini ? ")
      print("1. Gatal-Gatal\n2. Munculnya kerak berwarna keabu-abuan pada tubuh sapi")
      print("3. Bulu mulai rontok ")
      diag3 = input("Jawab (y/n) : ")

      if diag3 == "y" :
        print("Hasil awal diagnosa Hewan Ternak adalah :")
        print("Sapi anda terkena gejala penyakit Scabies, segera periksakan ke Dokter Hewan!")
      elif diag3 == "n" :
        print("Hewan Ternak anda sepertinya butuh vitamin")
      else :
        print("Hewan Ternak anda sepertinya tidak mau berobat")
    else :
      print("Hewan Ternak anda sepertinya tidak mau berobat")
  elif diag1 == "n" :
    print("Hewan Ternak anda sepertinya butuh Istirahat")
  else :
    print("Hewan Ternak anda sepertinya tidak mau berobat")

  print("\n+-----------------------------------------------+")
  pilihan = input("\nApakah Anda Ingin Melakukan Diagnosa pada Ternak Sapi ? (y/n) : ")

  if pilihan == "y" :
    os.system("clear")
    print("+--------------------------------------------------+")
    print("|\tSelamat Datang di Aplikasi Sistem Pakar \t\t|")
    print("|\tDeteksi Penyakit Anthrax & Scabies Pada Sapi \t|")
    print("+---------------------------------------------------+")
  else :
    print("+-----------------------Terimakasih------------------------+")