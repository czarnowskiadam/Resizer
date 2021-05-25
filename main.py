import cv2
import glob
import sys
import os
import imutils

f_name_lst = []
angles = [0, 90, 180, 270]
scale = 1.0
start = 0

def f_dir(path):
    global f_name_lst
    f_name_lst = glob.glob(path)

def counter():
    global start
    start += 1
    print(f'Przetwarzanie: {start}/{len(f_name_lst) * 4}')

def change(path, size):
    for file in range(len(f_name_lst)):
        img = cv2.imread(f_name_lst[file], 1)
        (h, w) = img.shape[:2]
        for angle in angles:
            rotated = imutils.rotate_bound(img, angle)
            if w > h:
                resized = cv2.resize(rotated, (size, round(h/w*size)))
                if angle == 90:
                    cv2.imwrite(f"{path}//{str(file)}a.png", resized)
                    counter()
                elif angle == 180:
                    cv2.imwrite(f"{path}//{str(file)}b.png", resized)
                    counter()
                elif angle == 270:
                    cv2.imwrite(f"{path}//{str(file)}c.png", resized)
                    counter()
                else:
                    cv2.imwrite(f"{path}//{str(file)}.png", resized)
                    counter()
            else:
                resized = cv2.resize(rotated, (round(w/h*size), size))
                if angle == 90:
                    cv2.imwrite(f"{path}//{str(file)}a.png", resized)
                    counter()
                elif angle == 180:
                    cv2.imwrite(f"{path}//{str(file)}b.png", resized)
                    counter()
                elif angle == 270:
                    cv2.imwrite(f"{path}//{str(file)}c.png", resized)
                    counter()
                else:
                    cv2.imwrite(f"{path}//{str(file)}.png", resized)
                    counter()

def main():
    global start
    run = True
    while run:
        start = 0
        user_input = int(input("1. Start\n2. Wyjście\n"))
        if user_input == 1:
            path = input("Podaj ścieżkę do folderu z plikami: ")
            path_resized = input("Podaj ścieżkę do folderu zapisu: ")
            resized_size = int(input("Podaj porządaną wartość długośći krawędzi zdjęcia: "))
            good_path = path + '\*.*'
            print(f'\nOtwarty folder: {path}\n')
            f_dir(good_path)
            change(path_resized, resized_size)
            print(f'\nZapis plików do folderu: {path_resized}\n')
        elif user_input == 2:
            run = False
            sys.exit("BYE!")
        else:
            print('Coś poszło nie tak...')

if __name__ == "__main__":
    main()




