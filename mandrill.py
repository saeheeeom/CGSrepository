# mandrill.py
# 2019-14505 엄세희


from PIL import Image

# 이미지 파일을 읽어서 화면에 띄워 봅시다.
# import문을 실행한 뒤에 시작 가능
image = Image.open("mandrill.png")
image.show()



# 이미지를 변환해 볼 거예요.
# 변환된 결과를 보관하기 위해서 같은 크기의 빈 이미지를 만들어요.
width, height = image.size # 순서짝 size
newimg = Image.new("RGB", (width, height), (255, 255, 255)) 
# Image.new(mode, size, color)



# 확인해 보세요. 빈 이미지입니다.
newimg.show()



# 이미지를 조작하려면 픽셀 정보에 접근할 수 있게 만들어야 합니다.
# 각각의 이미지의 모든 픽셀을 변수로 지정
pixels = image.load()
newpxl = newimg.load()



# 다음 과정을 수행하기 이전에, 픽셀 정보를 한번 얻어 본다
# print('RGB = (',r,',', g, ',', b, ')')를 넣으면 
# 첫번째 픽셀의 정보를 볼 수 있다. 
x = 0
y = 0
r, g, b = pixels[x,y]



# 이제 컬러 이미지를 회색조(grayscale)로 바꾸어 봅시다.
# 그냥 RGB 값의 평균을 이용해 보지요. 
# R, G, B 값은 정수만 가능하니 // 사용
for h in range(height):
    for w in range(width):
        col = sum(pixels[w, h]) // 3
        newpxl[w, h] = (col, col, col)

newimg.show()



# 이번에는 회색조 변환 알고리즘을 이용할 거예요.
for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        gr = int(0.3*r + 0.59*g + 0.11*b)
        newpxl[w, h] = gr, gr, gr

# 회색조로 변환된 이미지를 확인해 보세요.
newimg.show()



# 흑백으로도 바꾸어 볼까요? 회색조는 흰색부터 검은색 사이에 회색을
# 배치하여 256단계로 만든 것인데요. 흑백은 흰색과 검은색만 있는 것이에요.
# 어디를 흰색과 검은색의 경계로 할지 마음대로 정해 보세요.
threshold = 128
for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        gr = int(0.3*r + 0.59*g + 0.11*b)
        if gr < threshold :
            newpxl[w, h] = 0, 0, 0
        else :
            newpxl[w, h] = 255, 255, 255



# 흑백으로 변환된 이미지를 확인해 보세요. 
# 어떤가요? 마음에 드시나요? 
# 혹시 threshold 값에 대해 이견이 있으신가요?

# threshold 값을 40, 200으로 바꾸어본 결과 
# 이미지가 명확하게 드러나지 않음을 확인할 수 있었음.
newimg.show()



# 세피아 톤으로 바꾸어 보세요.
# 다음에 있는 sepia() 함수를 만들어서 실행해 보세요.
def sepia(x, y, z) :
    xSepia = int(0.393 * x + 0.769 * y + 0.189 * z)
    ySepia = int(0.349 * x + 0.686 * y + 0.168 * z)
    zSepia = int(0.272 * x + 0.534 * y + 0.131 * z)
    if xSepia > 255: # if문이 아닌 min()으로 더 간단하게 표현가능
        xSepia = 255
    if ySepia > 255:
        ySepia = 255
    if zSepia > 255:
        zSepia = 255
    return xSepia, ySepia, zSepia

for h in range(height):
    for w in range(width):
        r, g, b = pixels[w, h]
        newpxl[w, h] = sepia(r, g, b)

newimg.show()



# 이번에 좀 어려운 것입니다.
# 모자이크를 만들어 볼 거예요.
# 일종의 구조를 가진 자료를 다루는 연습이라고 해 둘까요?
tile_height = 10
tile_width = 10

# 하나의 타일에 배정되는 RGB : 100개의 픽셀의 평균값
# 평균값을 계산하기 위한 더하는 과정 + 나누는 과정
for h in range(int(height / tile_height)): # 타일 개수
    for w in range(int(width / tile_width)):
        total = [0, 0, 0]
        for th in range(tile_height): # 하나의 타일에 배정되는 100개의 픽셀
            for tw in range(tile_width):
                r, g, b = pixels[w*tile_width + tw, h*tile_height + th]
                # 원래 이미지 상의 픽셀번호
                total[0] += r
                total[1] += g
                total[2] += b
        n = (tile_height*tile_width) # 타일에 배정된 픽셀 개수 = 100
        r = int(total[0] / n)
        g = int(total[1] / n)
        b = int(total[2] / n)
        for th in range(tile_height):
            for tw in range(tile_width):
                newpxl[w*tile_width + tw, h*tile_height + th] = r, g, b



# 확인해 보세요.
newimg.show()


# 파일로 저장할 수도 있습니다.
newimg.save("mandrill_mosaic.png", "PNG")




# 세피아 톤 변환 알고리즘이에요.
# 이걸 보지 말고 직접 만들어 보시면 좋겠죠.
def sepia(r, g, b):
        tr = 0.393*r + 0.769*g + 0.189*b
        tg = 0.349*r + 0.686*g + 0.168*b
        tb = 0.272*r + 0.534*g + 0.131*b

        tr = min(int(tr), 255)
        tg = min(int(tg), 255)
        tb = min(int(tb), 255)

        return (tr, tg, tb)
