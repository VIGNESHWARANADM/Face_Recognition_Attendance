import cv2

# Load an image from file
def imgPixelChange(path,rename):
    image = cv2.imread(rf'{path}')

    # Check if image is loaded properly
    if image is None:
        return "Error: Could not open or find the image."
    else:
        # Resize the image (width=216, height=216)
        resized_image = cv2.resize(image, (216, 216))

        # Display the resized image
        cv2.imshow('Resized Image', resized_image)

        # Save the resized image to a file
        cv2.imwrite(f'{rename}.jpg', resized_image)
        return resized_image



         
