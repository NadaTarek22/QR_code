# QR_code

We can generate a simple QR code using the make function of qrcode and pass the data as its parameter.

we have imported the cv2 library. We have then used the imread() function to read the image from the directory and,
the QRCodeDectector() function to detect the QR code in the image.
We have then used the detectAndDecode() function and printed the value for the users.

As a result, the detectAndDecode function returns the content of the QR code, coordinates of the corners of the box, and binarized QR code.
