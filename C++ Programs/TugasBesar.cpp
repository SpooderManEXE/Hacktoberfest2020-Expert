#include<stdio.h>
#include <string.h>
#include <iostream>
#include <fstream>

using namespace std;

//VARIABEL
//array
char a[50] ,b[50],cicil[50],merk[50],c[30],pilihlaptop, ulang, pilihtv , pilihkulkas , pilihhp, pilihbayar,pilihcicil;
int hargaSatuan,harga,cicil1 = 0, cicil2 = 0, cicil3 = 0, dp , kredit ,pilihtipe;
//fungsi
void laptop();
void tv();
void kulkas();
void hp();
void bayar();
void data();
void nota();
void transkripnota();

void sort() //untuk sort selection
{
  char benda[4][20]={"Laptop","Televisi","Smartphone","Kulkas"};
  char arr[20];
  int i,j,k;
  for(i=0;i<4;i++)
  {
    for(j=1;j<4;j++)
    {
      if(strcmp(benda[j-1],benda[j])>0)
      {
        strcpy(arr,benda[j-1]);
        strcpy(benda[j-1],benda[j]);
        strcpy(benda[j],arr);
      }
    }
  }
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << "|                 Pilihan Tipe Barang               |" << endl;
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  for(i=0;i<4;i++)
  {
    cout << "| " << i+1 <<"."<<benda[i] << endl;
  }
}

int main() //menu utama
{
  ulang :
  do {
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << "|                 Selamat Datang            	    |" << endl;
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << "|                 Toko Elektronik Dinda             |" << endl;
  cout << "|         Menjual Barang dengan Harga Terbaik       |" << endl;
  cout << "|         Cicilan tanpa Bunga , Langsung !          |" << endl;
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  sort();
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << " Pilih [1-5] : " ;cin >> pilihtipe; //inputan
  cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
    switch (pilihtipe)
    {
    case 1 :
    {kulkas(); break;}
    case 2 :
    {laptop(); break;}
    case 3 :
    {hp(); break;}
    case 4 :
    {tv(); break;}
    case 5 :
    {goto keluar;}
    }
  }
  while(pilihtipe > 5);
  bayar();
  cout << endl;
  data();
  transkripnota();

  keluar :
  cout << "Apakah anda ingin keluar? [Y / T]"; cin >> ulang;
  if(ulang=='y' || ulang=='Y'){goto selesai;} else
  if(ulang=='t' || ulang=='T'){goto ulang;}
selesai :
cin.get();
}

///UNTUK MENU PILIHAN
void laptop()
    {
       cout << "                      Laptop" << endl;
       cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
       cout << "|1. Acer Aspire E5-475G        Harga : 7000000" << endl;
       cout << "|2. HP Business ProBook 440    Harga : 6900000" << endl;
       cout << "|3. MSi GL62M                  Harga : 12999000" << endl;
       cout << "|4. Kembali ke pilihan barang " << endl;
       cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
       cout << "Pilih [1-4] : " ; cin >> pilihlaptop;
       if (pilihlaptop == '1')
      {strcpy(merk,"Acer Aspire E5-475G"); // ini string
      harga=6800000;}
      else if (pilihlaptop == '2')
      {
        strcpy(merk,"HP Business ProBook 440");
      harga=12760000;}
      else if (pilihlaptop == '3')
      {
        strcpy(merk,"MSi GL62M");
      harga=14499000;}
        else if(pilihlaptop == '4')
      { main(); }
    }
void kulkas()
{
      cout << "                      KULKAS" << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "|1. Panasonic NR-AF17AN-SS                Harga : 1700000" << endl;
      cout << "|2. Sharp Shine Series SJ-195MD-SR/SG     Harga : 2499000" << endl;
      cout << "|3. Toshiba GR-WG66ED                     Harga : 3999500" << endl;
      cout << "|4. Kembali ke pilihan barang " << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "Pilih [1-4] : " ; cin >> pilihtv;
      if (pilihtv == '1')
     {strcpy(merk,"Panasonic NR-AF17AN-SS");harga=1700000;}
     else if (pilihtv == '2')
     {strcpy(merk,"Sharp Shine Series SJ-195MD-SR/SG");harga = 2499000;}
     else if (pilihtv == '3')
     {strcpy(merk,"Toshiba GR-WG66ED"); harga=3999500;}
     else if (pilihtv == '4')
      {main();}
    }
void tv()
    {

      cout << "                      Televisi" << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "|1. Polytron PLD-55UV5900 LED TV              Harga : 10700000" << endl;
      cout << "|2. Sharp Aquos LC-50UA440 LED Smart TV       Harga : 12900000" << endl;
      cout << "|3. LG 65SJ800T Smart TV                      Harga : 24490000" << endl;
      cout << "|4. Kembali ke pilihan barang " << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "Pilih [1-4] : " ; cin >> pilihkulkas;
      if (pilihkulkas == '1')
     {strcpy(merk,"Polytron PLD-55UV5900 LED TV");harga=10700000;}
     else if (pilihkulkas == '2')
     {strcpy(merk,"Sharp Aquos LC-50UA440 LED Smart TV");harga =12900000;}
     else if (pilihkulkas == '3')
     {strcpy(merk,"LG 65SJ800T Smart TV"); harga=24490000;}
       else if (pilihkulkas == '4')
     {cout << "Kembali ke menu utama" << endl;
       main();}
    }
