import pytesseract as tess

if __name__ == "__main__":
    img_path = "./recitiation-2-5.png" 
    print(tess.image_to_string(img_path))
    #find_in_source("Screenshot.png", "/home/davidponar/workspace/academic/projects/Simulation_circuit_project/Classiq.tex")



