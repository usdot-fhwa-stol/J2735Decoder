from CAVmessages import J2735_decode

#BSM
# payload = "001425067c0eb5842562e66e8a2b9ea6c96408b97fffffff900027d9637d07d0007fff8000640fa0"
# payload = "00145F45A6EEC002ADC4266E9C501EA6E42588CC0404000020A96DCC197966D600780405404F89D000E0C0A101653FFE100000E410A4AC1241000073810BCBC0EF0FEE08A010EFB3E83EFE00D3C11331BB96EFDC11D81182737EACFE417F07ED7510"

# SPAT
# payload = "00131900100b5a81000021a6100007047f8000001400140014780000"
# payload = "00136400382E4EEE997973CB8FA69DFB800020402015528407742C00410C0753800408683AAE3AAE01604301D4E00182180EA7001010D0755C755C03008603A9C00504301D4E003021A0EAB8EAB806810C0753800E08603A9C00804341D571D5700E02180EA700"

#MAP
# payload = "0012815338033020204bda0d4cdcf8143d4dc48811860224164802280008002297d4bc80a0a0a9825825923a90b2f2e418986f41b7006480602403812020084015480010004521d9f001414160c7c42a1879858619502a42a060e927100662000400105be6bf41c8aded5816ebc050507dcb860ec57aead5079e02828900890001000417223a50728b750f9c6ea9e8ae480a0a0f68746ad447c002828900a0880704404020803b9000200062b68d5305d1f9269a725027d8352f72867d6c82403340004000c53f5b761abbb7d35d3c0813ec1a3baac16bfc048050240301202008402208001000310fe55f849acd608d8ace136b440000dfe4808880008002086365c0017d1612eb34026067404895390907bd848050440302201c100024000200000090026180a0a0f2852600140001000000169fc1585bd1da000b00008000000a3bb2f439459a80060000400000046d55c416c67f40"
# payload = "0012829138023000201428094edb9bd3396687aa196a02dc0e200224000800518e59a274276dcf1b98e59a262e76dd28a18e59a25a676dd61f38e59a249276dd91b814146396688df9db7735a6396689479db77db4e39668a5a9db784aa050518e59a306a76de24318e59a3a1a76de34198e59a456676de3e718e59a4e8e76de3f418e59a561676de3cd920112000200186396685c89db7393c6396685eb9db744fa6396685eb9db7518463966860d9db75c76e396686309db76dc6050518e59a194a76ddd5598e59a19d276ddf3998e59a1bfa76de0c4b8e59a204a76de21c81414639668a5b9db78d6a639668cc79db790cc6396690029db793646396692909db793966396695cb9db792fe48030240281201c08400cc8001000171cb340bd4edb981f027d8c72ccf3a93b6e5551c72ccdeb53b6e46c009f624044400040005c72cd04bd3b6e566809f631cb33d4ecedb932971cb33840cedb8fc0027d890020880504403820802a900020002e396685909db727f204fb18e59a16ae76dc66218e59a156e76dc28292033200020002e396688d09db7286a04fb18e59a22d676dc66c38e59a22d676dc296013ec48010640183201c18401dc8001000b31cb34706cedb99c931cb348c7cedb9ca731cb349c6cedb9f0e31cb34a2b4edba14331cb34a53cedba37931cb34a3f4edba57331cb34a09cedba71331cb349764edba92131cb348b3cedbab0771cb347a0cedbad6402828c72cd1af33b6ebcd8c72cd186f3b6ec3d4c72cd15653b6ecd98902210001000831cb3461bcedb9beb31cb347a7cedb9e1631cb348924edba01031cb348d54edba26d31cb348c7cedba47b31cb348924edba63931cb347f84edba8a031cb34706cedbab1b71cb345eccedbadbd02828c72cd15153b6ebdc8900210803084028400"
# payload = "00123b38073000204bda1d4cdcf87b3d4dc4e8118602dc0248022800080001616c5fd08b1170fd040b02800020110022200040000af269054e5770e837b0"
payload = "00124a38073000204bda1d4cdcf87b3d4dc4e8118602dc02480228000800018f5372de666e7be818f537562266e7b3c02c0a0000804400888001000031ea6de88ccdcfade31ea6d95fccdcfe01"

decode = J2735_decode(payload,True)
# print(decode.xml)
# print(decode.json)