void hp()
    {

      cout << "                      Smartphone" << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "|1. Samsung Galaxy J7 Pro              Harga : 3800000" << endl;
      cout << "|2. Oppo F7                            Harga : 3689000" << endl;
      cout << "|3. Samsung Galaxy Note 8              Harga : 10950000" << endl;
      cout << "|4. Kembali ke pilihan barang " << endl;
      cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
      cout << "|Pilih [1-4] : " ; cin >> pilihhp;
      if (pilihhp == '1')
     {strcpy(merk,"Samsung Galaxy J7 Pro");harga=3800000;}
     else if (pilihhp == '2')
     {strcpy(merk,"Oppo F7");harga = 3689000;}
     else if (pilihhp == '3')
     {strcpy(merk,"Samsung Galaxy Note 8"); harga=10950000;}
       else if (pilihhp == '4')
     {cout << "Kembali ke menu utama" << endl;
      main();}
    }
//AKHIR DARI MENU Pilihan
// Menu penghitungan
void bayar()
{
  int ci;
//Untuk menu pembayaran
cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
cout << "|Pembayaran : " << endl;
cout << "|1. Tunai " << endl;
cout << "|2. Kredit " << endl;
cout << "|Pilih [1/2] : " ;cin >> pilihbayar;
cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
if (pilihbayar == '1')
{ cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  cout << "|Tunai" << endl;
cout << "|Jumlah Pemabayaran Rp." << harga <<",-"<< endl;
cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;}
else if (pilihbayar == '2')
{cout << "Kredit" << endl;
cout << "|Pilih lama cicilan " << endl;
cout << "|1. 3 bulan" << endl;
cout << "|2. 6 bulan" << endl;
cout << "|3. 12 bulan " << endl;
cout << "|Masukan Uang Muka terlebih dahulu Rp." ; cin >> dp;
cout << "|Pilih cicilan [1-3] : " ;cin >> kredit;
cout << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
switch (kredit)
{
case 1:
{cout << "cicilan 3 bulan " << endl;
  {strcpy(cicil,"Cicilan 3 bulan");}
  cicil1 = ((harga-dp)/3);
  for (ci=0; ci<3;ci++) // ini repetation/loop
cout << "Jumlah yang dibayar bulan ke"<<ci+1 <<" Rp." << cicil1 <<",-"<< endl;break;}
case 2:
{cout << "cicilan 6 bulan " << endl;
{strcpy(cicil,"Cicilan 6 bulan");}
  cicil2 = ((harga-dp)/6);
  for (ci=0; ci<6;ci++)
cout << "Jumlah yang dibayar bulan ke "<<ci+1 <<" Rp." << cicil2 << ",-"<< endl; break;}
case 3:
{cout << "cicilan 12 bulan " << endl;
{strcpy(cicil,"Cicilan 12 bulan");}
  cicil3 = ((harga-dp)/12);
  for (ci=0; ci<12;ci++) //repetation
cout << "Jumlah yang dibayar bulan ke "<<ci+1 <<" Rp." << cicil3 << ",-" << endl;break;}
}}
}
//Untuk Notanya

void data()
{
  cin.ignore();
  cout << "Masukan Nama Pelanggan       : " ; gets(a);
  cout << "Masukan Alamat Pelanggan     : " ; gets(b);
  cout << "Masukan Telephone Pelanggan  :  (+62)"; cin >> c;
  cout << endl;
  cout << endl;

  //ngesave data yang dibeli
  ofstream file_dindut;

	file_dindut.open("notapembelian.TXT");
	cout << "sedang diproses........." << endl;
	file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "                      NOTA PEMBELIAN ELEKTRONIK                          " << endl;
  file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "|Nama Pelanggan       : " << a << endl;
  file_dindut << "|Alamat Pelanggan     : " << b << endl;
  file_dindut << "|Telephone Pelanggan  :  (+62)" << c << endl;
  file_dindut << endl;
  file_dindut << "Barang Yang Dibeli   : "<< endl;
  file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "|     NAMA  BARANG               |    HARGA                             |" << endl;
  file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "|       " << merk << "                |" << "    Rp." <<  harga << ",-           " << endl;
  file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "|                     TOTAL                                             |" << endl;
  file_dindut << "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << "|Total Bayar                =                  Rp." << harga << ",-" << endl;
  file_dindut << "|Dp                         =                  RP." << dp << ",-" << endl;
  file_dindut << "|Cicilan                    =                   " << cicil << endl;
  file_dindut<< "|~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~|" << endl;
  file_dindut << endl;
  file_dindut<<"Terima kasih telah berbelanja di Toko Elektronik Kami"<<endl;
	file_dindut.close();
}
//file
void transkripnota()
{
	const int max=200;
	char ciwi[max+1];
	ifstream file_dindut("notapembelian.TXT");
	while(file_dindut)
	{
		file_dindut.getline(ciwi,max);
		cout << ciwi << endl;
	}

	file_dindut.close();
}
