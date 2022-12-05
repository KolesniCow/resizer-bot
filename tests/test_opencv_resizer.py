from opencv_resizer import strech_image

new_image = strech_image(open('test_image.png', 'rb') , 1, 1)

with open('img1x1.jpg', 'wb') as first_file:
    first_file.write(new_image)

new_image = strech_image(open('test_image.png', 'rb') , 100, 100)

with open('img100x100.jpg', 'wb') as first_file:
    first_file.write(new_image)

print('test 1')
assert strech_image('buffer', 400, 300) is None
print('test 2')
assert strech_image(1 , 400, 300) is None
print('test 3')
assert strech_image(2.5 , 400, 300) is None
print('test 4')
assert strech_image(b'image', 400, 300) is None
print('test 5')
assert strech_image(buffer_with_test_image , 0, 0) is None
print('test 6')
assert strech_image(buffer_with_test_image , 0, 50) is None
print('test 7')
assert strech_image(buffer_with_test_image , 50, 0) is None
print('test 8')
assert type(strech_image(open('test_image.png', 'rb'), 400, 300)) is bytes
