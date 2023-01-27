import cv2


mon_image_path = "/Users/camille/repo/Hetic/computer_science_basics/exercices/watermark/mon_image.jpg"

mon_image_array = cv2.imread(mon_image_path, cv2.IMREAD_GRAYSCALE)
message = "chocolat au lait"

def text_to_binary(chaine_carac):
	return [format(ord(i), '08b') for i in chaine_carac]


def steganography_lsb1_text_to_image(mon_image_array, message):
	mon_image_steganographie = mon_image_array//2 * 2 #step 1
	
	binary_message = "".join(text_to_binary(message))
	number_lines, number_columns = mon_image_steganographie.shape

	for index_line in range(0, number_lines):
		for index_column in range(0, number_columns):
			
			index_in_binary_message = index_line * number_columns + index_column
			
			if index_in_binary_message < len(binary_message):
				mon_image_steganographie[index_line][index_column] += int(binary_message[index_in_binary_message])
			else:
				print(mon_image_steganographie)
				return mon_image_steganographie
				


steganography_lsb1_text_to_image(mon_image_array, message)










# binary_to_string = lambda binary : "".join([chr(int(binary_value, 2)) for binary_value in binary])








# print(mon_image_array)
# print(mon_image_even_array)

# cv2.imshow('mon precieux', mon_image_array)
# cv2.waitKey(0)