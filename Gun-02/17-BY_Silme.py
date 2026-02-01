from rembg import remove



input_path ="Gun-02\images.jpg"
output_path="Gun-02\images.png"

with open (input_path,'rb') as i:
    with open(output_path,'wb') as o:
        input=i.read()
        output=remove(input)
        o.write(output)


