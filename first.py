with open(r"C:\Users\IdeaPad Pro 5i\Downloads\wallpapersden.com_windows-11-black_5120x3200.jpg", "rb") as foto:
    with open("foto.jpg", "wb") as foto_kopya:
        for satir in foto:
            foto_kopya.write(satir)