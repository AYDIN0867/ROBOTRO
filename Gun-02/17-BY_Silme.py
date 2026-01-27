from rembg import remove



input_file ="Gun-02\images.jpg"
output_file="Gun-02\images.png"

output=remove(input_file)
output.save(output_file)