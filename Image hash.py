import hashlib



filename = "India.jpg"


with open(filename,"rb") as f:
    file_data = f.read()
    
    
    image_hash = hashlib.sha256(file_data).hexiigest()
    
    
    print("Hash code of image:", image_hash)
