import leafmap.foliumap as lm
img1 = r"C:\Users\Hasan\Desktop\BTK Akademi Trae\fatsa eski meydan.jpg"
img2 = r"C:\Users\Hasan\Desktop\BTK Akademi Trae\fatsa yeni meydan.jpg"
lm.image_comparison(img1,img2,
label1 = 'Fatsa Eski Meydan',
label2 = 'Fatsa Yeni Meydan',
starting_position =50,
out_html='fatsa.html')