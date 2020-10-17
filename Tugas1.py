jamMulai = 6
menitMulai = 00
jamKembali = 23
menitKembali = 50
tarif1 = 200000
tarif2 = 10000
menit = 10000//60

lamaSewajam = jamKembali - jamMulai
lamaSewamenit = menitKembali - menitMulai

totalWaktu = int(lamaSewajam + lamaSewamenit / 60)

totalbiaya = int(tarif1 + tarif2 * (totalWaktu - 12))

print("total tarif nya adalah", totalbiaya)

